Absence = int(input('Masukkan Jumlah Kehadiran: '))
Jml_tugas = int(input('Masukkan Jumlah Tugas: '))
TotalTugas = 0
for i in range(Jml_tugas):
    tugas = int(input(f'Masukkan Nilai Tugas {i+1}: '))
    TotalTugas += tugas
Uts = int(input('Masukkan Nilai UTS: '))
Uas = int(input('Masukkan Nilai UAS: '))

kehadiran = (Absence/16)*100
rata2_tugas = TotalTugas/Jml_tugas
total_nilai = (kehadiran + rata2_tugas + Uts + Uas)/4

if total_nilai >= 90:
    print("Nilai anda: ", total_nilai)
    print("Selamat anda lulus dengan predikat : A")
elif total_nilai >=80:
    print("Nilai anda: ", total_nilai)
    print("Selamat anda lulus dengan predikat : B")
elif total_nilai >=70:
    print("Nilai anda: ", total_nilai)
    print("Selamat anda lulus dengan predikat : C")
elif total_nilai >=60:
    print("Nilai anda: ", total_nilai)
    print("Selamat anda lulus dengan predikat : D")
elif total_nilai > 0:
    print("Nilai anda: ", total_nilai)
    print("Selamat anda lulus dengan predikat : E")
else:
    print('Maaf nilai anda tidak terbaca')