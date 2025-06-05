import os
os.system("pip install random")
os.system("pip install string")

import random
import string

uzunluk = int(input("Şifreniz kaç karakter olsun? "))
karakterler = string.ascii_letters + string.digits + string.punctuation

sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
print("Güçlü Şifreniz:", sifre)
