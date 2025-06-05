import os
os.system("pip install random")


import random
while True:
    input("Zar atmak için Enter'a basın...")
    print("Gelen sayı:", random.randint(1, 6))
    devam = input("Tekrar atmak ister misin? (e/h): ")
    if devam.lower() != 'e':
        break
