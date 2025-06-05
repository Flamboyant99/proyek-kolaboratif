import streamlit as st
from detailPlayer import tampilkan_detail_pemain

st.set_page_config(page_title="Detail Pemain NFL", layout="wide")
st.title("NFL StatHive - Detail Pemain")

daftar_pemain = ["Patrick Mahomes", "Tom Brady", "Justin Herbert", "Josh Allen"]
pemain_dipilih = st.selectbox("Pilih pemain:", daftar_pemain)

tampilkan_detail_pemain(pemain_dipilih)