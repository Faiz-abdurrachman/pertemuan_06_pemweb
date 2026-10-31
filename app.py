from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

# Kunci rahasia untuk mengamankan session dan flash message
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
# LIVE CODING PRAKTIKUM PERTEMUAN 06
# Langkah 1 & 3: Buat route /register untuk menangani form registrasi member
# ====================================================================
# TULIS KODINGAN ROUTE /register DI SINI SAAT LIVE CODING
# ====================================================================


if __name__ == '__main__':
    app.run(debug=True)
