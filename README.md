# Cipher Tool

Caesar ve Vigenère şifreleme/şifre çözme aracı.

## Özellikler
- Caesar cipher (kaydırmalı şifreleme)
- Vigenère cipher (anahtar kelimeli şifreleme)
- Büyük/küçük harf korunur, harf olmayan karakterler değişmez

## Kullanım
```python
from cipher import caesar, vigenere

caesar("Merhaba", 3)        # şifreler
caesar("Phukded", -3)       # çözer
vigenere("Merhaba", "key")  # şifreler
```

## Nasıl Çalışır
Caesar her harfi alfabede `shift` kadar kaydırır, modulo 26 ile
alfabe sınırında başa döner. Vigenère sabit shift yerine anahtar
kelimeden türeyen değişken shift kullanır.
