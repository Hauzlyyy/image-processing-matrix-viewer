"""Mengambil informasi dasar gambar."""
import os


def get_image_info(filename: str, loaded: dict) -> dict:
    h, w = loaded["rgb"].shape[:2]
    ext = os.path.splitext(filename)[1].lstrip(".").upper()
    fmt = "JPEG" if ext in ("JPG", "JPEG") else ext
    raw = loaded["raw"]
    channels = 1 if raw.ndim == 2 else raw.shape[2]
    mode = {1: "Grayscale", 3: "RGB", 4: "RGBA"}.get(channels, "Unknown")
    return {
        "Nama File": filename,
        "Format": fmt,
        "Lebar": f"{w} px",
        "Tinggi": f"{h} px",
        "Resolusi": f"{w} × {h}",
        "Channel": channels,
        "Mode": mode,
        "Bit Depth": f"{loaded['bit_depth']}-bit",
        "Total Piksel": f"{w * h:,}".replace(",", "."),
    }
