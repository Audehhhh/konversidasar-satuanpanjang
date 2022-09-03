import time 


ulang = True
while (ulang):
    print('')
    print("-------------------------------------------------------")
    print("----------------- KONVERSI SATUAN M -------------------")
    print("-------------------------------------------------------")

    print('')
    print('AI: silahkan masukan nilai yang ingin dikonversikan')
    m = float(input("user: "))

    print('')
    print('======================== Hasil ========================')
    time.sleep(1)

    print('')
    m2mm = (m * 1000) 
    print("hasil konversi", m, "meter ke mm :", m2mm, "mm")
    time.sleep(0.5)

    m2cm = (m * 100)
    print("hasil konversi", m, "meter ke cm :", m2cm, "cm")
    time.sleep(0.5)

    m2dm = (m * 10)
    print("hasil konversi", m, "meter ke dm :", m2dm, "dm")
    time.sleep(0.5)

    m2dam = (m / 10)
    print("hasil konversi", m, "meter ke dam :", m2dam, "dam")
    time.sleep(0.5)

    m2hm = (m / 100)
    print("hasil konversi", m, "meter ke hm :", m2hm, "hm")
    time.sleep(0.5)

    m2km = (m / 1000)
    print("hasil konversi", m, "meter ke km :", m2km, "km")
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