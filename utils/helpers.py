"""Fungsi pendukung."""
import numpy as np

MATRIX_OPTIONS = {
    "10 × 10 pertama": 10,
    "20 × 20 pertama": 20,
    "50 × 50 pertama": 50,
    "Matriks lengkap": None,
}
DEFAULT_MATRIX = "20 × 20 pertama"
FULL_MATRIX_WARN_PIXELS = 250_000


def value_range(arr: np.ndarray) -> str:
    return f"min = {int(arr.min())}, max = {int(arr.max())}"


def full_matrix_too_big(arr: np.ndarray) -> bool:
    return arr.shape[0] * arr.shape[1] > FULL_MATRIX_WARN_PIXELS
