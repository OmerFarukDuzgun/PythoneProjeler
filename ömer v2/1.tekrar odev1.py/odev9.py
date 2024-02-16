count = 0
total = 0

while True:
 num = int(input("Bir sayi girin: "))
 total += num
 count += 1
 if num == 1:
    break
print("Girilen sayilarin ortalamasi:", total/count)
