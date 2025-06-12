import streamlit as st
import pandas as pd
from detailPlayer import show_player_details
from search import search_player_by_full_name, search_player_by_partial_name, filter_by_position, filter_by_season, handle_invalid_input

# Judul dan background
st.set_page_config(page_title="NFL Player Stats Viewer", layout="wide")
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/NFL_2023_logo.svg/2560px-NFL_2023_logo.svg.png");
    background-size: cover;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Upload dataset
st.title("🏈 NFL Player Stats Viewer")
uploaded_file = st.file_uploader("Upload dataset NFL (.csv)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df = df.dropna(subset=['Player'])  # pastikan kolom Player ada isinya

    # Menampilkan pemain yang tersedia
    players = df['Player'].drop_duplicates().sort_values()
    selected_player = st.selectbox("Pilih pemain:", players)

    if selected_player:
        # Menampilkan detail pemain yang dipilih
        show_player_details(df, selected_player)

    # Pencarian Pemain
    st.subheader("Pencarian Pemain Berdasarkan Nama, Posisi, dan Musim")

    # Input untuk nama pemain
    player_name = st.text_input("Cari Pemain Berdasarkan Nama", "")

    # Pencarian berdasarkan nama pemain
    if player_name:
        # Pencarian berdasarkan nama lengkap
        player = search_player_by_full_name(df, player_name)
        if player is not None:
            st.write("Pemain Ditemukan:", player)
        else:
            # Pencarian sebagian nama (autocomplete)
            partial_search = search_player_by_partial_name(df, player_name)
            if partial_search is not None:
                st.write("Pemain Ditemukan:", partial_search)
            else:
                st.write(handle_invalid_input())

    # Filter berdasarkan posisi (misal QB)
    position = st.selectbox("Filter Berdasarkan Posisi", ['Semua', 'QB', 'WR', 'RB'])
    if position != 'Semua':
        filtered_players = filter_by_position(df, position)
        if filtered_players is not None:
            st.write(f"Pemain dengan posisi {position}:", filtered_players)
        else:
            st.write(f"Tidak ada pemain ditemukan untuk posisi: {position}")

    # Filter berdasarkan musim (misal 2023)
    season = st.selectbox("Filter Berdasarkan Musim", [2023, 2022, 2021])
    filtered_season_players = filter_by_season(df, season)
    if filtered_season_players is not None:
        st.write(f"Pemain untuk musim {season}:", filtered_season_players)
    else:
        st.write(f"Tidak ada pemain ditemukan untuk musim {season}")
print ("hello world")