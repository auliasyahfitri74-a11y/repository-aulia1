DISKON_LEVEL_1 = 0.15          
DISKON_LEVEL_2 = 0.10          
TARIF_PPN = 0.11               

BATAS_MINIMAL_DISKON_1 = 200000
BATAS_MINIMAL_DISKON_2 = 100000

def hitung_diskon(total_awal):
    """Fungsi khusus untuk menghitung potongan harga (diskon)"""
    if total_awal > BATAS_MINIMAL_DISKON_1:
        return total_awal * DISKON_LEVEL_1
    elif total_awal > BATAS_MINIMAL_DISKON_2:
        return total_awal * DISKON_LEVEL_2
    return 0


def hitung_ppn(total_setelah_diskon):
    """Fungsi khusus untuk menghitung pajak PPN"""
    return total_setelah_diskon * TARIF_PPN


def tampilkan_struk(nama_barang, total_awal, jumlah_diskon, jumlah_ppn, total_akhir):
    """Fungsi khusus untuk mencetak output struk belanja"""
    print("\n--- STRUK BELANJA ---")
    print(f"Barang      : {nama_barang}")
    print(f"Total Awal  : Rp{total_awal:,.2f}")
    print(f"Diskon      : Rp{jumlah_diskon:,.2f}")
    print(f"PPN (11%)   : Rp{jumlah_ppn:,.2f}")
    print(f"Total Bayar : Rp{total_akhir:,.2f}")


def main():
    """Fungsi utama untuk mengatur alur program (Flow Control)"""
    print("=== SISTEM KASIR TOKO ===")
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = float(input("Masukkan harga barang: "))
    jumlah_beli = int(input("Masukkan jumlah beli: "))
    
    # Proses Kalkulasi Menggunakan Fungsi Hasil Refactoring
    total_awal = harga_barang * jumlah_beli
    jumlah_diskon = hitung_diskon(total_awal)
    total_setelah_diskon = total_awal - jumlah_diskon
    jumlah_ppn = hitung_ppn(total_setelah_diskon)
    total_akhir_bayar = total_setelah_diskon + jumlah_ppn
    
    # Mencetak Hasil
    tampilkan_struk(nama_barang, total_awal, jumlah_diskon, jumlah_ppn, total_akhir_bayar)


# Memastikan program berjalan dari fungsi utama
if __name__ == "__main__":
    main()