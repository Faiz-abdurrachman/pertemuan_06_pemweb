from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

# Kunci rahasia untuk session dan flash message
app.secret_key = 'kunci-rahasia-kantin-p06'

# Data menu kantin kampus sederhana untuk tampilan beranda
menu_list = [
    {
        'id': 1,
        'nama': 'Nasi Goreng Spesial',
        'harga': 'Rp 15.000',
        'kategori': 'Makanan',
        'deskripsi': 'Nasi goreng dengan bumbu rempah pilihan, telur mata sapi, dan kerupuk renyah.'
    },
    {
        'id': 2,
        'nama': 'Mie Ayam Bakso',
        'harga': 'Rp 13.000',
        'kategori': 'Makanan',
        'deskripsi': 'Mie kenyal gurih disajikan dengan suwiran ayam manis dan 2 butir bakso sapi.'
    },
    {
        'id': 3,
        'nama': 'Es Teh Manis Jumbo',
        'harga': 'Rp 5.000',
        'kategori': 'Minuman',
        'deskripsi': 'Teh melati segar disajikan dingin manis penyejuk dahaga saat istirahat kuliah.'
    }
]

@app.route('/')
def home():
    return render_template('index.html', menu_list=menu_list)


# ====================================================================
# LIVE CODING PRAKTIKUM PERTEMUAN 06:
# Route /register dengan method GET dan POST serta validasi 4 aturan
# ====================================================================
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Jika request POST: Pengguna mengirim data formulir
    if request.method == 'POST':
        # 1. Menangkap data dari form dan sanitasi spasi kosong berlebih
        nama = request.form.get('nama', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        confirm = request.form.get('confirm', '').strip()

        # 2. Wadah penampung pesan kesalahan validasi
        errors = []

        # ATURAN 1: Validasi Nama (Wajib diisi & minimal 3 karakter)
        if not nama:
            errors.append('Nama lengkap wajib diisi!')
        elif len(nama) < 3:
            errors.append('Nama lengkap terlalu pendek, minimal 3 karakter!')

        # ATURAN 2: Validasi Email (Wajib diisi, mengandung '@' dan domain '.')
        if not email:
            errors.append('Alamat email wajib diisi!')
        elif '@' not in email or '.' not in email:
            errors.append('Format email tidak valid (harus mengandung "@" dan domain "." misalnya budi@mail.com)!')

        # ATURAN 3: Validasi Password (Wajib diisi & minimal 6 karakter)
        if not password:
            errors.append('Kata sandi (password) wajib diisi!')
        elif len(password) < 6:
            errors.append('Kata sandi terlalu pendek, minimal 6 karakter demi keamanan!')

        # ATURAN 4: Validasi Konfirmasi Password (Harus sama persis dengan password)
        if password != confirm:
            errors.append('Konfirmasi kata sandi tidak cocok dengan kata sandi yang dimasukkan!')

        # 3. Evaluasi Hasil Validasi
        if errors:
            # Jika ada error: kirim flash message kategori 'danger' lalu render ulang form
            for error in errors:
                flash(error, 'danger')
            return render_template('register.html')

        # Jika lolos semua validasi: kirim pesan sukses dan redirect ke beranda (pola PRG)
        flash(f'Selamat datang, {nama}! Pendaftaran member kantin berhasil. Anda berhak mendapatkan diskon 15%!', 'success')
        return redirect(url_for('home'))

    # Jika request GET: Tampilkan formulir registrasi kosongan
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
