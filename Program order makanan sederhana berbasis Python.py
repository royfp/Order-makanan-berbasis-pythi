total = 0
barang = []
harga = []

while True :
    print("""Daftar Menu\n
1. Roti bakar \t         10000
2. Indomie \t             7000
3. Indomie Telor \t     10000
4. Kentang Goreng \t     10000
5. Otak-otak \t         10000
6. Good Day \t         7000
7. Pelet gus samsudin \t 100
8. Tutor jadi dukun \t 100000000
""")

    kode = int(input("masukan kode menu :"))
    if kode == 1:
        barang.append("Roti bakar")
        harga.append(10000)
        total += 10000
    elif kode == 2:
        barang.append("Indomie")
        harga.append(7000)
        total += 7000
    elif kode == 3:
        barang.append("Indomie telor")
        harga.append(10000)
        total += 10000
    elif kode == 4:
        barang.append("kentang goreng")
        harga.append(10000)
        total += 10000
    elif kode == 5:
        barang.append("Otak-otak")
        harga.append(10000)
        total += 10000
    elif kode == 6:
        barang.append("Good Day")
        harga.append(7000)
        total += 7000
    elif kode == 7:
        barang.append("Pelet Gus samsusdin")
        harga.append(100)
        total += 100
    elif kode == 8:
        barang.append("Tutor jadi dukun")
        harga.append(100000000)
        total += 100000000
    else:
        print("Kode tidak ditemukan")

    lanjut = input("Lanjut pilih menu? (y/t) :")
    if lanjut == "t" :
        print("Terimakasih.Pesanan anda akan segera kami proses")
        break

print("Menu yang dipilih : ", barang)
print("Harga menu", harga )
print("Total Pesanan anda ", total, '\n')

uang = int(input("jumlah uang = "))
if uang > total :
    print("Kembalian =", uang - total)
elif uang == total :
    print(" ")
else:
     print("Uang Kurang", uang - total )