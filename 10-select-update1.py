import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

# ubah berdasarkan id_fauna
id_fauna = 10
jmlh_baru = 650

# mgunakan QUERY UPDATE
kursor.execute(f"UPDATE fauna SET jml_skrng  = {jmlh_baru} WHERE id = {id_fauna}")
koneksi.commit()

#cek apakah data berhasil diubah atau belum
if kursor.rowcount > 0: #cek berdasarkan adanya baris atau tidak
    print(f"Data dengan ID {id_fauna} Berhasil diubah!!")
else:
    print(f"Tidak ada data fauna dengan ID {id_fauna}!")

kursor.execute("SELECT *FROM fauna")

baris_tabel = kursor.fetchall()

print("TABEL FAUNA")
print("="*120)
print("{:<5} {:<20} {:<20} {:<15} {:<20}{:<20}".format("ID", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI","TAHUN TERAKHIR DITEMUKAN"))
print("-"*120)

# tampilkan data sesuai format tabel dengan perulangan
for baris in baris_tabel:
    print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

# putuskan koneksi  
koneksi.close