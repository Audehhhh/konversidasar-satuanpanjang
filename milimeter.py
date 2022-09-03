import time


ulang = True
while(ulang):
    print('')
    print("-------------------------------------------------------")
    print("----------------- KONVERSI SATUAN MM ------------------")
    print("-------------------------------------------------------")

    print('')
    print('AI: silahkan masukan nilai yang ingin dikonversikan')
    mm = float(input("user: "))

    print('')
    print('======================== Hasil ========================')
    time.sleep(1)

    print('')
    mm2cm = mm / 10
    print("hasil konversi", mm, "milimeter ke cm :", mm2cm, "km")
    time.sleep(0.5)

    mm2dm = mm / 100
    print("hasil konversi", mm, "milimeter ke dm :", mm2dm, "dm")
    time.sleep(0.5)

    mm2m = mm / 1000
    print("hasil konversi", mm, "milimeter ke m :", mm2m, "m")
    time.sleep(0.5)

    mm2dam = mm / 10000
    print("hasil konversi", mm, "milimeter ke dam :", mm2dam, "dam")
    time.sleep(0.5)

    mm2hm = mm / 100000
    print("hasil konversi", mm, "milimeter ke hm :", mm2hm, "hm")
    time.sleep(0.5)

    mm2km = mm / 1000000
    print("hasil konversi", mm, "milimeter ke km :", mm2km, "km")
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