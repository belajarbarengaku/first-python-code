import numpy as np

def menuadmin():
    p = input('\npinjaman mobil \n1.tambah data \n2.list data\n3.keluar \ninput : ')
    if p == "1":
        tambahdata()
    elif p == "2":
        print("mobil  status  pinjaman")
        for x in arr_B:
            for i in x:
                print(i, end = " ")
        menuadmin()
    elif p == "3":
        login()

def tambahdata():
    mobil = input('masukkan nama mobil : ')
    arr_B.insert(-1,[mobil,'tidakdisewa','baru'," "])
    print("data sudah masuk\n")
    print("mobil status peminjam")
    for x in arr_B:
        for i in x:
            print(i, end = " ")
        print("\n")
    menuadmin()

def peminjaman(pinjam):
    i = input('Silahkan Pinjam Mobil Dari Menu List Mobil : ')
    while True:

        for c in arr_B:

            if i == c[0] and c[1] == "tidakdisewa":
                print("mobil" + c[0] + "disewa")
                c[1] = "disewa"
                c[2] = "bekas"
                if pinjam == "menubeli":
                    menubeli()
                elif pinjam == "menuuser":
                    menuuser()
                break
            elif i == c[0] and c[1] == "disewa":
                print("Mmbil " + c[0] + " telah disewa lihat mobil lain")
                menuuser()
                break
        print("Mobil Tidak Ada.")
        menuuser()
        break

def beli():
    i = input('Silahkan Pembelian Mobil Dari Menu List Mobil : ')
    hapus = -1
    while True:

        for c in arr_B:

            hapus +=1
            if i == c[0] and c[1] == "tidakdisewa":
                del arr_B[hapus]
                print("mobil" + c[0] + "telah di beli")
                menubeli()
                break
            elif i == c[0] and c[1] == "disewa":
                print("Mmbil " + c[0] + " telah disewa lihat mobil lain")
                menuuser()
                break
        print("Mobil Tidak Ada.")
        menuuser()
        break

def pengembalian(kembali):
    i = input('silahkan kembalikan mobil yang anda sewa :')
    while True:

        for c in arr_B:

            if i == c[0]:
                print("mobil" + c[0] + "dikembalikan")
                c[1] = "tidakdisewa"
                if kembali == "menubeli":
                    menubeli()
                elif kembali == "menuuser":
                    menuuser()
                break
            else:
                print("mobil tidak anda sewa")
                menuuser()
                break
        print("mobil tidak ada")
        menuuser()
        break

def menuuser():
    p = input('peminjaman mobil \n1.peminjaman\n2.pengembalian\n3.list mobil\n4.keluar\nInput : ')
    if p == "1":
        peminjaman("menuuser")
    elif p == "2":
        pengembalian("menuuser")
    elif p == "3":
        print("mobil status peminjaman\n")
        for x in arr_B:
            for i in x:
                print(i, end = " ")
            print("\n")
        menuuser()
    elif p == "4":
        login()

def menubeli():
    p = input('menu sewa dan pembelian mobil'
              '\n1. penyewaan'
              '\n2. pengembalian'
              '\n3. pembelian'
              '\n4. list mobil'
              '\n5. keluar'
              'input : ')
    if p == "1":
        peminjaman("menubeli")
    elif p == "2":
        pengembalian("menubeli")
    elif p == "3":
        beli()
    elif p == "4":
        print("mobil status peminjaman\n")
        for x in arr_B:
            for i in x:
                print(i, end = " ")
            print("\n")
        menubeli()
    elif p == "5":
        login()

def login():
  arr_A = np.array = [["sherin","123","admin"],["dwi","123","user"],["april","123","pembeli"]]

  print("login")
  username = input("masukkan username : ")
  password = input("masukkan password : ")

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
        elif username == x[0] and password == x[1] and x[2] == "pembeli":
            print("=" * 40)
            print("\n\n" + "Selamat Datang di Rental Mobil Jaya" + x[0])
            print("=" * 40)
            menubeli()
            break
    print("salah akun. \n\n")
    break

arr_B = np.array = ([[]])
login()