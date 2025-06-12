import streamlit as st

def show_player_details(df, player_name):
    player_data = df[df['Player'] == player_name]

    if player_data.empty:
        st.warning("Pemain tidak ditemukan.")
        return

    st.header(f"📌 Detail Pemain: {player_name}")

    # Nama dan tim
    team = player_data['Current Team'].iloc[0] if 'Current Team' in player_data.columns else "N/A"
    st.subheader(f"Team: {team}")

    # Atribut fisik
    height = player_data['Height (inches)'].iloc[0] if 'Height (inches)' in player_data.columns else "N/A"
    weight = player_data['Weight (lbs)'].iloc[0] if 'Weight (lbs)' in player_data.columns else "N/A"
    age = player_data['Age'].iloc[0] if 'Age' in player_data.columns else "N/A"
    st.markdown(f"**Tinggi:** {height} in  \n**Berat:** {weight} lbs  \n**Usia:** {age}")

    # Perguruan tinggi dan tempat lahir
    college = player_data['College'].iloc[0] if 'College' in player_data.columns else "N/A"
    birthplace = player_data['Birth Place'].iloc[0] if 'Birth Place' in player_data.columns else "N/A"
    st.markdown(f"**Perguruan Tinggi:** {college}  \n**Tempat Lahir:** {birthplace}")

    # Statistik per musim
    if 'Season' in player_data.columns and 'Passing Yards' in player_data.columns:
        st.subheader("📊 Statistik per Musim")
        season_stats = player_data[['Season', 'Passing Yards', 'Touchdowns']].drop_duplicates()
        st.dataframe(season_stats.sort_values('Season'))

    # Statistik total dan rata-rata
    numeric_cols = ['Passing Yards', 'Touchdowns']
    valid_cols = [col for col in numeric_cols if col in player_data.columns]

    if valid_cols:
        st.subheader("📈 Ringkasan Statistik")
        total_stats = player_data[valid_cols].sum().to_frame(name="Total")
        avg_stats = player_data[valid_cols].mean().round(2).to_frame(name="Rata-rata")
        summary_df = total_stats.join(avg_stats)
        st.table(summary_df)