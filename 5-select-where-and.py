import sqlite3
#select all data fauna
koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()

#mengambil semua data dalam tabel dan ditampilkan
kursor.execute("SELECT *FROM fauna WHERE jenis = 'Mamalia' AND asal = 'Sulawesi' ")

#tampilkan data dalam bentuk baris
baris_tabel = kursor.fetchall()

# membuat format table dengan method format()
print("TABEL FAUNA")
print("="*120)
print("{:<5} {:<20} {:<20} {:<15} {:<20}{:<20}".format("ID", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI","TAHUN TERAKHIR DITEMUKAN"))
print("-"*120)

# tampilkan data sesuai format tabel dengan perulangan
for baris in baris_tabel:
    print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

koneksi.close