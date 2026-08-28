# Cipher Tool
# Caesar ve Vigenere sifreleme araci

def caesar(text, shift):
    # TODO: her karakteri dolas, harfse kaydir, degilse dokunma
    pass


def vigenere(text, key, decrypt=False):
    # TODO: anahtar kelimeden turetilen degisken shift ile sifrele/coz
    pass


if __name__ == "__main__":
    # TODO: test ciktilari
    pass
def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result