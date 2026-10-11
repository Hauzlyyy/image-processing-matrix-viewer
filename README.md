# Image Processing & Matrix Viewer

> **Project Tugas Mandiri Pengolahan Citra Digital**

## 1. Identitas Project

**Nama Project:** Image Processing & Matrix Viewer  
**Bahasa Pemrograman:** Python  
**Framework:** Streamlit  
**Jenis Aplikasi:** Aplikasi Pengolahan Citra Digital Berbasis Web Lokal

---

## 2. Deskripsi Project

**Image Processing & Matrix Viewer** adalah aplikasi sederhana untuk melakukan pengolahan dasar citra digital.

Aplikasi menerima input berupa file gambar dengan format:

- JPG
- JPEG
- PNG
- BMP

Setelah gambar dimasukkan, sistem akan membaca dan menampilkan informasi gambar, kemudian menghasilkan beberapa bentuk representasi citra, yaitu:

1. Citra asli
2. Citra biner
3. Grayscale 8-bit
4. Grayscale 16-bit
5. RGB 8-bit
6. RGB 16-bit
7. Representasi citra dalam bentuk matriks

Project ini dibuat untuk memenuhi kebutuhan tugas mandiri pengolahan citra digital, khususnya kemampuan untuk mengambil input gambar, mengubah representasi citra, mempertahankan resolusi sesuai input, serta merepresentasikan nilai piksel dalam bentuk matriks.

---

# 3. Latar Belakang

Citra digital merupakan representasi gambar dalam bentuk data numerik. Setiap gambar tersusun atas piksel yang memiliki nilai tertentu. Nilai tersebut dapat direpresentasikan dalam berbagai bentuk, seperti citra biner, grayscale, maupun RGB.

Dalam pembelajaran pengolahan citra digital, pemahaman terhadap representasi nilai piksel sangat penting. Oleh karena itu, diperlukan sebuah aplikasi sederhana yang dapat menunjukkan hubungan antara gambar yang terlihat secara visual dengan nilai numerik penyusunnya.

Aplikasi **Image Processing & Matrix Viewer** dibuat untuk mempermudah proses tersebut. Pengguna cukup memasukkan gambar, kemudian sistem akan menampilkan berbagai bentuk representasi citra beserta matriks nilai pikselnya.

---

# 4. Tujuan

Tujuan pembuatan aplikasi ini adalah:

1. Membuat program yang dapat menerima input gambar.
2. Mendukung format JPG, JPEG, PNG, dan BMP.
3. Menampilkan gambar asli sesuai resolusi input.
4. Menampilkan informasi dasar gambar.
5. Mengubah gambar menjadi citra biner.
6. Mengubah gambar menjadi grayscale 8-bit.
7. Mengubah gambar menjadi grayscale 16-bit.
8. Menampilkan gambar RGB 8-bit.
9. Menampilkan gambar RGB 16-bit.
10. Merepresentasikan citra dalam bentuk matriks.
11. Mempermudah pemahaman hubungan antara piksel dan nilai numerik.
12. Membuat aplikasi pengolahan citra yang sederhana dan mudah digunakan.

---

# 5. Ruang Lingkup

Project ini berfokus pada pengolahan citra dasar.

### Input

File gambar:

- `.jpg`
- `.jpeg`
- `.png`
- `.bmp`

### Proses

- Membaca gambar
- Membaca resolusi
- Membaca channel warna
- Konversi biner
- Konversi grayscale
- Konversi RGB
- Konversi bit depth
- Konversi ke bentuk matriks

### Output

- Gambar asli
- Citra biner
- Grayscale 8-bit
- Grayscale 16-bit
- RGB 8-bit
- RGB 16-bit
- Matriks nilai piksel
- Informasi gambar

---

# 6. Konsep Dasar Citra Digital

## 6.1 Piksel

Piksel merupakan elemen terkecil penyusun sebuah citra digital.

