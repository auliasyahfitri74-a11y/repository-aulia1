print("=== SISTEM KASIR TOKO ===")
n = input("Masukkan nama barang: ")
h = float(input("Masukkan harga barang: "))
j = int(input("Masukkan jumlah beli: "))

t = h * j
d = 0

if t > 200000:
    d = t * 0.15  
elif t > 100000:
    d = t * 0.10  

tot = t - d
pjk = tot * 0.11  
akhir = tot + pjk

print("\n--- STRUK BELANJA ---")
print("Barang:", n)
print("Total Awal: Rp", t)
print("Diskon: Rp", d)
print("PPN: Rp", pjk)
print("Total Bayar: Rp", akhir)