import streamlit as st
from modules.image_loader import SUPPORTED_EXT


def render_uploader():
    st.subheader("Upload Gambar")
    f = st.file_uploader(
        "Format yang didukung: JPG / JPEG / PNG / BMP",
        type=list(SUPPORTED_EXT),
    )
    if f is None:
        st.info("Silakan pilih gambar terlebih dahulu.")
    return f
