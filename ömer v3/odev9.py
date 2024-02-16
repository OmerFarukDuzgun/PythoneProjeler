
sayilar = [35, 26, 81, 64]

# a) Listeyi büyükten küçüğe doğru sıralama
sayilar.sort(reverse=True)
print("Sıralanmış liste:", sayilar)

# b) Listeyi tersten yazdırma
tersten_sayilar = sayilar[::-1]
print("Tersten yazılmış liste:", tersten_sayilar)

# c) Listede kaç tane 26 elemanı olduğunu bulma
adet_26 = sayilar.count(26)
print("Listede 26 sayısı", adet_26, "kez geçiyor.")

# ç) Listedeki 81 sayısını silme
sayilar.remove(81)
print("81 sayısı listeden silindi. Yeni liste:", sayilar)

# d) Listenin tüm elemanlarını silme
sayilar.clear()
print("Liste tamamen boşaltıldı. Yeni liste:", sayilar)

# e) 64 elemanının indeksini bulma
indeks_64 = tersten_sayilar.index(64)
print("64 sayısının indeksi:", indeks_64)

# f) Listeyi ondalikli_sayilar ile birleştirme
ondalikli_sayilar = [1.4, 6.8]
birlesik_liste = sayilar + ondalikli_sayilar
print("Birleştirilmiş liste:", birlesik_liste)