Setiap piksel mempunyai nilai tertentu. Pada citra grayscale, satu piksel biasanya memiliki satu nilai intensitas. Pada citra RGB, satu piksel memiliki tiga nilai, yaitu Red, Green, dan Blue.

---

## 6.2 Resolusi

Resolusi menunjukkan jumlah piksel yang menyusun gambar.

Sebagai contoh:

```text
800 × 600
```

berarti gambar mempunyai:

- Lebar = 800 piksel
- Tinggi = 600 piksel

Jumlah total piksel:

```text
800 × 600 = 480.000 piksel
```

---

## 6.3 Channel

Channel merupakan komponen penyusun informasi warna pada citra.

Contoh:

### Grayscale

Memiliki satu channel:

```text
Gray
```

### RGB

Memiliki tiga channel:

```text
R = Red
G = Green
B = Blue
```

---

# 7. Representasi Citra

## 7.1 Citra Biner

Citra biner merupakan citra yang hanya mempunyai dua kondisi utama, yaitu hitam dan putih.

Dalam representasi 8-bit:

```text
0   = Hitam
255 = Putih
```

Contoh:

```text
[
    [0,   0,   255, 255],
    [0,   255, 255, 0],
    [255, 255, 0,   0]
]
```

---

## 7.2 Grayscale 8-bit

Grayscale 8-bit mempunyai rentang nilai:

```text
0 - 255
```

Keterangan:

```text
0   = Hitam
255 = Putih
```

Contoh:

```text
[
    [0, 50, 100, 150],
    [30, 80, 130, 200],
    [60, 120, 180, 255]
]
```

---

## 7.3 Grayscale 16-bit

Grayscale 16-bit mempunyai rentang nilai:

```text
0 - 65535
```

Contoh:

```text
[
    [0, 10000, 30000],
    [5000, 25000, 45000],
    [10000, 40000, 65535]
]
```

Grayscale 16-bit memiliki jumlah tingkat intensitas yang lebih banyak dibandingkan grayscale 8-bit.

---

## 7.4 RGB 8-bit

RGB merupakan model warna yang terdiri dari tiga channel:

```text
R = Red
G = Green
B = Blue
```

Pada RGB 8-bit, masing-masing channel mempunyai rentang:

```text
0 - 255
```

Satu piksel dapat ditulis:

```text
(R, G, B)
```

Contoh:

```text
(255, 0, 0)
```

merupakan warna merah.

Contoh matriks RGB:

```text
[
    [(255,0,0), (0,255,0)],
    [(0,0,255), (255,255,255)]
]
```

---

## 7.5 RGB 16-bit

RGB 16-bit tetap mempunyai tiga channel:

```text
R
G
B
```

Namun masing-masing channel mempunyai rentang:

```text
0 - 65535
```

Contoh:

```text
(65535, 0, 0)
```

menunjukkan nilai merah maksimum pada channel Red.

---

# 8. Alur Sistem

Alur kerja aplikasi:

```text
                MULAI
                  |
                  v
          Upload File Gambar
                  |
                  v
           Validasi Format
                  |
                  v
            Baca Gambar
                  |
                  v
        Tampilkan Informasi
                  |
                  v
          Tampilkan Original
                  |
                  v
       +----------+----------+
       |          |          |
       v          v          v
    Biner     Grayscale     RGB
               8/16 bit    8/16 bit
       |          |          |
       +----------+----------+
                  |
                  v
        Representasi Matriks
                  |
                  v
              SELESAI
```

---

# 9. Rancangan Tampilan

Aplikasi menggunakan tampilan sederhana dengan beberapa bagian atau tab.

## 9.1 Halaman Utama

```text
====================================================
       IMAGE PROCESSING & MATRIX VIEWER
          Pengolahan Citra Digital
====================================================

Upload Gambar
[ Browse Files ]

Format yang didukung:
JPG / JPEG / PNG / BMP
```

---

