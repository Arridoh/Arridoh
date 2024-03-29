listfilm = {
    'Action':{1:'Black Adam', 2: 'Star Wars', 3: 'Guardians of the Galaxy', 4: 'John Wick'},
    'Comedy':{1: 'Kapan Kawin', 2: 'Orang Kaya Baru', 3: 'My Stupid Boss', 4: 'Agak Laen'},
    'Fantasy':{1: 'The Chronicles of Narnia', 2: 'Wonka', 3: 'Cinderella', 4: 'Beauty and the Beast'},
    'Thriller':{1: 'Parasite', 2: 'Joker', 3: 'Bird Box', 4: 'Plane'},
}
waktufilm = {1: '08:00 WIT - 09:50 WIT',2: '14:30 WIT - 16:20 WIT',3: '21:00 WIT - 22:50 WIT',}

# harinonton = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
import datetime
tanggal = datetime.datetime.now()
hari = tanggal.strftime('%A')

namapembeli = []
umurpembeli = []
    
def garis():
    print('==============================')

print('Genre film:')
garis()
for genre in listfilm:
    print(genre)
garis()
pilih = input('Pilih genre Film: ')
print('')
for genre in listfilm:
    if pilih == genre:
        print(f'Daftar film {pilih}: ')
        garis()
        for number, film in listfilm[pilih].items():
            print(f'{number}. {film}')
        garis()    
        pilihfilm = int(input(f'Pilih film yang ingin di tonton (1-{len(listfilm)}): '))
        print('')
        for number, film in listfilm[pilih].items():
            if pilihfilm == number:
                print('Jam tayang:')
                garis()
                for x, waktu in waktufilm.items():
                    print(f'{x}. {waktu}')        
                jamtayang = int(input(f'Pilih jam tayang (1-{len(waktufilm)}): '))
                for x, waktu in waktufilm.items():
                    if jamtayang == x:
                        jamtayang = waktu
                print('')
                print('Detail film: ')
                garis()
                print(f'Nama film\t: {film}')
                print(f'Genre film\t: {genre}')
                print(f'Waktu film\t: {jamtayang}')
                if hari == 'Sunday':
                    hargatiket = 50000
                elif hari == 'Saturday':
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
                            jumlahtiket -= 1
                            print('Maaf anda tidak bisa membeli tiket')
                        print('')
                    print(f'hanya {len(namapembeli)} orang yang akan menonton')    
                    confirm = input('Ingin melanjutkan? (ya/tidak): ')
                    if confirm == 'ya':
                        print('\nInvoice ticket:')        
                        print(f'Quantity: {jumlahtiket} orang')
                        for i in range(jumlahtiket):
                            garis()
                            print('Nama :', namapembeli[i])
                            print('Usia :', umurpembeli[i], 'tahun')
                            print('Film :', film)
                            print('Waktu:', jamtayang)
                            garis()
                    else:
                        print('Baiklah, terimakasih sudah singgah')
                        break
                else:
                    print('Terimkasih sudah singgah walaupun tak sungguh :(')
            elif pilihfilm != number:
                continue
            else:
                print('Harap masukkan keyword dengan benar')
                break    
        break
    elif pilih != genre and pilih in genre:
        continue
    else:
        print('Harap masukkan keyword dengan benar')
        break

