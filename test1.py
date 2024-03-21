nama = input('Masukkan username: ')
password = input('Masukkan password: ')

username = 'rido'
sandi = '12345'

if nama == username and password == sandi:
    print('\nAnda berhasil login!!')
    print('Pilih matakuliah anda:')
    print('1. Matematika Diskrit')
    print('2. Aljabar Linear')
    print('3. Logika matematika')
    print('4. Dasar Pemrograman')
    matakuliah = int(input('Masukkan pilihan (1-4): '))
    print('')
    if matakuliah == 1:
        Dosen = 'Pak Syarifuddin'
        matakuliah = 'Matematika Diskrit'
        print('Berikut informasi anda:')    
        print('Username\t: ', nama)
        print('Matakuliah\t: ', matakuliah)
        print('Dosen pengampuh\t: ', Dosen)

    elif matakuliah == 2:
        Dosen = 'Ibu Aisjah'
        matakuliah = 'Aljabar Linear'
        print('Berikut informasi anda:')
        print('Username\t: ', nama)
        print('Matakuliah\t: ', matakuliah)
        print('Dosen pengampuh\t: ', Dosen)
    
    elif matakuliah == 3:
        Dosen = 'Pak Amal'
        matakuliah = 'Logika Matematika'
        print('Berikut informasi anda:')
        print('Username\t: ', nama)
        print('Matakuliah\t: ', matakuliah)
        print('Dosen pengampuh\t: ', Dosen)

    elif matakuliah == 4:
        Dosen = 'Pak Yasir'
        matakuliah = 'Dasar Pemrograman'
        print('Berikut informasi anda:')    
        print('Username\t: ', nama)
        print('Matakuliah\t: ', matakuliah)
        print('Dosen pengampuh\t: ', Dosen)
    else:
        print('Matakuliah tidak tersedia')
else:
    print('Username atau Password salah')