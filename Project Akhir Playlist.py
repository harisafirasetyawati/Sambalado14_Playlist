playlist = []
genre_set = {"pop", "rock", "jazz", "dangdut", "k-pop"}
rating_valid = (1, 2, 3, 4, 5)

album_list = {}
favorit_list = []
play_count = {}
album_play_count = {}

def tambah_lagu():
    while True:
        print("\n=== Tambah Lagu ===")
        judul = input("Judul lagu       : ").strip().lower()
        penyanyi = input("Penyanyi         : ").strip().lower()

        for lagu in playlist:
            if lagu["judul"] == judul and lagu["penyanyi"] == penyanyi:
                print("\nLagu sudah ada dalam playlist!\n")
                break
        else:
            print("\nGenre tersedia:", genre_set)
            while True:
                genre = input("Pilih genre       : ").lower()
                if genre in genre_set:
                    break
                print("Genre tidak tersedia!")
            while True:
                try:
                    rating = int(input("Masukkan rating (1–5): "))
                    if rating in rating_valid:
                        break
                    print("Rating harus 1–5!")
                except ValueError:
                    print("Harus angka!")

            lagu = {
                "judul": judul,
                "penyanyi": penyanyi,
                "genre": genre,
                "rating": rating
            }
            playlist.append(lagu)
            play_count[(judul, penyanyi)] = 0
            print("\nLagu berhasil ditambahkan!")
        if input("Tambah lagi? (y/n): ").lower() != "y":
            break

def tampilkan_playlist():
    print("\n=== Daftar Playlist ===")
    if not playlist:
        print("Playlist kosong!")
        return

    for no, lagu in enumerate(playlist, start=1):
        key = (lagu["judul"], lagu["penyanyi"])
        print(f"{no}. {lagu['judul'].title()} - {lagu['penyanyi'].title()} | "
              f"Genre: {lagu['genre']} | Rating: {lagu['rating']}")

def ubah_lagu():
    if not playlist:
        print("\nPlaylist kosong!")
        return
    tampilkan_playlist()
    print("\n=== Ubah Lagu Berdasarkan Judul & Penyanyi ===")
    judul_lama = input("Masukkan judul lagu lama: ").lower().strip()
    penyanyi_lama = input("Masukkan penyanyi lama: ").lower().strip()
    lagu = next(
        (l for l in playlist
         if l["judul"] == judul_lama and l["penyanyi"] == penyanyi_lama),
        None
    )
    if not lagu:
        print("\nLagu tidak ditemukan!")
        return
    old_key = (lagu["judul"], lagu["penyanyi"])

    judul_baru = input("Judul baru (Enter jika tidak mengubah): ").lower().strip()
    if judul_baru:
        lagu["judul"] = judul_baru
    penyanyi_baru = input("Penyanyi baru (Enter jika tidak mengubah): ").lower().strip()
    if penyanyi_baru:
        lagu["penyanyi"] = penyanyi_baru
    print("\nGenre tersedia:", genre_set)
    genre_baru = input("Genre baru (Enter jika tidak mengubah): ").lower().strip()
    if genre_baru:
        if genre_baru in genre_set:
            lagu["genre"] = genre_baru
        else:
            print("Genre tidak valid, genre tidak diubah.")
    rating_baru = input("Rating baru (1-5, Enter jika tidak mengubah): ").strip()
    if rating_baru:
        try:
            rating_baru = int(rating_baru)
            if rating_baru in rating_valid:
                lagu["rating"] = rating_baru
            else:
                print("Rating tidak valid, rating tidak diubah.")
        except ValueError:
            print("Input bukan angka, rating tidak diubah.")

    new_key = (lagu["judul"], lagu["penyanyi"])
    for album in album_list.values():
        for i, key in enumerate(album):
            if key == old_key:
                album[i] = new_key
    for i, key in enumerate(favorit_list):
        if key == old_key:
            favorit_list[i] = new_key
    if new_key != old_key:
        value = play_count.pop(old_key, 0)
        play_count[new_key] = play_count.get(new_key, 0) + value
    print("\nData lagu berhasil diubah!")

def hapus_lagu():
    print("\n=== Hapus Lagu ===")
    judul = input("Masukkan judul lagu: ").lower()
    penyanyi = input("Masukkan penyanyi lagu: ").lower()
    found = False
    for lagu in playlist:
        if lagu["judul"] == judul and lagu["penyanyi"] == penyanyi:
            found = True

            playlist.remove(lagu)
            play_count.pop((judul, penyanyi), None)

            print("Lagu berhasil dihapus!\n")
            break
    if not found:
        print("Lagu tidak ditemukan!\n")

    for album in album_list.values():
        if (judul, penyanyi) in album:
            album.remove((judul, penyanyi))
    if (judul, penyanyi) in favorit_list:
        favorit_list.remove((judul, penyanyi))

def cari_lagu():
    if not playlist:
        print("\nPlaylist kosong!")
        return
    print("\n=== Cari Lagu ===")
    judul = input("Judul: ").lower()
    penyanyi = input("Penyanyi: ").lower()
    hasil = [
        l for l in playlist
        if l["judul"] == judul and l["penyanyi"] == penyanyi
    ]
    if hasil:
        print("\nLagu ditemukan!")
        for l in hasil:
            print(f"- {l['judul'].title()} - {l['penyanyi'].title()}")
    else:
        print("Tidak ditemukan!")

