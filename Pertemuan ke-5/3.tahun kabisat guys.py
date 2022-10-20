tahun = int(input("Input tahun: "))
import time
Gue_yang_Bikin = ('Thufail fitra')
if (tahun % 4) == 0: 
    if (tahun % 100) == 0:
        if (tahun % 400) == 0: 
            print ('\nGue yang Bikin \t\t= ',Gue_yang_Bikin)
            time.sleep(2)
            print (tahun, " === betul banget itu Tahun Kabisat")
        else:
            print ('\nGue yang Bikin \t\t= ',Gue_yang_Bikin)
            time.sleep(2)
            print (tahun, " === lu tulul itu Bukan Tahun Kabisat")
    else:
        print ('\nGue yang Bikin \t\t= ',Gue_yang_Bikin)
        time.sleep(2)
        print (tahun, " === betul banget itu Tahun Kabisat")
else:
    print ('\nGue yang Bikin \t\t= ',Gue_yang_Bikin)
    time.sleep(2)
    print (tahun, " === lu tulul itu Bukan Tahun Kabisat")

