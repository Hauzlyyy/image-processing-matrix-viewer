"""Image Processing & Matrix Viewer — Tugas Mandiri Pengolahan Citra Digital."""
import streamlit as st

from components.uploader import render_uploader
from components.display import show_info, show_image
from components.matrix_view import show_matrix
from modules.image_loader import load_image, ImageLoadError
from modules.image_info import get_image_info
from modules import image_processor as ip

st.set_page_config(page_title="Image Processing & Matrix Viewer", layout="wide")
st.title("IMAGE PROCESSING & MATRIX VIEWER")
st.caption("Pengolahan Citra Digital — biner, grayscale, RGB (8/16 bit) dan representasi matriks")

file = render_uploader()
if file is None:
    st.stop()

try:
    loaded = load_image(file.getvalue(), file.name)
except ImageLoadError as e:
    st.error(str(e))
    st.stop()

base_name = file.name.rsplit(".", 1)[0]
info = get_image_info(file.name, loaded)
show_info(info)
st.divider()

tabs = st.tabs(["Original", "Biner", "Grayscale", "RGB", "Matriks"])

# --- Original ---------------------------------------------------------
with tabs[0]:
    st.subheader("Gambar Asli")
    show_image(loaded["rgb"], "Original", f"Resolusi: {info['Resolusi']}",
               "dl_orig", f"{base_name}_original.png")

# --- Biner ------------------------------------------------------------
with tabs[1]:
    st.subheader("Citra Biner")
    method = st.radio("Metode threshold", ["Manual", "Otsu (otomatis)"], horizontal=True)
    if method == "Manual":
        thr = st.slider("Nilai threshold", 0, 255, 127)
        binary, used = ip.to_binary(loaded, "manual", thr)
    else:
        binary, used = ip.to_binary(loaded, "otsu")
    show_image(binary, f"Biner (threshold = {used})", "Nilai: 0 = Hitam, 255 = Putih",
               "dl_bin", f"{base_name}_biner.png")

# --- Grayscale --------------------------------------------------------
gray8 = ip.to_gray8(loaded)
gray16 = ip.to_gray16(loaded)
with tabs[2]:
    st.subheader("Grayscale")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Grayscale 8-bit**")
        show_image(gray8, "Grayscale 8-bit", "Rentang: 0 - 255",
                   "dl_g8", f"{base_name}_gray8.png")
    with c2:
        st.markdown("**Grayscale 16-bit**")
        show_image(gray16, "Grayscale 16-bit", "Rentang: 0 - 65535",
                   "dl_g16", f"{base_name}_gray16.png")
    st.caption("Catatan: layar menampilkan 8-bit, sehingga gambar 16-bit terlihat sama; "
               "perbedaannya ada pada nilai piksel (lihat tab Matriks) dan file PNG 16-bit hasil download.")

# --- RGB --------------------------------------------------------------
rgb8 = ip.to_rgb8(loaded)
rgb16 = ip.to_rgb16(loaded)
with tabs[3]:
    st.subheader("RGB")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**RGB 8-bit**")
        show_image(rgb8, "RGB 8-bit", "R, G, B = 0 - 255", "dl_r8", f"{base_name}_rgb8.png")
    with c2:
        st.markdown("**RGB 16-bit**")
        show_image(rgb16, "RGB 16-bit", "R, G, B = 0 - 65535", "dl_r16", f"{base_name}_rgb16.png")

# --- Matriks ----------------------------------------------------------
with tabs[4]:
    st.subheader("Representasi Matriks")
    pilihan = st.selectbox("Pilih citra", [
        "Biner", "Grayscale 8-bit", "Grayscale 16-bit", "RGB 8-bit", "RGB 16-bit"])
    data = {"Biner": binary, "Grayscale 8-bit": gray8, "Grayscale 16-bit": gray16,
            "RGB 8-bit": rgb8, "RGB 16-bit": rgb16}[pilihan]
    show_matrix(data, pilihan, key=pilihan.replace(" ", "_"),
                csv_name=f"{base_name}_{pilihan.replace(' ', '_').lower()}.csv")
