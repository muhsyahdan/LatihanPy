data = []
while True:
    print("="*8+"menu"+"="*8)
    print("\n1.input data")
    print("2. tampilkan data")
    print("3. update data")
    print("4. hapus data")
    print("0. keluar")

    pilihan = int(input("masukan pilihan anda : "))
    if pilihan == 0:
        print("terimakasih")
        break
    elif pilihan == 1:
        nama = input("masukan nama : ")
        umur = input("masukan umur : ")
        alamat = input("masukan alamat : ")
        data.append({"Nama":nama, "Umur":umur,"alamat":alamat})
        print("data berhasil ditambahkan!!")
    elif pilihan == 2:
        print("\nData")
        for i,item in enumerate(data,start=1):
            print(f"{i}. Nama : {item['Nama']}, Umur : {item['Umur']}, Alamat : {item['alamat']}")
    elif pilihan == 3:
        if not data:
            print("data kosong, masukan data")
        else:
            print("pilih data yang ingin di update")
            for i,item in enumerate(data,start=1):
                print(f"{i}. Nama : {item['Nama']}, Umur : {item['Umur']}, Alamat : {item['alamat']}")
            choice = int(input("masukan nomor yang ingin diubah : "))
            if 1<= choice <= len(data):
                item_to_update = data[choice-1]
                new_nama = input("masukan nama : ")
                new_umur = input("masukan umur : ")
                new_alamat = input ("masukan alamat : ")

                item_to_update["Nama"] = new_nama
                item_to_update["Umur"] = new_umur
                item_to_update["alamat"] = new_alamat
                print("data berhasil diupdate")
            else:
                print("pilihan tidak valid")
    elif pilihan == 4:
        if not data:
            print("data kosong")
        else:
            print("pilih data yang ingin dihapus")
            for i,item in enumerate(data,start=1):
                print(f"{i}. Nama : {item['Nama']}, Umur : {item['Umur']}, Alamat : {item['alamat']}")
            delete_choice = int(input("masukan nomor yang ingin anda hapus : "))
            if 1<= delete_choice <=len(data):
                del data[delete_choice-1]
                print("data berhasil dihapus")
    else:
        print("pilihan tidak valid")

                    