import pandas as pd

# Fungsi untuk pencarian berdasarkan nama lengkap pemain
def search_player_by_full_name(players_data, full_name):
    result = players_data[players_data['Player'].str.contains(full_name, case=False, na=False)]
    return result if not result.empty else None

# Fungsi untuk pencarian berdasarkan sebagian nama pemain (autocomplete)
def search_player_by_partial_name(players_data, partial_name):
    result = players_data[players_data['Player'].str.contains(partial_name, case=False, na=False)]
    return result if not result.empty else None

# Fungsi untuk filter berdasarkan posisi
def filter_by_position(players_data, position):
    result = players_data[players_data['Position'] == position]
    return result if not result.empty else None

# Fungsi untuk filter berdasarkan musim
def filter_by_season(players_data, season):
    result = players_data[players_data['Season'] == season]
    return result if not result.empty else None

# Fungsi untuk menangani input yang tidak valid
def handle_invalid_input():
    return "Pemain tidak ditemukan"
