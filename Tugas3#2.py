# konversi dua data list menjadi data dictionary
key = ['Nama','NPM','Roles']
value = ['Arridoh','07352311153','Mahasiswa']

dictionery= {key[i]: value[i] for i in range(len(key))}

print('Data Dictionery:')
print(dictionery)