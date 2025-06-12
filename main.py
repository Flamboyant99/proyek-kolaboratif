# main.py
import streamlit as st
import pandas as pd
from detailPlayer import show_player_details
from statistikPlayer import show_player_stats_chart  # diperbaiki nama modul
from search import (
    search_player_by_full_name,
    search_player_by_partial_name,
    filter_by_position,
    filter_by_season,
    handle_invalid_input
)

# Konfigurasi halaman
st.set_page_config(page_title="NFL Player Stats Viewer", layout="wide")

# Background style NFL
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/NFL_2023_logo.svg/2560px-NFL_2023_logo.svg.png");
    background-size: 30%;
    background-repeat: no-repeat;
    background-position: top left;
    background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Judul
st.title("🏈 NFL Player Stats Viewer")

# Upload Dataset
uploaded_file = st.file_uploader("Upload dataset NFL (.csv)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df = df.dropna(subset=['Player'])

    st.success("✅ Dataset berhasil dimuat.")

    # Pilih pemain
    players = df['Player'].drop_duplicates().sort_values()
    selected_player = st.selectbox("Pilih Pemain untuk Lihat Detail:", players)

    if selected_player:
        # Tampilkan Detail
        show_player_details(df, selected_player)

        # Tampilkan Statistik Visualisasi
        show_player_stats_chart(df, selected_player)

    # -------------------- Pencarian dan Filter -------------------- #
    st.markdown("---")
    st.subheader("🔍 Pencarian Pemain Berdasarkan Nama, Posisi, dan Musim")

    # Cari berdasarkan nama lengkap atau sebagian
    player_name = st.text_input("Cari Pemain Berdasarkan Nama", "")

    if player_name:
        player = search_player_by_full_name(df, player_name)
        if player is not None:
            st.write("✅ Pemain Ditemukan:", player)
        else:
            partial_result = search_player_by_partial_name(df, player_name)
            if partial_result is not None:
                st.write("🔎 Hasil Pencarian Parsial:", partial_result)
            else:
                st.warning(handle_invalid_input())

    # Filter berdasarkan posisi
    posisi_tersedia = ['Semua'] + sorted(df['Position'].dropna().unique())
    position = st.selectbox("Filter Berdasarkan Posisi", posisi_tersedia)
    if position != 'Semua':
        filtered_by_pos = filter_by_position(df, position)
        if filtered_by_pos is not None:
            st.write(f"Pemain dengan posisi {position}:", filtered_by_pos)
        else:
            st.warning(f"Tidak ada pemain ditemukan untuk posisi {position}.")

    # Filter berdasarkan musim
    if 'Season' in df.columns:
        seasons = sorted(df['Season'].dropna().unique(), reverse=True)
        selected_season = st.selectbox("Filter Berdasarkan Musim", seasons)
        filtered_by_season = filter_by_season(df, selected_season)
        if filtered_by_season is not None:
            st.write(f"Pemain pada musim {selected_season}:", filtered_by_season)
        else:
            st.warning(f"Tidak ada pemain ditemukan pada musim {selected_season}.")

else:
    st.info("📁 Silakan upload file CSV berisi data pemain NFL untuk memulai.")
