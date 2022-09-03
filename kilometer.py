import time


ulang = True
while (ulang):
    print('')
    print("-------------------------------------------------------")
    print("----------------- KONVERSI SATUAN KM ------------------")
    print("-------------------------------------------------------")

    print('')
    print("AI: silahkan masukan nilai yang ingin dikonversikan")
    km = float(input("User: "))

    print('')
    print('======================== Hasil ========================')
    time.sleep(1)

    print('')
    km2mm = km * 1000000
    print("hasil konversi", km, "kilometer ke mm :", km2mm, "mm")
    time.sleep(0.5)

    km2cm = km * 100000
    print("hasil konversi", km, "kilometer ke km :", km2cm, "cm")
    time.sleep(0.5)

    km2dm = km * 10000
    print("hasil konversi", km, "kilometer ke dm :", km2dm, "dm")
    time.sleep(0.5)

    km2m = km * 1000
    print("hasil konversi", km, "kilometer ke m :", km2m, "m")
    time.sleep(0.5)

    km2dam = km * 100
    print("hasil konversi", km, "kilometer ke dam :", km2dam, "dam")
    time.sleep(0.5)

    km2hm = km * 10
    print("hasil konversi", km, "kilometer ke hm :", km2hm, "hm")
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