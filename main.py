import pathlib
import streamlit as st
import pandas as pd
import os
import json

from detailPlayer import show_player_details
from statistikPlayer import show_player_stats_chart
from compare import compare_players
from search import (
    search_player_by_full_name,
    search_player_by_partial_name,
    filter_by_position,
    filter_by_season,
    handle_invalid_input,
)
from favorite import add_to_favorites, remove_from_favorites, get_favorites

# -------------------------------------------------- #
# Konfigurasi halaman
# -------------------------------------------------- #
st.set_page_config(page_title="NFL Player Stats Viewer", layout="wide")

# Background NFL
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/NFL_2023_logo.svg/2560px-NFL_2023_logo.svg.png");
        background-size: 30%;
        background-repeat: no-repeat;
        background-position: top left;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🏈 NFL Player Stats Viewer")

# -------------------------------------------------- #
# Upload Dataset
# -------------------------------------------------- #
uploaded_file = st.file_uploader(
    "Upload dataset NFL (CSV atau Excel)", type=["csv", "xlsx", "xls"]
)

def load_dataframe(file_obj):
    ext = pathlib.Path(file_obj.name).suffix.lower()
    try:
        if ext == ".csv":
            df_tmp = pd.read_csv(file_obj)
        elif ext in [".xlsx", ".xls"]:
            df_tmp = pd.read_excel(file_obj)
        else:
            st.error("Tipe file tidak didukung.")
            return None
    except Exception as e:
        st.error(f"Gagal memuat file: {e}")
        return None

    required_cols = {"Player", "Position", "Season"}
    if not required_cols.issubset(df_tmp.columns):
        st.error(f"Dataset harus memiliki kolom: {required_cols}")
        return None

    return df_tmp.dropna(subset=["Player"])

# -------------------------------------------------- #
# MAIN LOGIC
# -------------------------------------------------- #
if uploaded_file:
    df = load_dataframe(uploaded_file)

    if df is None:
        st.stop()

    st.success("✅ Dataset berhasil dimuat.")
    players = df["Player"].drop_duplicates().sort_values()
    selected_player = st.selectbox("Pilih Pemain untuk Lihat Detail:", players)

    if selected_player:
        show_player_details(df, selected_player)
        show_player_stats_chart(df, selected_player)

    # ---------------------------------------------- #
    # ⭐ Manajemen Pemain Favorit
    # ---------------------------------------------- #
    st.markdown("---")
    st.subheader("⭐ Manajemen Pemain Favorit")

    if st.button(f"➕ Tambahkan {selected_player} ke Favorit"):
        st.success(add_to_favorites(selected_player))
        st.rerun()

    st.markdown("#### 📋 Daftar Pemain Favorit:")
    favorit_list = get_favorites()

    if favorit_list:
        for fav in favorit_list:
            col1, col2 = st.columns([5, 1])
            with col1:
                st.write(f"🔹 {fav}")
            with col2:
                if st.button("❌", key=f"hapus_{fav}"):
                    st.warning(remove_from_favorites(fav))
                    st.rerun()
    else:
        st.info("Belum ada pemain favorit.")

    # ---------------------------------------------- #
    # ⚔ Perbandingan Pemain
    # ---------------------------------------------- #
    st.markdown("---")
    st.subheader("⚔ Perbandingan Pemain")

    col_a, col_b = st.columns(2)
    with col_a:
        player1 = st.selectbox("Pemain Pertama:", players, key="cmp1")
    with col_b:
        player2 = st.selectbox("Pemain Kedua:", players, key="cmp2")

    if player1 and player2:
        if player1 != player2:
            compare_players(df, player1, player2)
        else:
            st.warning("Pilih dua pemain yang **berbeda** untuk dibandingkan.")

    # ---------------------------------------------- #
    # 🔍 Pencarian & Filter
    # ---------------------------------------------- #
    st.markdown("---")
    st.subheader("🔍 Pencarian Pemain Berdasarkan Nama, Posisi, dan Musim")

    name_query = st.text_input("Cari Pemain Berdasarkan Nama")
    if name_query:
        exact = search_player_by_full_name(df, name_query)
        if exact is not None:
            st.write("✅ Pemain Ditemukan:", exact)
        else:
            partial = search_player_by_partial_name(df, name_query)
            if partial is not None:
                st.write("🔎 Hasil Pencarian Parsial:", partial)
            else:
                st.warning(handle_invalid_input())

    posisi_opt = ["Semua"] + sorted(df["Position"].dropna().unique())
    pos_choice = st.selectbox("Filter Berdasarkan Posisi", posisi_opt)
    if pos_choice != "Semua":
        pos_df = filter_by_position(df, pos_choice)
        if pos_df is not None:
            st.write(f"Pemain posisi {pos_choice}:", pos_df)
        else:
            st.warning(f"Tidak ada pemain pada posisi {pos_choice}.")

    seasons = sorted(df["Season"].dropna().unique(), reverse=True)
    season_choice = st.selectbox("Filter Berdasarkan Musim", seasons)
    season_df = filter_by_season(df, season_choice)
    if season_df is not None:
        st.write(f"Pemain musim {season_choice}:", season_df)
    else:
        st.warning(f"Tidak ada pemain pada musim {season_choice}.")
else:
    st.info("📁 Silakan upload file CSV/Excel berisi data pemain NFL untuk memulai.")
