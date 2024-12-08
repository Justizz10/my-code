# program pemesanan kedai mie ayam
print("Selamat datang datang di kedai Mie Ayam\nSilahkan pilih pesanan anda:")
print("1. Mie Ayam Original (Rp8000)\n2. Mie Ayam Bakso (Rp10000)\n3. Mie Ayam Setan (Rp11000)\n4. Bakso (Rp8000)\n5. Bakso Jumbo (Rp10000)")

# memasukkan pesanan
while True:
    try:
        pilih_makanan = int(input("Masukkan pesanan sesuai angka (masukkan Nilai): "))

        if pilih_makanan == 1:
            makanan = "Mie Ayam"
            harga_makanan = 8000
            break
        elif pilih_makanan == 2:
            makanan = "Mie Ayam Bakso"
            harga_makanan = 10000
            break
        elif pilih_makanan == 3:
            makanan = "Mie Ayam Setan"
            harga_makanan = 11000
            break
        elif pilih_makanan == 4:
            makanan = "Bakso"
            harga_makanan = 8000
            break
        elif pilih_makanan == 5:
            makanan = "Bakso Jumbo"
            harga_makanan = 10000
            break
        else:
            print("Mohon Maaf, Nilai anda masukkan tidak ada dalam pesanan")
    except ValueError:
        print("Mohon maaf, tolong masukkan sebuah angka")

print("======================================================\nAnda sudah memesan", makanan,"dengan seharga Rp",harga_makanan)

while True:
    try:
        struk = input("\nKonfirmasi Pesanan?(ya/tidak): ")

        if struk == "ya":
            print("\n===================================\n      Kedai Mie Ayam       \n=================================\nMakanan:",makanan,"\nHarga:Rp",harga_makanan,"\nTerima Kasih Sudah Memesan\nSelamat Menikmati")
            break
        elif struk == "tidak":
            print("Pesanan Dibatalkan, Silahkan PULANG!!!!!")
        else:
            print("Mohon maaf, kata yang anda masukkan tidak valid")
    except ValueError:
        print("Mohon maaf, kata yang anda masukkan tidak valid")