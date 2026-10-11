import streamlit as st
from modules.matrix_converter import (crop_matrix, to_dataframe,
                                      to_channel_dataframes, describe_shape, to_csv)
from utils.helpers import (MATRIX_OPTIONS, DEFAULT_MATRIX,
                           value_range, full_matrix_too_big)


def show_matrix(arr, title: str, key: str, csv_name: str):
    st.markdown(f"#### Matriks {title}")
    st.write(f"Ukuran penuh: **{describe_shape(arr)}** · {value_range(arr)} · tipe `{arr.dtype}`")

    labels = list(MATRIX_OPTIONS.keys())
    choice = st.radio("Tampilkan matriks", labels,
                      index=labels.index(DEFAULT_MATRIX),
                      horizontal=True, key=f"radio_{key}")
    size = MATRIX_OPTIONS[choice]

    if size is None and full_matrix_too_big(arr):
        st.warning("Gambar besar: matriks lengkap membutuhkan sumber daya lebih besar. "
                   "Gunakan tampilan matriks sebagian atau download CSV.")
        st.download_button("Download matriks lengkap (CSV)", to_csv(arr),
                           file_name=csv_name, mime="text/csv", key=f"csv_{key}")
        return

    part = crop_matrix(arr, size)
    if arr.ndim == 3:
        view = st.radio("Bentuk", ["Gabungan (R,G,B)", "Per channel"],
                        horizontal=True, key=f"view_{key}")
        if view == "Per channel":
            tabs = st.tabs(["R", "G", "B"])
            for tab, (_, df) in zip(tabs, to_channel_dataframes(part).items()):
                tab.dataframe(df, use_container_width=True)
        else:
            st.dataframe(to_dataframe(part), use_container_width=True)
    else:
        st.dataframe(to_dataframe(part), use_container_width=True)

    st.download_button("Download matriks lengkap (CSV)", to_csv(arr),
                       file_name=csv_name, mime="text/csv", key=f"csv_{key}")
