print('Masukkan nilai awal dan nilai akhir')

nilai_awal = int(input('\nnilai awal: '))
nilai_akhir = int(input('nilai akhir: '))
gue_Yang_Bikin = 'Thufail fitra'
print ("\ngue_Yang_Bikin \t\t= ",gue_Yang_Bikin)

print("""\nTampilkan bilangan
 1. Ganjil
 2. Genap""")

pilihan = int(input('Pilihan: '))

# pilihan = 'string'
# while pilihan == 'string':
    # periksa kalau pilihan bukan 1 dan 2
# if pilihan not in [1, 2]:
#       print('Pilihan salah')
# else:
#     for x in range(nilai_awal, nilai_akhir + 1):
#             if pilihan == 1 and x % 2 == 1:
#                 print(x, end=' ')
#             elif pilihan == 2 and x % 2 == 0:
#                 print(x, end=' ')
#         else:
                
#     # ganti baris ketika perulangan selesai
#                 print('')
#                 # break
if pilihan not in [1, 2]:
      print('Pilihan salah')
else:
  for x in range(nilai_awal, nilai_akhir + 1):
    if pilihan == 1 and x % 2 == 1:
      print(x, end=' ')
    elif pilihan == 2 and x % 2 == 0:
      print(x, end=' ')
  else:
    # ganti baris ketika perulangan selesai
    print('')