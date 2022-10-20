import time

Angka_absurd = 'string'
Gue_yang_Bikin = ('Thufail fitra')
while Angka_absurd == 'string':
    Angka_absurd = int(input('masukan angka tergila kalian : '))
    if (Angka_absurd%2==1):
        print ('\nGue yang Bikin \t\t= ',Gue_yang_Bikin)
        time.sleep(2)
        print ( 'yee kan pada tau kalo === ',Angka_absurd, ' === itu GANJIL CUY')
        
    else:
        print ('\nGue yang Bikin \t\t= ',Gue_yang_Bikin)
        time.sleep(2)
        print ( 'yee kan pada tau kalo === ',Angka_absurd, ' ===  itu GENAP CUY')  

