import numpy as np
#untuk array

def menuadmin():
    p = input("\nSewa mobil \n1. Tambah data \n2. List data\n3. Keluar \nInput : ")
    if p == "1":
        tambahdata()
    elif p == "2":
        print("Mobil  Status  Pinjaman")
        for x in arr_B:
            for i in x:
                print(i, end = " ")
        menuadmin()
    elif p == "3":
        login()

def tambahdata():
    mobil = input("Masukkan Nama Mobil : ")
    arr_B.insert(-1,[mobil,'tidakdisewa'," "])
    print("Data Sudah Masuk\n")
    print("Mobil Status Peminjam")
    for x in arr_B:
        for i in x:
            print(i, end = " ")
        print("\n")
    menuadmin()


def peminjaman():
    i = input("Silahkan Pinjam Mobil Dari Menu List Mobil : ")
    while True:

        for c in arr_B:

            if i == c[0] and c[1] == "tidakdisewa":
                print("Mobil " + c[0] + " disewa")
                c[1] = "disewa"
                menuuser()
                break
            elif i == c[0] and c[1] == "disewa":
                print("Mobil " + c[0] + " Telah disewa Lihat Mobil Lain")
                menuuser()
                break
        print("Mobil Tidak Ada.")
        menuuser()
        break

def pengembalian():
    i = input("Silahkan Kembalikan Mobil yang Anda Sewa :")
    while True:

        for c in arr_B:

            if i == c[0]:
                print("Mobil " + c[0]+ " dikembalikan")
                c[1] = "tidakdisewa"
                menuuser()
                break
            else:
                print("Mobil tidak Anda Sewa")
                menuuser()
                break
        print("Mobil Tidak ada")
        menuuser()
        break


def menuuser():
    p = input("Sewa Mobil \n1. Peminjaman\n2. Pengembalian\n3. List Mobil\n4. Keluar\nInput : ")
    if p == "1":
        peminjaman()
    elif p == "2":
        pengembalian()
    elif p == "3":
        print("Mobil Sewaan\n")
        for x in arr_B:
            for i in x:
                print(i, end=" ")
            print("\n")
        menuuser()
    elif p == "4":
        login()

def login():
  arr_A = np.array = ([["sherin","123","admin"],["dwi","123","user"],["april","123","user"]])

  print("=" * 40)
  print("        Login Rental Mobil Jaya")
  print("=" * 40)
  username = input("Masukkan username : ")
  password = input("Masukkan password : ")

  while True:

    for x in arr_A:
        if username == x[0] and password == x[1] and x[2] == "admin":
            print("=" * 50)
            print(" Selamat Datang Admin Rental Mobil Jaya " + x[0])
            print("=" * 50)
            menuadmin()
            break
        elif username == x[0] and password == x[1] and x[2] == "user":
            print("=" * 40)
            print("\n\n" + "Selamat Datang di Rental Mobil Jaya" + x[0])
            print("=" * 40)
            menuuser()
            break
    print("Login Gagal! Coba Lagi!. \n\n")
    break

arr_B = np.array = ([[]])
login()