def buat_album():
    nama = input("\nNama album: ").lower()
    if nama in album_list:
        print("Album sudah ada!")
        return
    album_list[nama] = []
    album_play_count[nama] = 0
    print("Album berhasil dibuat!")

def tambah_lagu_ke_album():
    if not playlist:
        print("\nPlaylist kosong!")
        return
    tampilkan_album()
    nama = input("\nMasukkan nama album: ").lower()

    if nama not in album_list:
        print("Album tidak ditemukan!")
        return
    tampilkan_playlist()
    while True:
        print("\n=== Tambah Lagu ke Album ===")
        judul = input("Judul lagu: ").lower()
        if judul == "0":
            break
        penyanyi = input("Penyanyi: ").lower()
        lagu = next((l for l in playlist if l["judul"] == judul and l["penyanyi"] == penyanyi), None)

        if not lagu:
            print("Lagu tidak ditemukan!")
            continue
        key = (judul, penyanyi)
        if key in album_list[nama]:
            print("Sudah ada dalam album!")
        else:
            album_list[nama].append(key)
            print("Berhasil ditambahkan!")
        if input("Tambah lagi? (y/n): ").lower() != "y":
            break

def tampilkan_album():
    print("\n=== Daftar Album ===")
    if not album_list:
        print("Belum ada album!")
        return
    for nama, isi in album_list.items():
        print(f"\nAlbum: {nama.title()}")
        if not isi:
            print("  (Kosong)")
            continue
        for no, (judul, penyanyi) in enumerate(isi, start=1):
            print(f"  {no}. {judul.title()} - {penyanyi.title()}")

def tambah_favorit():
    if not playlist:
        print("\nPlaylist kosong!")
        return
    tampilkan_playlist()
    while True:
        print("\n=== Tambah Lagu Favorit ===")
        judul = input("Judul Lagu: ").lower()
        penyanyi = input("Penyanyi: ").lower()
        lagu = next((l for l in playlist if l["judul"] == judul and l["penyanyi"] == penyanyi), None)
        if not lagu:
            print("Lagu tidak ditemukan!")
            continue
        key = (judul, penyanyi)
        if key in favorit_list:
            print("Sudah ada di favorit!")
        else:
            favorit_list.append(key)
            print("Ditambahkan ke favorit!")
        if input("Tambah lagi? (y/n): ").lower() != "y":
            break

def tampilkan_favorit():
    print("\n=== Daftar Lagu Favorit ===")
    if not favorit_list:
        print("Belum ada favorit!")
        return
    for no, (judul, penyanyi) in enumerate(favorit_list, start=1):
        print(f"{no}. {judul.title()} - {penyanyi.title()}")

def putar_lagu():
    if not playlist:
        print("\nPlaylist kosong!")
        return
    while True:
        tampilkan_playlist()
        print("\n=== Putar Lagu ===")
        judul = input("Judul: ").lower()
        penyanyi = input("Penyanyi: ").lower()
        lagu = next((l for l in playlist if l["judul"] == judul and l["penyanyi"] == penyanyi), None)
        if not lagu:
            print("Lagu tidak ditemukan!")
            continue

        key = (judul, penyanyi)
        play_count[key] += 1
        print(f"Memutar: {judul.title()} - {penyanyi.title()}")
        print(f"Total diputar: {play_count[key]}")

        for album, daftar in album_list.items():
            if key in daftar:
                album_play_count[album] += 1
        if input("Putar lagi? (y/n): ").lower() != "y":
            break

def lagu_tersering_diputar():
    print("\n=== Daftar Lagu yang Diputar ===")
    if not play_count:
        print("Belum ada data pemutaran!")
        return
    no = 1
    for (judul, penyanyi), jumlah_putar in play_count.items():
        print(f"{no}. {judul.title()} - {penyanyi.title()} | Diputar: {jumlah_putar} kali")
        no += 1

def menu():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tambah Lagu")
        print("2. Tampilkan Playlist")
        print("3. Ubah Lagu")
        print("4. Hapus Lagu")
        print("5. Cari Lagu")
        print("6. Buat Album")
        print("7. Tambah Lagu ke Album")
        print("8. Tampilkan Album")
        print("9. Tambah Favorit")
        print("10. Tampilkan Favorit")
        print("11. Putar Lagu")
        print("12. Lagu Sering Diputar")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_lagu()
        elif pilihan == "2":
            tampilkan_playlist()
        elif pilihan == "3":
            ubah_lagu()
        elif pilihan == "4":
            hapus_lagu()
        elif pilihan == "5":
            cari_lagu()
        elif pilihan == "6":
            buat_album()
        elif pilihan == "7":
            tambah_lagu_ke_album()
        elif pilihan == "8":
            tampilkan_album()
        elif pilihan == "9":
            tambah_favorit()
        elif pilihan == "10":
            tampilkan_favorit()
        elif pilihan == "11":
            putar_lagu()
        elif pilihan == "12":
            lagu_tersering_diputar()
        elif pilihan == "0":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

menu()