import streamlit as st

# Simulasi data pemain
data_pemain = {
    "Patrick Mahomes": {
        "nama": "Patrick Mahomes",
        "tim": "Kansas City Chiefs",
        "tinggi": "6 ft 3 in",
        "berat": "230 lbs",
        "usia": 28,
        "perguruan_tinggi": "Texas Tech",
        "asal": "Tyler, Texas",
        "statistik": {
            "2020": {"yards": 4740, "touchdowns": 38},
            "2021": {"yards": 4839, "touchdowns": 37},
            "2022": {"yards": 5250, "touchdowns": 41},
        }
    },
    "Tom Brady": {
        "nama": "Tom Brady",
        "tim": "Retired",
        "tinggi": "6 ft 4 in",
        "berat": "225 lbs",
        "usia": 46,
        "perguruan_tinggi": "Michigan",
        "asal": "San Mateo, California",
        "statistik": {
            "2020": {"yards": 4633, "touchdowns": 40},
            "2021": {"yards": 5316, "touchdowns": 43},
            "2022": {"yards": 4694, "touchdowns": 25},
        }
    },
    "Justin Herbert": {
        "nama": "Justin Herbert",
        "tim": "Los Angeles Chargers",
        "tinggi": "6 ft 6 in",
        "berat": "236 lbs",
        "usia": 26,
        "perguruan_tinggi": "Oregon",
        "asal": "Eugene, Oregon",
        "statistik": {
            "2020": {"yards": 4336, "touchdowns": 31},
            "2021": {"yards": 5014, "touchdowns": 38},
            "2022": {"yards": 4739, "touchdowns": 25},
        }
    },
    "Josh Allen": {
        "nama": "Josh Allen",
        "tim": "Buffalo Bills",
        "tinggi": "6 ft 5 in",
        "berat": "237 lbs",
        "usia": 27,
        "perguruan_tinggi": "Wyoming",
        "asal": "Firebaugh, California",
        "statistik": {
            "2020": {"yards": 4544, "touchdowns": 37},
            "2021": {"yards": 4407, "touchdowns": 36},
            "2022": {"yards": 4283, "touchdowns": 35},
        }
    }
}

def tampilkan_detail_pemain(nama_pemain):
    pemain = data_pemain.get(nama_pemain)

    if not pemain:
        st.error("Pemain tidak ditemukan di database.")
        return

    st.header(f"{pemain['nama']} ({pemain['tim']})")

    with st.expander("Atribut Fisik"):
        st.write(f"Tinggi: {pemain['tinggi']}")
        st.write(f"Berat: {pemain['berat']}")
        st.write(f"Usia: {pemain['usia']}")

    with st.expander("Asal dan Perguruan Tinggi"):
        st.write(f"Perguruan Tinggi: {pemain['perguruan_tinggi']}")
        st.write(f"Asal: {pemain['asal']}")

    with st.expander("Statistik per Musim"):
        total_yards = 0
        total_touchdowns = 0
        musim_count = len(pemain["statistik"])

        for musim, stats in pemain["statistik"].items():
            st.write(f"**{musim}** - Yards: {stats['yards']}, Touchdowns: {stats['touchdowns']}")
            total_yards += stats['yards']
            total_touchdowns += stats['touchdowns']

    with st.expander("Ringkasan Statistik"):
        if musim_count > 0:
            rata_yards = total_yards / musim_count
            rata_touchdowns = total_touchdowns / musim_count
            st.write(f"Total Yards: {total_yards}")
            st.write(f"Rata-rata Yards: {rata_yards:.2f}")
            st.write(f"Total Touchdowns: {total_touchdowns}")
            st.write(f"Rata-rata Touchdowns: {rata_touchdowns:.2f}")
        else:
            st.warning("Statistik belum tersedia.")