import os
os.system("pip install random")
os.system("pip install time")

import time
import random

kelimeler = ["python", "geliştirici", "program", "kodlama", "klavye"]
kelime = random.choice(kelimeler)
print("Yazman gereken kelime:", kelime)
start = time.time()
giris = input("Hemen yaz ve Enter'a bas: ")
end = time.time()
if giris == kelime:
    print("Doğru! Süreniz:", round(end - start, 2), "saniye")
else:
    print("Yanlış yazdın!")
