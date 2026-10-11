"""Membaca file gambar (JPG, JPEG, PNG, BMP) tanpa mengubah resolusi."""
import numpy as np
import cv2

SUPPORTED_EXT = ("jpg", "jpeg", "png", "bmp")


class ImageLoadError(Exception):
    pass


def validate_extension(filename: str) -> bool:
    return filename.lower().rsplit(".", 1)[-1] in SUPPORTED_EXT


def load_image(file_bytes: bytes, filename: str) -> dict:
    """
    Mengembalikan dict:
      raw      : array asli (dtype asli, bisa uint8/uint16, 2D atau 3D)
      base     : array RGB/gray dengan dtype asli
      rgb      : array RGB uint8 (H, W, 3) untuk proses konversi
      bit_depth: bit depth per channel file asli (8 atau 16)
    """
    if not validate_extension(filename):
        raise ImageLoadError(
            "Format file tidak didukung.\nGunakan JPG, JPEG, PNG, atau BMP."
        )

    buf = np.frombuffer(file_bytes, dtype=np.uint8)
    raw = cv2.imdecode(buf, cv2.IMREAD_UNCHANGED)  # pertahankan bit depth asli
    if raw is None:
        raise ImageLoadError(
            "Gambar tidak dapat diproses.\nSilakan gunakan file gambar lain."
        )

    bit_depth = 16 if raw.dtype == np.uint16 else 8
    if raw.dtype not in (np.uint8, np.uint16):
        raw = cv2.normalize(raw, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        bit_depth = 8

    # Buang alpha, ubah BGR -> RGB
    if raw.ndim == 2:
        base = raw
    elif raw.shape[2] == 4:
        base = cv2.cvtColor(raw[:, :, :3], cv2.COLOR_BGR2RGB)
    else:
        base = cv2.cvtColor(raw, cv2.COLOR_BGR2RGB)

    base8 = (base >> 8).astype(np.uint8) if base.dtype == np.uint16 else base
    rgb8 = np.stack([base8] * 3, axis=-1) if base8.ndim == 2 else base8

    return {
        "raw": raw,
        "base": base,
        "rgb": rgb8,
        "bit_depth": bit_depth,
        "is_gray_source": raw.ndim == 2,
    }
