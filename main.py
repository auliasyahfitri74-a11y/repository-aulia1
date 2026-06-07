DISKON_LEVEL_1 = 0.15
DISKON_LEVEL_2 = 0.10
TARIF_PPN = 0.11

BATAS_MIN_DISKON_1 = 200000
BATAS_MIN_DISKON_2 = 100000

print("=== SISTEM KASIR TOKO ===")
nama_barang = input("Masukkan nama barang: ")
harga_barang = float(input("Masukkan harga barang: "))
jumlah_beli = int(input("Masukkan jumlah beli: "))

total_awal = harga_barang * jumlah_beli
jumlah_diskon = 0

if total_awal > BATAS_MIN_DISKON_1:
    jumlah_diskon = total_awal * DISKON_LEVEL_1
elif total_awal > BATAS_MIN_DISKON_2:
    jumlah_diskon = total_awal * DISKON_LEVEL_2

total_setelah_diskon = total_awal - jumlah_diskon
jumlah_ppn = total_setelah_diskon * TARIF_PPN
total_akhir_bayar = total_setelah_diskon + jumlah_ppn

print("\n--- STRUK BELANJA ---")
print(f"Barang      : {nama_barang}")
print(f"Total Awal  : Rp{total_awal}")
print(f"Diskon      : Rp{jumlah_diskon}")
print(f"PPN (11%)   : Rp{jumlah_ppn}")
print(f"Total Bayar : Rp{total_akhir_bayar}")