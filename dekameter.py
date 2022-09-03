import time


ulang = True
while (ulang):
    print("")
    print("-------------------------------------------------------")
    print("----------------- KONVERSI SATUAN DAM -----------------")
    print("-------------------------------------------------------")

    print('')
    print("AI: silahkan masukan nilai yang ingin dikonversikan")
    dam = float(input('user: '))

    print('')
    print('======================== Hasil ========================')
    time.sleep(1)
    
    print('')
    dam2mm = (dam * 10000) 
    print("AI: hasil konversi", dam, "dekameter ke milimeter :", dam2mm, "mm")
    time.sleep(0.5)

    dam2cm = (dam * 1000)
    print("AI: hasil konversi", dam, "dekameter ke centimeter :", dam2cm, "cm")
    time.sleep(0.5)

    dam2dm = (dam * 100)
    print("AI: hasil konversi", dam, "dekameter ke desimeter :", dam2dm, "dm")
    time.sleep(0.5)

    dam2m = (dam * 10)
    print("AI: hasil konversi", dam, "dekameter ke meter :", dam2m, "m")
    time.sleep(0.5)

    dam2hm = (dam / 10)
    print("AI: hasil konversi", dam, "dekameter ke hektometer :", dam2hm, "hm")
    time.sleep(0.5)

    dam2km = (dam / 100)
    print("AI: hasil konversi", dam, "dekameter ke kilometer :", dam2km, "km")
    time.sleep(0.5)

    print('')
    print('======================= selesai =======================')
    time.sleep(1.5)

    print('')
    print('AI: apakah anda ingin melakukan pengulangan ?')
    time.sleep(1.5)
    print('AI: ketik 1 jika ingin ulang, ketik 0 jika ingin berhenti.')
    time.sleep(1.5)
    ulang = input('User: ')  
 

    if ulang == '0':
        print('')
        print('memproses')
        time.sleep(1)
        print('memproses.')
        time.sleep(1)
        print('memproses..')
        time.sleep(1)
        print('memproses...')
        time.sleep(1)
        print('program diberhentikan')
        time.sleep(0.5)
        print('======================= selesai =======================')
        print('')
        break
    elif ulang == '1':
        print('')
        print('memproses')
        time.sleep(1)
        print('memproses.')
        time.sleep(1)
        print('memproses..')
        time.sleep(1)
        print('memproses...')
        time.sleep(1)
        ulang == True
        print('')
    else:
        print('')
        print('AI: salah dalam penginputan')
        time.sleep(1.5)
        print('AI: program akan diberhentikan dalam')
        time.sleep(1.5)
        print('AI: 3')
        time.sleep(1)
        print('AI: 2')
        time.sleep(1)
        print('AI: 1')
        time.sleep(1)
        print('========================selesai========================')
        print('')
        break