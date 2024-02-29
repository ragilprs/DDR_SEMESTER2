product = {
   "caffe americano": 37.000,
    "caramel machiato": 59.000,
    "asian dolce latte": 55.000,
    "caramel latte": 52.000,
    "vanilla latte": 52.000,
    "caffe latte": 48.000,
    "cappuccino": 48.000,
    "caffe mocha": 55.000,
}

def belanja():
    print("Selamat datang di Rini")
    print("Berikut adalah daftar barang yang tersedia:")
    for barang, harga in product.items():
        print(f"{barang}: Rp{harga} per cup") 
        
    total_belanja = 0
    while True:
        barang_dipilih = input("Masukkan nama barang yang ingin anda beli(atau 'selesai' untuk selesai)").lower()
        if barang_dipilih.lower() == 'selesai':
             break
        if barang_dipilih not in product:
            print("Maaf, barang tersebut tidak tersedia")
            continue
        jumlah = float(input(f"Berapa cup {barang_dipilih} yang anda inginkan?"))
        total_belanja += product[barang_dipilih] * jumlah
    print(f"total Belanja anda adalah: Rp{total_belanja}")

    if total_belanja > 350000:\
    diskon = total_belanja * 0.15
    print("Diskon anda kali ini adalah",diskon)
    total_belanja -= diskon
    pajak = total_belanja *0.1
    print('pajak dari pesanan anda kali ini adalah, pajak')
    print('total yang harus di bayar adalah', total_belanja+pajak, 'terimakasih telah berebelanja di caffe Rini')

belanja()       