## 9.2 Informasi Gambar

Setelah gambar berhasil diunggah:

```text
INFORMASI GAMBAR

Nama File   : gambar.jpg
Format      : JPEG
Lebar       : 800 px
Tinggi      : 600 px
Resolusi    : 800 × 600
Channel     : 3
Mode        : RGB
Bit Depth   : 8-bit
```

---

## 9.3 Gambar Asli

```text
GAMBAR ASLI

+--------------------------------------+
|                                      |
|             GAMBAR INPUT             |
|                                      |
+--------------------------------------+

Resolusi: 800 × 600
```

---

## 9.4 Citra Biner

```text
CITRA BINER

+--------------------------------------+
|                                      |
|          HASIL CITRA BINER           |
|                                      |
+--------------------------------------+

Nilai:
0   = Hitam
255 = Putih
```

Kemudian sistem menampilkan matriks biner.

---

## 9.5 Grayscale

```text
GRAYSCALE

[ Grayscale 8-bit ]

+--------------------------------------+
|                                      |
|          HASIL GRAYSCALE             |
|                                      |
+--------------------------------------+

Rentang: 0 - 255


[ Grayscale 16-bit ]

+--------------------------------------+
|                                      |
|          HASIL GRAYSCALE             |
|                                      |
+--------------------------------------+

Rentang: 0 - 65535
```

---

## 9.6 RGB

```text
RGB

[ RGB 8-bit ]

R = 0 - 255
G = 0 - 255
B = 0 - 255


[ RGB 16-bit ]

R = 0 - 65535
G = 0 - 65535
B = 0 - 65535
```

---

# 10. Representasi Matriks

Matriks merupakan salah satu output utama aplikasi.

## 10.1 Matriks Grayscale

Contoh:

```text
[
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
]
```

Ukuran matriks mengikuti resolusi gambar.

Jika gambar memiliki resolusi:

```text
800 × 600
```

maka matriks grayscale secara konseptual mempunyai:

```text
600 baris × 800 kolom
```

---

## 10.2 Matriks RGB

Pada RGB, setiap piksel mempunyai tiga nilai.

Contoh:

```text
[
    [(255,0,0), (0,255,0)],
    [(0,0,255), (255,255,255)]
]
```

Bentuk konseptualnya:

```text
Tinggi × Lebar × 3
```

---

# 11. Tampilan Matriks

Gambar dengan resolusi besar akan menghasilkan matriks yang sangat besar.

Contoh:

```text
1920 × 1080
```

Jika seluruh matriks ditampilkan sekaligus, tampilan akan terlalu panjang dan sulit dibaca.

Oleh karena itu, aplikasi menyediakan pilihan:

```text
Tampilkan Matriks

( ) 10 × 10 pertama
( ) 20 × 20 pertama
( ) 50 × 50 pertama
( ) Matriks lengkap
```

Default:

```text
20 × 20 pertama
```

Tujuannya agar aplikasi tetap ringan dan matriks mudah diperiksa.

---

# 12. Struktur Folder Project

Struktur project dibuat terpisah berdasarkan fungsi.

```text
image-processing-viewer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── __init__.py
│   ├── image_loader.py
│   ├── image_processor.py
│   ├── matrix_converter.py
│   └── image_info.py
│
├── components/
│   ├── __init__.py
│   ├── uploader.py
│   ├── display.py
│   └── matrix_view.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
└── assets/
    └── contoh/
        ├── gambar1.jpg
        ├── gambar2.png
        └── gambar3.bmp
```

---

# 13. Penjelasan Struktur Folder

## `app.py`

Merupakan file utama aplikasi.

Tugasnya:

- Menjalankan aplikasi.
- Mengatur halaman.
- Menghubungkan berbagai modul.
- Menampilkan komponen aplikasi.

---

## `modules/`

Folder untuk proses utama pengolahan citra.

### `image_loader.py`

Bertugas:

