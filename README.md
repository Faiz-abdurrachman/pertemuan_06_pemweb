# Starter Kit Praktikum Pemrograman Web - Pertemuan 06
## Form Handling, Sanitasi Data, dan Validasi Sisi Server (Flask)

Selamat datang di repositori Starter Kit Praktikum Pertemuan 06!
Repositori ini adalah titik awal untuk sesi live coding di kelas praktikum.

---

## Cara Menjalankan Project

### 1. Clone Repositori Ini
```bash
git clone https://github.com/Faiz-abdurrachman/pertemuan_06_pemweb.git
cd pertemuan_06_pemweb
```

### 2. Pastikan Flask Sudah Terpasang
```bash
pip install flask
```

### 3. Jalankan Aplikasi
```bash
python app.py
```
Buka browser dan akses alamat: `http://127.0.0.1:5000`

---

## Struktur Folder Project

```
pertemuan_06_pemweb/
├── app.py                      # Backend Flask utama
├── static/
│   └── css/
│       └── style.css           # Styling tampilan modern
├── templates/
│   ├── base.html               # Layout induk + wadah notifikasi flash
│   ├── index.html              # Halaman beranda daftar menu
│   └── register.html           # (Dibuat saat live coding) Form registrasi
└── README.md
```

---

## Target Pembelajaran Pertemuan 06
1. Memahami perbedaan validasi client-side (HTML5) vs validasi sisi server (Python).
2. Menangkap input formulir secara aman dengan `request.form.get()` dan sanitasi `.strip()`.
3. Menerapkan 4 aturan validasi server-side:
   - Nama minimal 3 karakter.
   - Format email valid (mengandung `@` dan domain `.`).
   - Password minimal 6 karakter.
   - Konfirmasi password harus cocok.
4. Menampilkan notifikasi error/sukses dengan kategori Flash Messages (`danger` vs `success`).
5. Menerapkan fitur *Sticky Form* agar input pengguna tidak terhapus saat terjadi kesalahan.
