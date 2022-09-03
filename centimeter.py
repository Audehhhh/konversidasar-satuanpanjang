import time


ulang = True
while (ulang):
    print('')
    print("-------------------------------------------------------")
    print("----------------- KONVERSI SATUAN CM ------------------")
    print("-------------------------------------------------------")

    print('')
    print('AI: silahkan masukan nilai yang ingin dikonversikan')
    cm = float(input("user: "))

    print('')
    print('======================== Hasil ========================')
    time.sleep(1)

    print('')
    cm2mm = (cm * 10) 
    print("hasil konversi", cm, "centimeter ke mm :", cm2mm, "mm")
    time.sleep(0.5)

    cm2dm = (cm / 10)
    print("hasil konversi", cm, "centimeter ke dm :", cm2dm, "dm")
    time.sleep(0.5)

    cm2m = (cm / 100)
    print("hasil konversi", cm, "centimeter ke m :", cm2m, "m")
    time.sleep(0.5)

    cm2dam = (cm / 1000)
    print("hasil konversi", cm, "centimeter ke dam :", cm2dam, "dam")
    time.sleep(0.5)

    cm2hm = (cm / 10000)
    print("hasil konversi", cm, "centimeter ke hm :", cm2hm, "hm")
    time.sleep(0.5)

    cm2km = (cm / 100000)
    print("hasil konversi", cm, "centimeter ke km :", cm2km, "km")
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