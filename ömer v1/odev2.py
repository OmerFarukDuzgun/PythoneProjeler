aci1 = int(input("Birinci açiyi giriniz: "))
aci2 = int(input("İkinci açiyi giriniz: "))
aci3 = int(input("Üçüncü açiyi giriniz: "))

aci_toplami = aci1 + aci2 + aci3

if aci_toplami == 180:
    print("Bu bir üçgendir.")
else:
    print("Bu bir üçgen değildir.")
