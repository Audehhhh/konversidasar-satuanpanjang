import time


ulang = True
while (ulang):
    print("")
    print("-------------------------------------------------------")
    print("----------------- KONVERSI SATUAN DM ------------------")
    print("-------------------------------------------------------")

    print('')
    print('AI: silahkan masukan nilai yang ingin dikonversikan')
    dm = float(input("user: "))

    print('')
    print('=========================Hasil=========================')
    time.sleep(1)

    print('')
    dm2mm = (dm * 100) 
    print("hasil konversi", dm, "desimeter ke mm :", dm2mm, "mm")
    time.sleep(0.5)

    dm2cm = (dm * 10)
    print("hasil konversi", dm, "desimeter ke cm :", dm2cm, "cm")
    time.sleep(0.5)

    dm2m = (dm / 10)
    print("hasil konversi", dm, "desimeter ke m :", dm2m, "m")
    time.sleep(0.5)

    dm2dam = (dm / 100)
    print("hasil konversi", dm, "desimeter ke dam :", dm2dam, "dam")
    time.sleep(0.5)

    dm2hm = (dm / 1000)
    print("hasil konversi", dm, "desimeter ke hm :", dm2hm, "hm")
    time.sleep(0.5)

    dm2km = (dm / 10000)
    print("hasil konversi", dm, "desimeter ke km :", dm2km, "km")
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