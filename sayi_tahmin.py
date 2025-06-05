import os
os.system("pip install random")

import random

sayi = random.randint(1, 100)
tahmin = -1

while tahmin != sayi:
    tahmin = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
    if tahmin < sayi:
        print("Daha büyük bir sayı girin.")
    elif tahmin > sayi:
        print("Daha küçük bir sayı girin.")
    else:
        print("Tebrikler, doğru tahmin!")
