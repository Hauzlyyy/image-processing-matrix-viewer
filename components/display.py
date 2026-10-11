import streamlit as st
from modules.image_processor import to_display8, encode_png


def show_info(info: dict):
    st.subheader("Informasi Gambar")
    cols = st.columns(3)
    for i, (k, v) in enumerate(info.items()):
        cols[i % 3].metric(k, str(v))


def show_image(arr, caption: str, value_note: str, key: str, filename: str):
    """Tampilkan gambar pada resolusi aslinya + tombol download PNG."""
    h, w = arr.shape[:2]
    st.image(to_display8(arr), caption=f"{caption} — {w} × {h} px",
             clamp=True, use_container_width=True)
    st.caption(value_note)
    st.download_button("Download PNG", encode_png(arr), file_name=filename,
                       mime="image/png", key=key)