- Membaca file gambar.
- Memastikan file dapat diproses.
- Menyiapkan gambar untuk proses berikutnya.

### `image_processor.py`

Bertugas melakukan:

- Konversi biner.
- Grayscale 8-bit.
- Grayscale 16-bit.
- RGB 8-bit.
- RGB 16-bit.

### `matrix_converter.py`

Bertugas:

- Mengubah citra menjadi array/matriks.
- Mengambil sebagian matriks.
- Menyiapkan matriks untuk ditampilkan.

### `image_info.py`

Bertugas membaca:

- Nama file.
- Format.
- Lebar.
- Tinggi.
- Resolusi.
- Channel.
- Mode warna.
- Bit depth.

---

# 14. Folder `components/`

Folder ini digunakan untuk bagian tampilan aplikasi.

### `uploader.py`

Mengatur tampilan upload file.

### `display.py`

Mengatur tampilan gambar.

### `matrix_view.py`

Mengatur tampilan matriks.

---

# 15. Folder `utils/`

Berisi fungsi pendukung yang digunakan oleh beberapa bagian aplikasi.

### `helpers.py`

Berisi fungsi-fungsi sederhana yang membantu aplikasi tetap rapi dan tidak mengulang kode yang sama.

---

# 16. Folder `assets/`

Digunakan untuk menyimpan gambar contoh yang digunakan dalam pengujian.

Contoh:

```text
assets/
└── contoh/
    ├── gambar1.jpg
    ├── gambar2.png
    └── gambar3.bmp
```

---

# 17. Library yang Digunakan

Library yang diperlukan:

```text
streamlit
numpy
pillow
opencv-python
matplotlib
pandas
```

Daftar library disimpan pada:

```text
requirements.txt
```

---

# 18. Fitur Sistem

## Fitur Input

- Upload JPG.
- Upload JPEG.
- Upload PNG.
- Upload BMP.

## Fitur Informasi

- Nama file.
- Format file.
- Resolusi.
- Lebar.
- Tinggi.
- Channel.
- Mode warna.
- Bit depth.

## Fitur Pengolahan

- Biner.
- Grayscale 8-bit.
- Grayscale 16-bit.
- RGB 8-bit.
- RGB 16-bit.

## Fitur Representasi

- Matriks biner.
- Matriks grayscale.
- Matriks RGB.
- Pemilihan ukuran matriks yang ditampilkan.

---

# 19. Persyaratan Tugas

Berdasarkan tugas mandiri, aplikasi dirancang untuk memenuhi poin berikut:

| No | Persyaratan | Implementasi |
|---:|---|---|
| 1 | Input gambar | Upload file |
| 2 | BMP | Didukung |
| 3 | JPG | Didukung |
| 4 | PNG | Didukung |
| 5 | Citra biner | Tersedia |
| 6 | Grayscale 8-bit | Tersedia |
| 7 | Grayscale 16-bit | Tersedia |
| 8 | RGB 8-bit | Tersedia |
| 9 | RGB 16-bit | Tersedia |
| 10 | Resolusi sesuai input | Ditampilkan |
| 11 | Representasi matriks | Tersedia |

---

# 20. Pengujian

Pengujian dilakukan menggunakan beberapa jenis file.

## 20.1 Pengujian Format

| No | File | Hasil yang Diharapkan |
|---:|---|---|
| 1 | gambar.jpg | Berhasil dibaca |
| 2 | gambar.jpeg | Berhasil dibaca |
| 3 | gambar.png | Berhasil dibaca |
| 4 | gambar.bmp | Berhasil dibaca |

---

## 20.2 Pengujian Resolusi

Digunakan beberapa ukuran gambar:

| No | Resolusi | Hasil |
|---:|---|---|
| 1 | 100 × 100 | Sesuai |
| 2 | 640 × 480 | Sesuai |
| 3 | 800 × 600 | Sesuai |
| 4 | 1920 × 1080 | Sesuai |

