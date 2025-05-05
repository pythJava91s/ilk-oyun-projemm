import random

print("Sayı Tahmin Oyununa Hoş Geldin!")
sayi = random.randint(1, 10)
can = 3

while can > 0:
    tahmin = int(input("1 ile 10 arasında bir sayı tahmin et: "))
    if tahmin == sayi:
        print("Tebrikler! Doğru tahmin!")
        break
    else:
        print("Yanlış tahmin.")
        can -= 1

if can == 0:
    print(f"Kaybettin! Doğru sayı: {sayi}")
