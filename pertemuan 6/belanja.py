product = {
    "beras": 18000,
    "gula": 12500,
    "telur": 35000,
    "susu": 19000,
}

def belanja():
    print("Selamat datang, Selamat berbelanja")
    print("Berikut adalah daftar barang yang tersedia:")
    for barang, harga in product.item():
       print(f"{barang}: Rp{harga} per kg")

       total_belanja = 0
       while True:
         barang_dipilih = input = ("masukan nama barang yang ingin anda beli(atau 'selesai' untuk selesai)")
         if barang_dipilih.lower() == 'selesai':
            break
         if barang_dipilih not in product:
            print("maaf, barang tidak tersedia")
            continue
         jumlah = float(input(f"berapa kg {barang_dipilih} yang anda inginkan?"))
         total_belanja += product[barang_dipilih] * jumlah
         print(f"total belanja anda adalah: Rp{total_belanja}")

belanja()         