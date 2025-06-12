# statistik.py
import streamlit as st
import pandas as pd
import plotly.express as px

def show_player_stats_chart(df, player_name):
    if player_name not in df['Player'].values:
        st.warning("Pemain tidak ditemukan.")
        return

    player_df = df[df['Player'] == player_name]

    if 'Season' not in player_df.columns:
        st.error("Kolom 'Season' tidak tersedia dalam dataset.")
        return

    st.subheader("📈 Statistik Visualisasi per Musim")

    numeric_cols = ['Passing Yards', 'Rushing Yards', 'Receiving Yards', 'Touchdowns']
    available_stats = [col for col in numeric_cols if col in player_df.columns]

    if not available_stats:
        st.warning("Tidak ada statistik numerik tersedia untuk divisualisasikan.")
        return

    selected_stat = st.selectbox("Pilih Statistik yang Ingin Dilihat", available_stats)

    fig = px.line(
        player_df.sort_values('Season'),
        x='Season',
        y=selected_stat,
        title=f'{selected_stat} per Season untuk {player_name}',
        markers=True
    )

    fig.update_layout(template="plotly_white", height=400)
    st.plotly_chart(fig, use_container_width=True)

