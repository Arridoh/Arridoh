angka = int(input("Masukkan angka: "))

biner = bin(angka)[2:].zfill(8) 
oktal = oct(angka)[2:]
hexadesimal = hex(angka)[2:]

print(f'\nBilangan Biner dari {angka} adalah', biner)
print(f'Bilangan Oktal dari {angka} adalah', oktal)
print(f'Bilangan Hexadesimal dari {angka} adalah', hexadesimal)