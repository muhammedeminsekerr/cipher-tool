# Kullanim ornekleri
# from cipher import caesar, vigenere

# TODO: ornek cagrilar
from cipher import caesar, vigenere

# Caesar ornekleri
print("=== Caesar ===")
print(caesar("Merhaba", 3))           # sifreler
print(caesar("Phukded", -3))          # cozer

# Vigenere ornekleri
print("=== Vigenere ===")
sifrelenmis = vigenere("Merhaba Dunya", "anahtar")
print(sifrelenmis)
print(vigenere(sifrelenmis, "anahtar", decrypt=True))  # geri cozer