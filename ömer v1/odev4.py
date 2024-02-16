
urun1_fiyat = float(input("Birinci ürünün fiyatını giriniz: "))
urun2_fiyat = float(input("İkinci ürünün fiyatını giriniz: "))

toplam_fiyat = urun1_fiyat + urun2_fiyat

if toplam_fiyat <= 200:
    print("Ödenecek miktar= {} TL".format(toplam_fiyat))
else:
    indirimli_fiyat = toplam_fiyat * 0.9  # %10 indirim uygulandığını varsayalım
    print("Ödenecek miktar, indirimden sonra {} TL'dir.".format(indirimli_fiyat))