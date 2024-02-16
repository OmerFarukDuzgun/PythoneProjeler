
islemci = input("Bilgisayarınızın işlemcisi (i7 veya farklı bir değer): ")
ram = int(input("Bilgisayarınızın RAM belleği (GB cinsinden): "))

if islemci == "i7" or ram >= 8:
    print("Kurulum uygun")
else:
    print("Kurulum uygun değil")