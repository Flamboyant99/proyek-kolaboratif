import json
import os

FAVORITE_FILE = "favorites.json"

# Load daftar favorit dari file JSON
def load_favorites():
    if os.path.exists(FAVORITE_FILE):
        with open(FAVORITE_FILE, "r") as f:
            return json.load(f)
    return []

# Simpan daftar favorit ke file JSON
def save_favorites(favorites):
    with open(FAVORITE_FILE, "w") as f:
        json.dump(favorites, f)

# Tambah pemain ke favorit
def add_to_favorites(player_name):
    favorites = load_favorites()
    if player_name not in favorites:
        favorites.append(player_name)
        save_favorites(favorites)
        return f"{player_name} ditambahkan ke favorit."
    return f"{player_name} sudah ada di favorit."

# Hapus pemain dari favorit
def remove_from_favorites(player_name):
    favorites = load_favorites()
    if player_name in favorites:
        favorites.remove(player_name)
        save_favorites(favorites)
        return f"{player_name} dihapus dari favorit."
    return f"{player_name} tidak ditemukan di favorit."

# Ambil semua pemain favorit
def get_favorites():
    return load_favorites()
