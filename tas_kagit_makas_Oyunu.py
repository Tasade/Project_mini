import os
os.system("pip install random")

import random

secenekler = ["taş", "kağıt", "makas"]
skor = {"Sen": 0, "Bilgisayar": 0}

for i in range(3):  # 3 raund
    bilgisayar = random.choice(secenekler)
    sen = input("Taş, kağıt veya makas?: ").lower()

    print(f"Bilgisayarın Seçimi: {bilgisayar}")

    if sen == bilgisayar:
        print("Berabere!")
    elif (sen == "taş" and bilgisayar == "makas") or \
         (sen == "kağıt" and bilgisayar == "taş") or \
         (sen == "makas" and bilgisayar == "kağıt"):
        print("Kazandın!")
        skor["Sen"] += 1
    else:
        print("Bilgisayar kazandı!")
        skor["Bilgisayar"] += 1

print("Skorlar:", skor)
