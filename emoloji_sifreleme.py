harfler = "abcdefghijklmnopqrstuvwxyz"
emojiler = ["😀","😁","😂","🤣","😃","😄","😅","😆","😉","😊","😋","😎","😍",
            "😘","🤗","🤔","😐","😑","😶","🙄","😏","😣","😥","😮","🤐","😯"]

metin = input("Şifrelemek istediğiniz metni girin: ").lower()
sonuc = ""
for harf in metin:
    if harf in harfler:
        sonuc += emojiler[harfler.index(harf)]
    else:
        sonuc += harf
print("Emojili metin:", sonuc)
