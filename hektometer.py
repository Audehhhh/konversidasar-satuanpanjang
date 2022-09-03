import time


ulang = True
while (ulang):
    print('')
    print("-------------------------------------------------------")
    print("----------------- KONVERSI SATUAN HM ------------------")
    print("-------------------------------------------------------")

    print('')
    print('AI: silahkan masukan nilai yang ingin dikonversikan')
    hm = float(input("user: "))

    print('')
    print('======================== Hasil ========================')
    time.sleep(1)

    print('')
    hm2mm = (hm * 100000) 
    print("hasil konversi", hm, "hektometer ke mm :", hm2mm, "mm")
    time.sleep(0.5)

    hm2cm = (hm * 10000)
    print("hasil konversi", hm, "hektometer ke cm :", hm2cm, "cm")
    time.sleep(0.5)

    hm2dm = (hm * 1000)
    print("hasil konversi", hm, "hektometer ke dm :", hm2dm, "dm")
    time.sleep(0.5)

    hm2m = (hm * 100)
    print("hasil konversi", hm, "hektometer ke m :", hm2m, "m")
    time.sleep(0.5)

    hm2dam = (hm * 10)
    print("hasil konversi", hm, "hektometer ke dam :", hm2dam, "dam")
    time.sleep(0.5)

    hm2km = (hm / 10)
    print("hasil konversi", hm, "hektometer ke km :", hm2km, "km")
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