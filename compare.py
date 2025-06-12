import streamlit as st

def compare_players(df, player1, player2):
    # Pastikan kedua pemain ada di dalam DataFrame
    if player1 not in df['Player'].values or player2 not in df['Player'].values:
        st.warning("Salah satu atau kedua pemain yang dipilih tidak ditemukan dalam dataset.")
        return
    
    # Memastikan kolom yang diperlukan ada dalam DataFrame
    if 'Receptions' not in df.columns or 'Tackles' not in df.columns:
        st.warning("Kolom 'Receptions' atau 'Tackles' tidak ditemukan dalam data. Perbandingan akan dilakukan pada statistik yang tersedia.")
    
    # Ambil data pemain 1 dan pemain 2
    player1_data = df[df['Player'] == player1].iloc[0]
    player2_data = df[df['Player'] == player2].iloc[0]

    # Menampilkan informasi umum kedua pemain
    st.subheader(f"Detail Perbandingan: {player1} vs {player2}")
    
    st.write(f"{player1}:")
    st.write(player1_data)
    
    st.write(f"{player2}:")
    st.write(player2_data)

    # Bandingkan statistik jika kolom ada
    if 'Receptions' in df.columns and 'Tackles' in df.columns:
        st.write(f"{player1} Receptions**: {player1_data['Receptions']}")
        st.write(f"{player2} Receptions**: {player2_data['Receptions']}")

        st.write(f"{player1} Tackles**: {player1_data['Tackles']}")
        st.write(f"{player2} Tackles**: {player2_data['Tackles']}")

    # Perbandingan statistik lainnya, jika ada
    # Misalnya: 'Yards', 'Touchdowns', dll.
    if 'Yards' in df.columns:
        st.write(f"{player1} Yards**: {player1_data['Yards']}")
        st.write(f"{player2} Yards**: {player2_data['Yards']}")
    
    if 'Touchdowns' in df.columns:
        st.write(f"{player1} Touchdowns**: {player1_data['Touchdowns']}")
        st.write(f"{player2} Touchdowns**: {player2_data['Touchdowns']}")
