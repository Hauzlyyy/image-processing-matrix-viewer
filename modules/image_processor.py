"""Konversi citra: biner, grayscale 8/16 bit, RGB 8/16 bit.
Semua hasil mempertahankan resolusi gambar input."""
import numpy as np
import cv2


def to_gray8(loaded: dict) -> np.ndarray:
    """Grayscale 8-bit (0-255)."""
    return cv2.cvtColor(loaded["rgb"], cv2.COLOR_RGB2GRAY)


def to_gray16(loaded: dict) -> np.ndarray:
    """Grayscale 16-bit (0-65535).
    Sumber 16-bit -> dihitung dari data asli. Sumber 8-bit -> skala x257 (255*257=65535)."""
    base = loaded["base"]
    if base.dtype == np.uint16:
        if base.ndim == 2:
            return base.copy()
        g = 0.299 * base[:, :, 0] + 0.587 * base[:, :, 1] + 0.114 * base[:, :, 2]
        return np.clip(g, 0, 65535).astype(np.uint16)
    return to_gray8(loaded).astype(np.uint16) * 257


def to_binary(loaded: dict, method: str = "manual", threshold: int = 127):
    """Citra biner: nilai hanya 0 (hitam) atau 255 (putih).
    Mengembalikan (array biner, threshold yang dipakai)."""
    gray = to_gray8(loaded)
    if method == "otsu":
        t, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return binary, int(t)
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    return binary, int(threshold)


def to_rgb8(loaded: dict) -> np.ndarray:
    """RGB 8-bit (H, W, 3), 0-255."""
    return loaded["rgb"].copy()


def to_rgb16(loaded: dict) -> np.ndarray:
    """RGB 16-bit (H, W, 3), 0-65535."""
    base = loaded["base"]
    if base.dtype == np.uint16:
        return base.copy() if base.ndim == 3 else np.stack([base] * 3, axis=-1)
    return loaded["rgb"].astype(np.uint16) * 257


def to_display8(arr: np.ndarray) -> np.ndarray:
    """Ubah array 16-bit ke 8-bit hanya untuk ditampilkan di layar."""
    return (arr >> 8).astype(np.uint8) if arr.dtype == np.uint16 else arr


def encode_png(arr: np.ndarray) -> bytes:
    """Encode array (8/16 bit, gray atau RGB) ke PNG. PNG mendukung 16-bit."""
    out = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR) if arr.ndim == 3 else arr
    ok, buf = cv2.imencode(".png", out)
    return buf.tobytes() if ok else b""
