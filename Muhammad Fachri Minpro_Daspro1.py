print("Masukkan nama anda")
nama = input("Nama: ")
id = int(input("ID: "))

# Proses verivikasi nama dan id
while True:
    if nama == "fahri" and id == 150456:
        print("Nama dan ID terverifikasi")
        break
    else:
        print("Nama atau ID tidak ditemukan, silakan coba lagi.")
        nama = input("Nama: ")
        id = int(input("ID: "))

# Menghitung upah dan bonus
while True:
    print("Apakah anda ingin melakukan penghitungan upah? ")
    penghitungan = input()

    if penghitungan == "ya":
        print("Silahkan lakukan pengisian data")
        
        jam_kerja = int(input("waktu kerja: "))
        upah = int(input("upah : "))

        if jam_kerja >= 160:
            bonus = 10  # 10% bonus
            upah_bonus = upah * bonus // 100
            total_upah = upah + upah_bonus
            print("Bonus: ", upah_bonus)
            print("Total upah anda: ", total_upah)
        else:
            print("Anda tidak mendapatkan bonus, upah anda adalah: ", upah)

    elif penghitungan == "tidak":
        print("Selesai")
        break  

    else:
        print("Input tidak valid. Harap coba lagi .")