---

## 20.3 Pengujian Representasi

Setiap gambar diuji untuk:

- Biner.
- Grayscale 8-bit.
- Grayscale 16-bit.
- RGB 8-bit.
- RGB 16-bit.
- Matriks.

---

# 21. Skenario Penggunaan

### Langkah 1

Pengguna membuka aplikasi.

### Langkah 2

Pengguna memilih file gambar.

### Langkah 3

Sistem melakukan validasi format.

### Langkah 4

Sistem membaca gambar.

### Langkah 5

Sistem menampilkan informasi gambar.

### Langkah 6

Sistem menampilkan gambar asli.

### Langkah 7

Sistem melakukan konversi citra.

### Langkah 8

Pengguna melihat hasil biner, grayscale, dan RGB.

### Langkah 9

Pengguna memilih representasi matriks.

### Langkah 10

Sistem menampilkan nilai piksel dalam bentuk matriks.

---

# 22. Penanganan Error

Aplikasi perlu memberikan pesan apabila:

### File tidak dipilih

```text
Silakan pilih gambar terlebih dahulu.
```

### Format tidak didukung

```text
Format file tidak didukung.
Gunakan JPG, JPEG, PNG, atau BMP.
```

### File gagal dibaca

```text
Gambar tidak dapat diproses.
Silakan gunakan file gambar lain.
```

### Gambar terlalu besar

Sistem dapat memberikan informasi bahwa proses matriks penuh membutuhkan sumber daya lebih besar dan menyarankan penggunaan tampilan matriks sebagian.

---

# 23. Prinsip Tampilan

Tampilan aplikasi dibuat:

- Sederhana.
- Bersih.
- Mudah digunakan.
- Tidak terlalu banyak tombol.
- Informasi dikelompokkan berdasarkan fungsi.
- Matriks ditampilkan dalam bentuk tabel.
- Gambar ditampilkan dengan ukuran yang mudah dilihat.

---

# 24. Rancangan Navigasi

```text
HOME
 │
 ├── Upload Gambar
 │
 ├── Informasi
 │
 ├── Original
 │
 ├── Biner
 │
 ├── Grayscale
 │    ├── 8-bit
 │    └── 16-bit
 │
 ├── RGB
 │    ├── 8-bit
 │    └── 16-bit
 │
 └── Matriks
      ├── Biner
      ├── Grayscale
      └── RGB
```

---

# 25. Tahapan Pengerjaan

## Tahap 1 - Persiapan

Membuat folder project dan virtual environment.

## Tahap 2 - Instalasi Library

Menyiapkan library yang diperlukan.

## Tahap 3 - Input

Membuat fitur upload gambar.

## Tahap 4 - Informasi

Menampilkan informasi gambar.

## Tahap 5 - Biner

Membuat konversi citra biner.

## Tahap 6 - Grayscale

Membuat grayscale 8-bit dan 16-bit.

## Tahap 7 - RGB

Membuat RGB 8-bit dan 16-bit.

## Tahap 8 - Matriks

Mengubah citra menjadi matriks.

## Tahap 9 - Interface

Merapikan tampilan aplikasi.

## Tahap 10 - Testing

Menguji seluruh fitur menggunakan beberapa gambar.

---

# 26. Target Output

Setelah aplikasi selesai, tampilan akhir diharapkan mempunyai struktur seperti berikut:

