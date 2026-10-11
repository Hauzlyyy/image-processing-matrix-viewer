"""Representasi citra dalam bentuk matriks."""
import numpy as np
import pandas as pd


def crop_matrix(arr: np.ndarray, size) -> np.ndarray:
    """Ambil size x size pertama. size=None -> matriks lengkap."""
    return arr if size is None else arr[:size, :size]


def to_dataframe(arr: np.ndarray) -> pd.DataFrame:
    """Gray/biner -> tabel angka. RGB -> sel berisi string '(R,G,B)'."""
    if arr.ndim == 2:
        df = pd.DataFrame(arr)
    else:
        h, w, _ = arr.shape
        cells = [[f"({arr[i, j, 0]},{arr[i, j, 1]},{arr[i, j, 2]})"
                  for j in range(w)] for i in range(h)]
        df = pd.DataFrame(cells)
    df.index.name = "baris"
    return df


def to_channel_dataframes(arr: np.ndarray) -> dict:
    """Pecah RGB menjadi matriks R, G, B terpisah."""
    return {n: pd.DataFrame(arr[:, :, i]) for i, n in enumerate(("R", "G", "B"))}


def describe_shape(arr: np.ndarray) -> str:
    if arr.ndim == 2:
        return f"{arr.shape[0]} baris × {arr.shape[1]} kolom"
    return f"{arr.shape[0]} (tinggi) × {arr.shape[1]} (lebar) × {arr.shape[2]} (channel)"


def to_csv(arr: np.ndarray) -> bytes:
    """Matriks gray/biner ke CSV. RGB: format panjang (y, x, R, G, B)."""
    if arr.ndim == 2:
        return pd.DataFrame(arr).to_csv(index=False, header=False).encode()
    h, w, _ = arr.shape
    flat = pd.DataFrame(arr.reshape(-1, 3), columns=["R", "G", "B"])
    flat.insert(0, "x", np.tile(np.arange(w), h))
    flat.insert(0, "y", np.repeat(np.arange(h), w))
    return flat.to_csv(index=False).encode()
