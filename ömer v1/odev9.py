
sicaklik = float(input("Hava sıcaklığını giriniz: "))

if sicaklik <= 5:
    print("Soğuk")
elif sicaklik >= 6 and sicaklik <= 14:
    print("Ilık")
else:
    print("Sıcak")