# fruit market program v.0.0.1
# initialize variables

# Define fruit database
database_buah = [
    {
        "nama":"Apel",
        "harga":10000,
        "stok":5,
        "cart":None,
    },
    {
        "nama":"Jeruk",
        "harga":15000,
        "stok":7,
        "cart":None,
    },
    {
        "nama":"Anggur",
        "harga":20000,
        "stok":9,
        "cart":None,
    }
]

def tampilkan_daftar_buah():
    # print out daftar buah / READ
    # print header
    print("|Index\t | Nama  \t | Harga\t | Stok\t | Cart\t |")
    for i in range(0, len(database_buah)):
        print(f"|{i}\t | {database_buah[i]['nama']}  \t | {database_buah[i]['harga']}\t | {database_buah[i]['stok']}\t | {database_buah[i]['cart']}\t |")

def tambah_buah():
    #menambah buah / CREATE
    #memeriksa nama buah lama
    nama_buah_lama = [buah['nama'] for buah in database_buah]

    #meminta input  
    nama_buah_baru = input("Masukkan Nama Buah Baru: ")
    #validasi apakah nama buah baru ada di database
    if nama_buah_baru in nama_buah_lama:
        print("Buah sudah ada! ")
    else:
        harga_buah_baru = int(input("Masukkan Harga Buah Baru: "))
        stok_buah_baru = int(input("Masukkan Stok Buah Baru: "))
        database_buah.append({
            "nama":nama_buah_baru,
            "harga":harga_buah_baru,
            "stok":stok_buah_baru,
            "cart":None,
        })

def menghapus_buah():
    #menghapus buah / DELETE
    for i in range(0, len(database_buah)):
        print(f"Buah tersedia: {database_buah[i]['nama']}, Indeks: {i} ")
    index_buah_to_be_deleted = int(input("Masukkan Index Buah Ingin Dihapus: "))
    del database_buah[index_buah_to_be_deleted]

def update_buah():
    #update buah/ UPDATE
    for i in range(0, len(database_buah)):
        print(f"Buah tersedia: {database_buah[i]['nama']}, Indeks: {i} ")
    index_buah_to_be_updated = int(input("Masukkan Index Buah Ingin Diperbarui: "))
    #serve previous information to the user
    print(f"Buah yang akan diperbarui: {database_buah[index_buah_to_be_updated]['nama']}")
    print(f"Harga Buah sekarang: {database_buah[index_buah_to_be_updated]['harga']}")
    harga_buah_baru = int(input("Masukkan Harga Baru: "))
    if harga_buah_baru == 0 :
        pass
    else:
        database_buah[index_buah_to_be_updated]['harga'] = harga_buah_baru

    print(f"Stok Buah sekarang: {database_buah[index_buah_to_be_updated]['stok']}")
    stok_buah_baru = int(input("Masukkan Stock Buah Baru: "))
    if stok_buah_baru == 0 :
        pass
    else:
        database_buah[index_buah_to_be_updated]['stok'] = stok_buah_baru

def membeli_buah():
    for i in range(0, len(database_buah)):
        while database_buah[i]['cart'] is None:
            print(f"Jumlah {database_buah[i]['nama']} yang tersedia: {database_buah[i]['stok']}")
            try:
                temp_jumlah_buah = int(input(f"Masukkan Jumlah {database_buah[i]['nama']} : "))
                if temp_jumlah_buah< database_buah[i]['stok']:
                    database_buah[i]['cart'] = temp_jumlah_buah
                else:
                    print("Kelebihan!")
            except Exception as e:
                print(e)
                print("Input tidak benar!")
                
    grand_total = 0
    for i in range(0, len(database_buah)):
        database_buah[i]['total_belanja'] = database_buah[i]['cart'] * database_buah[i]['harga']
        grand_total = grand_total + database_buah[i]['total_belanja']

    # Print the shopping cart details
    print("\nDetail Belanja")
    for i in range(0, len(database_buah)):
        print(f"{database_buah[i]['nama']} : {database_buah[i]['cart']} x {database_buah[i]['harga']} = {database_buah[i]['total_belanja']}")
        if grand_total == 0: 
            pass
        else:
            print("\nTotal :", grand_total)

    #read customer payment amount
    jumlah_pembayaran = int(input("Masukkan jumlah uang : "))
    if jumlah_pembayaran>grand_total:
        print("Terimakasih")
        print("Kembalian anda ",jumlah_pembayaran-grand_total)

        for i in range(0, len(database_buah)):
            database_buah[i]['stok'] = database_buah[i]['stok'] - database_buah[i]['cart']


    elif jumlah_pembayaran==grand_total:
        print("Terimakasih")
        for i in range(0, len(database_buah)):
            database_buah[i]['stok'] = database_buah[i]['stok'] - database_buah[i]['cart']
    else:
        print("Pembelian anda dibatalkan")
        print("Uang anda Kurang : ",abs(grand_total-jumlah_pembayaran))

    for i in range(0, len(database_buah)):
        database_buah[i]['cart'] = None

menu=0
while menu!=6:
    print("Selamat datang di Pasar Buah")
    print("List Menu: ")
    print("1. Menampilkan Daftar Buah")
    print("2. Menambah Buah")
    print("3. Menghapus Buah")
    print("4. Update Buah")
    print("5. Membeli Buah")
    print("6. Exit Program")
    try:
        menu = int(input("Masukkan input Menu, 1-6: "))
        if menu == 1:
            tampilkan_daftar_buah()
        elif menu == 2:
            tambah_buah()
        elif menu == 3:
            menghapus_buah()
        elif menu == 4:
            update_buah()
        elif menu == 5:
            membeli_buah()
        else:
            pass

    except Exception as e:
        print(e)
        print("Input tidak benar!")


# 