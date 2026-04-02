# Praktikum Kecerdasan Buatan - Pertemuan 3

Proyek ini merupakan bagian dari praktikum Kecerdasan Buatan (Artificial Intelligence) untuk pertemuan ke-3. Proyek ini menunjukkan implementasi sistem kontrol fuzzy menggunakan pustaka scikit-fuzzy di Python untuk menyelesaikan dua studi kasus.

## Deskripsi

Dalam pertemuan ini, kita belajar tentang logika fuzzy dan aplikasinya dalam pengambilan keputusan. Dua studi kasus yang diimplementasikan adalah:

1. **Studi Kasus 1 (StudiKasus1.py)**: Sistem kontrol fuzzy untuk menentukan jumlah stok makanan hewan yang optimal berdasarkan variabel seperti jumlah barang terjual, permintaan, harga item, dan profit.

2. **Studi Kasus 2 (StudiKasus2.py)**: Sistem kontrol fuzzy untuk mengukur tingkat kepuasan pelanggan dalam layanan publik berdasarkan informasi, persyaratan, petugas, dan sarana prasarana.

## Persyaratan

- Python 3.x
- numpy
- scikit-fuzzy
- matplotlib

Untuk menginstal dependensi, jalankan:

```
pip install numpy scikit-fuzzy matplotlib
```

## Cara Menjalankan

1. Pastikan semua dependensi telah terinstal.
2. Jalankan file Python menggunakan interpreter Python:

   ```
   python StudiKasus1.py
   python StudiKasus2.py
   ```

3. Output akan ditampilkan di konsol, menunjukkan hasil perhitungan fuzzy.

## Troubleshooting

- Jika terjadi error saat menjalankan (misalnya exit code 1), pastikan semua pustaka telah terinstal dengan benar.
- Jika ada masalah dengan matplotlib, pastikan backend plotting dikonfigurasi dengan benar (misalnya, gunakan `plt.show()` jika diperlukan untuk visualisasi).

## Struktur Proyek

- `StudiKasus1.py`: Implementasi fuzzy logic untuk stok makanan hewan.
- `StudiKasus2.py`: Implementasi fuzzy logic untuk kepuasan pelanggan.
