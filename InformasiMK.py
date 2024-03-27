nama = input('Masukkan nama: ')
npm = input('Masukkan NPM: ')
print('')
print('Berikut matakuliah yang anda kontrak:')
print('=============================================')
print('1. Algoritma & Struktur Data')
print('2. Bahasa Indonesia')
print('3. Kalkulus')
print('4. Kecakapan Antar Personal')
print('5. Ko-Kulikuler')
print('6. Pendidikan Agama Islam')
print('7. Pendidikan Pancasila')
print('8. Pengantar Teknologi Informasi')
print('9. Wawasan Kepulauan dan Kemajemukan')
print('=============================================')
matakuliah = input('Silahkan pilih matakuliah (1-9): ')
nama_mk = {
    '1':{'Matakuliah' : 'Algoritma & Struktur Data', 'Dosen pengampu': 'Dr. Muhammad Ridha Albaar S.Kom., M.Kom.', 'Jumlah SKS': 4.00},
    '2':{'Matakuliah' : 'Bahasa Indonesia', 'Dosen pengampu': 'Asriani Thahir S.Pd., M.Pd.', 'Jumlah SKS': 2.00},
    '3':{'Matakuliah' : 'Kalkulus', 'Dosen pengampu': 'Syarifuddin N. Kapita S.Pd., M.Si.', 'Jumlah SKS': 3.00},
    '4':{'Matakuliah' : 'Kecakapan Antar Personal', 'Dosen pengampu': 'Dr. Assaf Arief S.T., M.Eng.', 'Jumlah SKS': 2.00},
    '5':{'Matakuliah' : 'Ko-Kulikuler', 'Dosen pengampu': 'Saiful Do Abdullah S.T., M.T.', 'Jumlah SKS': 1.00},
    '6':{'Matakuliah' : 'Pendidikan Agama Islam', 'Dosen pengampu': 'Fatoni Achmad S.Pd.I., M.Pd.I.', 'Jumlah SKS': 2.00},
    '7':{'Matakuliah' : 'Pendidikan Pancasila', 'Dosen pengampu': 'Firman Bunta S.Pd., M.Pd.', 'Jumlah SKS': 2.00},
    '8':{'Matakuliah' : 'Pengantar Teknologi Informasi', 'Dosen pengampu': 'Muhammad Fhadli S.Kom., M.Sc.', 'Jumlah SKS': 2.00},
    '9':{'Matakuliah' : 'Wawasan Kepulauan dan Kemajemukan', 'Dosen pengampu': 'Dr. Sudarman Samad S.T., M.T.', 'Jumlah SKS': 2.00}
}
print('')
if matakuliah in nama_mk:
    print('Informasi matakuliah:')
    print('=======================')
    print('Nama anda\t: ', nama)
    print('NPM anda\t: ', npm)
    for item in nama_mk[matakuliah]:
        print(item, '\t: ', nama_mk[matakuliah][item])
else:
    print('Maaf kode matakuliah yang anda masukkan tidak sesuai')


# pr_A = 4.00
# pr_AB = 3.50
# pr_B = 3.00
# pr_BC = 2.50
# pr_E = 0