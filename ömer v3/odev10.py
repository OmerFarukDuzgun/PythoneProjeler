
tek_sayilar = [sayi for sayi in range(5, 16) if sayi % 2 != 0]
cift_sayilar = [sayi for sayi in range(6, 17) if sayi % 2 == 0]

liste_ic_ice = [tek_sayilar, cift_sayilar]

# a) İç içe liste oluşturma
liste_ic_ice.append(cift_sayilar)

# b) Ekran çıktısı olarak 7 14 üreten kod
print(liste_ic_ice[0][2], liste_ic_ice[2][1])

# c) Ekrana sırasıyla çift sayılar listesinden 10 ve 12; tek sayılar listesinden 13 yazdırma
print(liste_ic_ice[1][4], liste_ic_ice[0][8], liste_ic_ice[0][6])
