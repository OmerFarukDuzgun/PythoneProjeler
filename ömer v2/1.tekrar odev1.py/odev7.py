s1=int(input("1.sayiyi giriniz:"))
s2=int(input("2.sayiyi giriniz:"))

toplam=0
i=s1
while i <= s2:
    toplam+=i
    i+=1

ortalama =toplam/(s2-s1+1)
print("Sayilarin ortalamasi",ortalama)
