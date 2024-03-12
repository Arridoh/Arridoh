# buat data nested dictionary 
# username password minimal 10 data mahasiswa
data = {
    '07352311151' : {'nama': 'Isra', 'password': '07352311151', 'role': 'Mahasiswa'},
    '07352311152' : {'nama': 'Sagri', 'password': '07352311152', 'role': 'Mahasiswa'},
    '07352311153' : {'nama': 'Arridoh', 'password': '07352311153', 'role': 'Mahasiswa'},
    '07352311154' : {'nama': 'Manda', 'password': '07352311154', 'role': 'Mahasiswa'},
    '07352311155' : {'nama': 'Mega', 'password': '07352311155', 'role': 'Mahasiswa'},
    '07352311156' : {'nama': 'Agung', 'password': '07352311156', 'role': 'Mahasiswa'},
    '07352311157' : {'nama': 'Ilham', 'password': '07352311157', 'role': 'Mahasiswa'},
    '07352311158' : {'nama': 'Irvan', 'password': '07352311158', 'role': 'Mahasiswa'},
    '07352311159' : {'nama': 'Salwan', 'password': '07352311159', 'role': 'Mahasiswa'},
    '07352311160' : {'nama': 'Yasmir', 'password': '07352311160', 'role': 'Mahasiswa'}
}
# buat sistem login
welcome = '''
==================================================
=|\t\t SELAMAT DATANG!! \t\t|=
=|\tSilahkan isi data dibawah untuk login\t|=
==================================================
Silahkan masukkan NPM sebagai username dan password anda!'''
print(welcome)

# penginputan dilihat pada data dictionary
username = input('Masukkan username: ')
password = input('Masukkan password: ')
 
if username in data and data[username]['password'] == password :
    print('\n=========================================')
    print('Nama\t:',data[username]['nama'])
    print('NPM\t:',username)
    print('Roles\t:',data[username]['role'])
    print('=========================================')
    print('Anda telah berhasil melakukan login!!')
else:
    print('\nlogin gagal, Username atau Password salah')