# Tes Junior Programmer - Fastprint
Project ini dibuat untuk memenuhi Tes Junior Programmer Fastprint.

Aplikasi berbasis Django yang berfungsi untuk:
- Mengambil data produk dari API yang disediakan
- Menyimpan data ke dalam database relasional
- Menampilkan data produk
- Menyediakan fitur CRUD (Create, Read, Update, Delete)
- Melakukan filter produk berdasarkan status "bisa dijual"

## Tech Stack
- Python 3
- Django
- Django Rest Framework
- MySQL / PostgreSQL
- HTML (Django Template)
- Git & GitHub

## Struktur Database

Terdapat 3 tabel utama:

### Tabel Produk
- id_produk
- nama_produk
- harga
- kategori_id (Foreign Key)
- status_id (Foreign Key)

### Tabel Kategori
- id_kategori
- nama_kategori

### Tabel Status
- id_status
- nama_status

## Tahapan Pengerjaan
1. Melakukan analisis API menggunakan Postman:
- Mengirim request ke endpoint API
- Menggunakan Basic Authentication sesuai ketentuan
- Memeriksa response JSON
- Memeriksa header dan cookies sesuai hint soal

2. Membuat project Django dan app produk, kemudian melakukan konfigurasi:
- Menambahkan Django Rest Framework
- Mengatur koneksi database
- Membuat struktur folder yang rapi

3. Membuat model Kategori, Status, dan Produk sesuai dengan struktur tabel pada soal:
Relasi antar tabel dibuat menggunakan Foreign Key untuk menjaga normalisasi data.

4. Membuat service untuk mengambil data produk dari API dan menyimpannya ke database:
- Mengambil data dari API menggunakan library requests
- Mengecek dan membuat data kategori dan status jika belum ada
- Menyimpan data produk menggunakan update_or_create agar tidak terjadi duplikasi

5. Menampilkan seluruh data produk yang telah disimpan ke dalam database menggunakan Django Template dalam bentuk tabel.

6. Membuat halaman khusus untuk menampilkan produk yang memiliki status "bisa dijual".

7. Membuat fitur:
- Tambah produk
- Edit produk
- Hapus produk

8. Untuk fitur tambah dan edit, digunakan validasi form menggunakan menggunakan Django Form (server-side validation):
- Nama produk wajib diisi
- Harga harus berupa angka dan lebih dari 0

9. Pada fitur hapus, ditambahkan alert konfirmasi (confirm) untuk memastikan pengguna tidak menghapus data secara tidak sengaja.

## Cara Menjalankan Aplikasi
1. Clone repository
   git clone https://github.com/username/tes-junior-programmer-fastprint.git

2. Masuk ke folder project
   cd tes-junior-programmer-fastprint

3. Install dependency
   pip install -r requirements.txt

4. Migrasi database
   python manage.py migrate

5. Jalankan server
   python manage.py runserver

## Pengambilan Data API

Data produk diambil dari API menggunakan service Django.

Endpoint API:
https://recruitment.fastprint.co.id/tes/api_tes_programmer

Proses pengambilan data:
- Menggunakan Basic Authentication
- Data diambil dan langsung disimpan ke database

Project ini dibuat sesuai dengan instruksi Tes Junior Programmer Fastprint.
Terima kasih atas kesempatan yang diberikan.
