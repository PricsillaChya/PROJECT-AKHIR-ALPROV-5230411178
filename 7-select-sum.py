import sqlite3
#select all data fauna
koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()

#mengambil semua data dalam tabel dan ditampilkan
kursor.execute("SELECT SUM(jml_skrng) FROM fauna")

jumlah_pplasi = kursor.fetchone()[0] # ambil data gaji jadikan baris baru dimulai dari indeks 0

print(f"Total seluruh populasi sekarang: {jumlah_pplasi}")


koneksi.close