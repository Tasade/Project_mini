import os
os.system("pip install random")

import random

kelimeler = ["elma", "karpuz", "araba", "okul", "kitap", "masa"]
kelime = random.choice(kelimeler)
tahminler = []
hak = 6

print("== Adam Asmaca Oyununa Hoşgeldin! ==")

while hak > 0:
    gizli = ""
    for harf in kelime:
        if harf in tahminler:
            gizli += harf
        else:
            gizli += "_"
    print("Kelime: ", gizli)

    if gizli == kelime:
        print("Tebrikler, kazandın!")
        break

    tahmin = input("Bir harf tahmin et: ")
    if tahmin in tahminler:
        print("Bu harfi zaten denedin.")
        continue
    tahminler.append(tahmin)
    if tahmin not in kelime:
        hak -= 1
        print(f"Yanlış! Kalan hakkın: {hak}")

    if hak == 0:
        print(f"Kaybettin. Doğru kelime: {kelime}")
