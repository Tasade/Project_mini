import os
os.system("pip install random")

import random

oduller = ["100 TL", "Bir çikolata", "Bir kitap", "Ücretsiz sinema bileti", "Bir pizza", "Hiçbir şey :("]

input("Çarkıfelek için Enter'a basın...")
sonuc = random.choice(oduller)
print("Tebrikler! Kazandığınız ödül:", sonuc)
