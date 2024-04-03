import locale
import datetime
import msvcrt

listfilm = {
    'action':{'1':'Black Adam', '2': 'Star Wars', '3': 'Guardians of the Galaxy', '4': 'John Wick', '5': 'The Beekeper'},
    'comedy':{'1': 'Kapan Kawin', '2': 'Orang Kaya Baru', '3': 'My Stupid Boss', '4': 'Agak Laen'},
    'fantasy':{'1': 'The Chronicles of Narnia', '2': 'Wonka', '3': 'Cinderella', '4': 'Beauty and the Beast'},
    'thriller':{'1': 'Parasite', '2': 'Joker', '3': 'Bird Box', '4': 'Plane', '5': 'Oppenheimer'},
}
waktufilm = {'1': '08:00 WIT - 09:50 WIT','2': '14:30 WIT - 16:20 WIT','3': '21:00 WIT - 22:50 WIT',}
kursi = {'A': ['1', '2', '3', '4', '5', '6', '7', '8'],
         'B': ['1', '2', '3', '4', '5', '6', '7', '8'],
         'C': ['1', '2', '3', '4', '5', '6', '7', '8'],}
namakelompok = ['Nurhasna Hi. Saleh','M. Arridoh Fuad','Muhammad Yasmir Sanaky','Nurhasna Majid','Riyadh Rafael Hanafi','Muhammad Agung','Mega Asriyani','Putri Jumiana Idris','Mirnasari Ramatin','Fauzan Mansur','Nurdalifa Marzuki']
npmkelompok = ['07352311167','07352311153','07352311160','07352311168','07352311173','07352311156','07352311155','','','07352311180','07352311166']

def garis():
    print('==============================')

locale.setlocale(locale.LC_TIME, 'id_ID')
tanggal = datetime.datetime.now()
hari = tanggal.strftime('%A')

namapembeli = []
umurpembeli = []
tidakcukupumur = []
filmdibeli = []
waktudibeli = []
haridibeli = []
hargatiketdibeli = []
barisdibeli = []
barisdisimpan = []
kolomdibeli = []
kolomdisimpan = []