```text
====================================================
          IMAGE PROCESSING & MATRIX VIEWER
====================================================

[ Upload Gambar ]

----------------------------------------------------
INFORMASI GAMBAR
----------------------------------------------------
Nama File     : gambar.jpg
Format        : JPEG
Resolusi      : 800 × 600
Channel       : RGB
Bit Depth     : 8-bit

----------------------------------------------------
ORIGINAL
----------------------------------------------------
             [ GAMBAR ]

----------------------------------------------------
BINARY
----------------------------------------------------
             [ GAMBAR BINER ]

Matriks:
[ 0 0 255 255 ... ]

----------------------------------------------------
GRAYSCALE
----------------------------------------------------
8-bit:
             [ GAMBAR ]

16-bit:
             [ GAMBAR ]

Matriks:
[ 20 40 60 ... ]

----------------------------------------------------
RGB
----------------------------------------------------
8-bit:
             [ GAMBAR ]

16-bit:
             [ GAMBAR ]

Matriks:
[(R,G,B) (R,G,B) ...]

====================================================
```

---

# 27. Kelebihan Sistem

Beberapa kelebihan sistem:

1. Mudah digunakan.
2. Tidak membutuhkan database.
3. Tidak membutuhkan koneksi internet setelah environment tersedia.
4. Mendukung beberapa format gambar.
5. Menampilkan gambar secara visual.
6. Menampilkan nilai piksel secara numerik.
7. Mempermudah pemahaman konsep citra digital.
8. Struktur kode dipisahkan berdasarkan fungsi.
9. Mudah dikembangkan untuk fitur tambahan.

---

# 28. Pengembangan Selanjutnya

Apabila diperlukan, aplikasi dapat dikembangkan dengan fitur:

- Histogram citra.
- Thresholding.
- Edge detection.
- Rotasi gambar.
- Resize gambar.
- Crop gambar.
- Konversi HSV.
- Konversi CMYK.
- Operasi aritmatika citra.
- Penyimpanan hasil pengolahan.
- Download matriks dalam format CSV.
- Download hasil gambar.

Fitur tersebut tidak menjadi fokus utama project awal agar sistem tetap sederhana dan sesuai dengan tugas.

---

# 29. Kesimpulan

**Image Processing & Matrix Viewer** merupakan aplikasi sederhana untuk membantu proses pembelajaran pengolahan citra digital.

Aplikasi menerima input berupa gambar JPG, JPEG, PNG, atau BMP. Gambar kemudian diproses menjadi beberapa bentuk representasi, yaitu biner, grayscale 8-bit, grayscale 16-bit, RGB 8-bit, dan RGB 16-bit.

Selain menampilkan hasil secara visual, aplikasi juga menampilkan nilai piksel dalam bentuk matriks. Dengan demikian, pengguna dapat melihat hubungan antara gambar secara visual dengan representasi numeriknya.

Struktur project dibuat modular agar setiap fungsi memiliki file tersendiri. Hal ini membuat project lebih rapi, mudah dipahami, mudah diuji, dan mudah dikembangkan.

---

# 30. Status Project

| Komponen | Status |
|---|---|
| Rancangan sistem | Selesai |
| Struktur folder | Selesai |
| Dokumentasi | Selesai |
| Upload gambar | Akan dibuat |
| Informasi gambar | Akan dibuat |
| Citra biner | Akan dibuat |
| Grayscale 8-bit | Akan dibuat |
| Grayscale 16-bit | Akan dibuat |
| RGB 8-bit | Akan dibuat |
| RGB 16-bit | Akan dibuat |
| Matriks | Akan dibuat |
| Testing | Akan dibuat |

---

## Catatan

Project ini sengaja dirancang dengan konsep sederhana dan modular agar dapat dikerjakan secara bertahap. **Kode program belum termasuk dalam dokumentasi ini.**

Urutan implementasi yang disarankan:

```text
requirements.txt
       ↓
image_loader.py
       ↓
image_info.py
       ↓
image_processor.py
       ↓
matrix_converter.py
       ↓
components/
       ↓
app.py
       ↓
Testing
```

---

# 31. Cara Menjalankan

```bash
pip install -r requirements.txt
streamlit run app.py
```

Buka `http://localhost:8501`, lalu upload gambar (contoh tersedia di `assets/contoh/`).

**Status implementasi:** seluruh fitur pada tabel Status Project (bagian 30) sudah dibuat dan diuji.
