kehadiran = int(input('masukkan kehadiran (1-16): '))
jml_tugas = int(input('Masukkan banyak tugas: '))

total_tugas = 0
for i in range(jml_tugas):
    tugas = int(input(f'Masukkan niali tugas {i+1}: '))
    total_tugas += tugas

nilaiUTS = int(input('Masukkan nilai UTS: '))
nilaiUAS = int(input('Masukkan nilai UAS: '))

kehadiran = (kehadiran/16)*100
total_tugas = total_tugas/jml_tugas
total_nilai = int((kehadiran + total_tugas + nilaiUTS + nilaiUAS)/4)
print("")
if total_nilai >= 90:
    print('Nilai anda:', total_nilai)
    print('Predikat anda: A')
elif total_nilai >= 80:
    print('Nilai anda:', total_nilai)
    print('Predikat anda: B')
elif total_nilai >= 70:
    print('Nilai anda:', total_nilai)
    print('Predikat anda: C')
elif total_nilai >= 60:
    print('Nilai anda:', total_nilai)
    print('Predikat anda: D')
else:
    print('Nilai anda:', total_nilai)    
    print('Predikat anda: E')