while True:
    print('Selamat datang')
    garis()
    print('1. Pesan tiket')
    print('2. lihat tiket yang dipesan')
    print('3. lihat nama kelompok')
    print('4. Exit')
    pilihan = input('Apa yang ingin anda lakukan?: ')
    if pilihan == '1' or pilihan.lower() == 'pesan tiket':
        while True:
            print('Pilih genre film:')
            garis()
            print('Genre film:')
            for genre, judul in listfilm.items():
                print(f'--> {genre}')
            garis()
            pilih = input('Pilih genre Film: ')
            print('')
            if pilih.lower() in listfilm:
                break
            else:
                print('Harap masukkan keyword dengan benar!!')
                print('')
        for genre, judul in listfilm.items():
            if pilih.lower() in listfilm and pilih.lower() != genre:
                continue
            elif pilih.lower() == genre:
                juduldipilih = judul
                while True:
                    print('Silahkan pilih film:')
                    garis()
                    print(f'Daftar film {pilih.lower()}: ')
                    for number, film in judul.items():
                        print(f'{number}. {film}')
                    garis()    
                    pilihfilm = input(f'Pilih film yang ingin di tonton (1-{len(judul)}): ')
                    print('')
                    if pilihfilm in judul:
                        break
                    else:
                        print('Pilihan tidak sesuai')
        for number, film in juduldipilih.items():
            if pilihfilm != number and pilihfilm in judul:
                continue
            elif pilihfilm == number:
                filmdipilih = film
                while True:
                    print('Jam tayang:')
                    garis()
                    for x, waktu in waktufilm.items():
                        print(f'{x}. {waktu}')        
                    jamtayang = input(f'Pilih jam tayang (1-{len(waktufilm)}): ')
                    if jamtayang in waktufilm:
                        break
                    else:
                        print('Pilihan tidak sesuai')
        for x, waktu in waktufilm.items():
            if jamtayang != x and jamtayang in waktufilm:
                continue
            elif jamtayang == x:
                while True:
                    print('Detail film: ')
                    garis()
                    print(f'Nama film\t: {filmdipilih}')
                    print(f'Genre film\t: {pilih}')
                    print(f'Waktu film\t: {waktu}')
                    if hari == 'Minggu':
                        hargatiket = 50000
                    elif hari == 'Sabtu':
                        hargatiket = 45000
                    else:
                        hargatiket = 35000
                    print(f'Harga tiket\t: Rp. {hargatiket}')
                    garis()
                    konfirmasi = input('Ingin membeli tiket? (ya/tidak): ')
                    print('')
                    if konfirmasi == 'ya':
                        jumlahtiket = int(input('Masukkan jumlah tiket: '))
                        print('')
                        for item in range(jumlahtiket):
                            print(f'Bio {item+1}: ')
                            garis()
                            nama = input('Masukkan nama: ')
                            namapembeli.append(nama)
                            umur = int(input('Masukkan umur: '))
                            umurpembeli.append(umur)
                            if umur < 18 :
                                namapembeli.remove(nama)
                                umurpembeli.remove(umur)
                                tidakcukupumur.append(nama)
                                print('Maaf anda tidak bisa membeli tiket')
                                print('')
                            else:
                                print('\nPilih tempat duduk anda:')
                                for baris, kolom in kursi.items():
                                    print(f'{baris}. {kolom}')
                                garis()    
                                while True:
                                    pilihbaris = input(f'Masukkan row (A-{baris}): ')
                                    pilihkolom = input(f'Masukkan seat (1-{len(kolom)}): ')
                                    if pilihbaris in barisdibeli and pilihkolom in kolomdibeli:
                                        print('Maaf Kursi telah dipesan')
                                    elif pilihbaris in kursi and pilihkolom in kolom:
                                        break
                                    else:
                                        print('Input yang dimasukkan tidak sesuai')
                                for baris, kolom in kursi.items():
                                    if pilihbaris != baris:
                                        continue
                                    elif pilihbaris == baris and pilihkolom in kolom:
                                        barisdibeli.append(pilihbaris)
                                        barisdisimpan.append(pilihbaris)
                                        kolomdibeli.append(pilihkolom)
                                        kolomdisimpan.append(pilihkolom)
                            waktudibeli.append(waktu)
                            haridibeli.append(hari)
                            hargatiketdibeli.append(hargatiket)
                            filmdibeli.append(filmdipilih)
                            print('')
                        barisdibeli.clear()
                        kolomdibeli.clear()   
                        if len(namapembeli) < jumlahtiket :
                            for i in range(len(tidakcukupumur)):    
                                print(f'{tidakcukupumur[i]} tidak dapat menonton')
                            garis()    
                            confirm = input('Ingin melanjutkan? (ya/tidak): ')
                            tidakcukupumur.clear()
                            if confirm == 'ya':
                                print('\nInvoice ticket:')        
                                print(f'Quantity: {len(namapembeli)} orang')
                                for i in range(len(namapembeli)):
                                    garis()
                                    print('Nama :', namapembeli[i])
                                    print('Usia :', umurpembeli[i], 'tahun')
                                    print('Film :', film)
                                    print('Row  :', barisdisimpan[i])
                                    print('Seat :', kolomdisimpan[i])
                                    print('Jam  :', waktu)
                                    print('Hari :', hari)
                                    print('Harga tiket:')
                                    print(f'Rp. {hargatiket:,}')
                                    garis()
                                print('Terimakasih, selamat menonton!')
                                garis()
                                print('Tekan enter untuk lanjut')
                                msvcrt.getch()
                                print('')
                                break
                            else:
                                print('Baiklah, terimakasih sudah singgah')
                                print('Tekan enter untuk lanjut')
                                msvcrt.getch()
                                print('')
                                break
                        else:
                            print('\nInvoice ticket:')        
                            print(f'Quantity: {jumlahtiket} orang')
                            for i in range(jumlahtiket):
                                garis()
                                print('Nama :', namapembeli[i])
                                print('Usia :', umurpembeli[i], 'tahun')
                                print('Film :', film)
                                print('Row  :', barisdisimpan[i])
                                print('Seat :', kolomdisimpan[i])
                                print('Jam  :', waktu)
                                print('Hari :', hari)
                                print('Harga tiket:')
                                print(f'Rp. {hargatiket:,}')
                                garis()
                            print('Terimakasih, selamat menonton!')
                            garis()
                            print('Tekan enter untuk lanjut')
                            msvcrt.getch()
                            print('')
                            break                                                       
                    else:
                        print('Terimakasih sudah singgah')
                        garis()
                        print('Tekan enter untuk lanjut')
                        msvcrt.getch()
                        print('')
                        break
    elif pilihan == '2' or pilihan.lower() == 'lihat tiket yang dipesan':
        print('')
        print(f'{len(namapembeli)} ticket dipesan')
        for i in range(len(namapembeli)):
            print('Bio', i+1)
            garis()
            print('Nama :', namapembeli[i])
            print('Usia :', umurpembeli[i], 'tahun')
            print('Film :', filmdibeli[i])
            print('Row  :', barisdisimpan[i])
            print('Seat :', kolomdisimpan[i])
            print('Jam  :', waktudibeli[i])
            print('Hari :', haridibeli[i])
            print('Harga tiket: ', hargatiketdibeli[i])
            garis()
        print('')
    elif pilihan == '3' or pilihan.lower() == 'lihat nama kelompok':
        print('')
        print('Nama kelompok: ')
        garis()
        for i in range(len(namakelompok)):
            print(f'{i+1}. Nama: {namakelompok[i]}')
            print(f'   NPM : {npmkelompok[i]}')
        print('')
    elif pilihan == '4' or pilihan.lower() == 'exit':
        garis()
        print('Program selesai')
        print('Anda telah keluar')
        break
    else:
        print('')
        print('Pilihan tidak valid, silahkan pilih lagi')
        print('')