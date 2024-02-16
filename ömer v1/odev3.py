bagaj_agirligi = int(input("Bagaj ağirligini giriniz (kg): "))

if bagaj_agirligi <= 20:
    print("Herhangi bir ücret ödemeniz gerekmiyor.")
else:
    ek_ucret = (bagaj_agirligi - 20) * 10
    print("Fazla bagaj için", ek_ucret, "TL ödemelisiniz.")
