import streamlit as st
import pandas as pd
from detailPlayer import show_player_details

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

    players = df['Player'].drop_duplicates().sort_values()
    selected_player = st.selectbox("Pilih pemain:", players)

    if selected_player:
        show_player_details(df, selected_player)
