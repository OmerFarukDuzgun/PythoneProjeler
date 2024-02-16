bütçe = float(input("Bütçenizi giriniz: "))
toplam_tutar = 0

while True:
    seçim = input("Almak istediğiniz meyveyi seçin:\n"
                  "Elma = 10 TL\n"
                  "Ayva = 15 TL\n"
                  "Karpuz = 5 TL\n"
                  "Çikiş ve toplam tutar için 'q' ye basin\n")

    if seçim == "q":
        print("Toplam tutar:", toplam_tutar)
        break
    else:
        if bütçe <= 0:
            print("Paraniz yok!")
            break

        if seçim == "elma":
            fiyat = 10
        elif seçim == "Ayva":
            fiyat = 15
        elif seçim == "Karpuz":
            fiyat = 5
        else:
            print("Geçersiz seçim! Lütfen geçerli bir meyve seçin.")
            continue

        if bütçe < fiyat:
            print("Yetersiz bütçe! Başka bir meyve seçin.")
        else:
            bütçe -= fiyat
            toplam_tutar += fiyat
            print(seçim, "satin alindi. Paranizdan" ,fiyat ,"TL düşüldü. Kalan bütçe:",bütçe,"TL")