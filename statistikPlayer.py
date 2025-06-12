import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

@st.cache_data
def load_data():
    csv_path = os.path.join(os.path.dirname(__file__), "data", "NFL_Combined_Recent_100K.csv")
    df = pd.read_csv(csv_path)
    df = df[["Player", "Season", "Passing Yards", "Touchdowns"]]
    df = df.dropna(subset=["Player", "Season"])
    df["Season"] = df["Season"].astype(int)
    return df

def get_csv_players():
    df = load_data()
    return df["Player"].unique().tolist()

def show_player_details(player_name):
    st.title("📊 Statistik Musiman Pemain NFL")
    df = load_data()
    player_df = df[df["Player"] == player_name].sort_values("Season")

    if player_df.empty:
        st.warning("Statistik pemain tidak tersedia.")
        return

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=player_df, x="Season", y="Passing Yards", marker="o", label="Passing Yards", ax=ax)
    sns.lineplot(data=player_df, x="Season", y="Touchdowns", marker="s", label="Touchdowns", ax=ax)
    ax.set_title(f"Statistik Musiman: {player_name}")
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    avg_passing = player_df["Passing Yards"].mean()
    avg_td = player_df["Touchdowns"].mean()
    st.subheader("🔍 Rata-Rata Statistik")
    st.metric("Rata-rata Passing Yards", f"{avg_passing:.1f}")
    st.metric("Rata-rata Touchdowns", f"{avg_td:.1f}")
