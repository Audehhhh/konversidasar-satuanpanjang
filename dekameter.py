print("-------------------------------------------------------")
print("----------------- KONVERSI SATUAN DAM ------------------")
print("-------------------------------------------------------")

dam = float(input("masukan satuan dam :"))
ulang = dam

dam2mm = (dam * 10000) 
print("hasil konversi ke mm :", dam2mm, "mm")

dam2cm = (dam * 1000)
print("hasil konversi ke cm :", dam2cm, "cm")

dam2dm = (dam * 100)
print("hasil konversi ke dm :", dam2dm, "dm")

dam2m = (dam * 10)
print("hasil konversi ke m :", dam2m, "m")

dam2hm = (dam / 10)
print("hasil konversi ke hm :", dam2hm, "hm")

dam2km = (dam / 100)
print("hasil konversi ke km :", dam2km, "km")
