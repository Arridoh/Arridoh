# Buatlah program yang dapat menggabungkan 2 data dictionary
jadwalDasproIf3 = {'senin': 'jam 08:00', 'kamis': 'jam 10:50', 'jumat': 'jam 08:00'}   
jadwalDasproIf2 = {'selasa': 'jam 08:00', 'rabu': 'jam 10:50', 'sabtu': 'jam 15:00'}

# Masukkan data dictionary jadwalDasproIf2 kedalam jadwalDasproIf3
jadwalDasproIf3.update(jadwalDasproIf2)
print('\nData dictionery Setelah digabungkan:')
print(jadwalDasproIf3)
