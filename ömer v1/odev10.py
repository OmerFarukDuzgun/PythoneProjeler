
saat_suresi = int(input("Otoparkta kalınan saat süresini giriniz: "))

if saat_suresi <= 1:
    ucret = 5
elif saat_suresi <= 5:
    ucret = 5 + (saat_suresi - 1) * 4
else:
    ucret = 5 + 4 * 4 + (saat_suresi - 5) * 3

print("Ödenecek miktar:", ucret, "TL")