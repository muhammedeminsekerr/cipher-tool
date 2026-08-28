# 🔐 Cipher Tool

Caesar ve Vigenère şifreleme algoritmalarının Python implementasyonu.

## 📌 Ne İşe Yarar?

Bu araç iki klasik kriptografi algoritmasını uygular:

- **Caesar Cipher:** Her harfi alfabede sabit sayıda kaydırır. Şifreleme için `shift` değeri pozitif, çözme için negatif verilir.
- **Vigenère Cipher:** Anahtar kelime kullanarak her harf için farklı shift değeri üretir. Caesar'dan çok daha güvenlidir.

## 📁 Dosya Yapısı

```
cipher-tool/
├── cipher.py       # Ana algoritma fonksiyonları
├── examples.py     # Kullanım örnekleri
└── README.md       # Bu dosya
```

## 🚀 Kullanım

### Doğrudan çalıştır:
```bash
python cipher.py
python examples.py
```

### Import ederek kullan:
```python
from cipher import caesar, vigenere

# Caesar - Şifreleme
sifre = caesar("Merhaba Dunya", 3)
print(sifre)   # Phukded Gxqbd

# Caesar - Çözme (negatif shift)
metin = caesar("Phukded Gxqbd", -3)
print(metin)   # Merhaba Dunya

# Vigenere - Şifreleme
sifre = vigenere("Merhaba Dunya", "anahtar")
print(sifre)

# Vigenere - Çözme
metin = vigenere(sifre, "anahtar", decrypt=True)
print(metin)   # Merhaba Dunya
```

## ⚙️ Nasıl Çalışır?

### Caesar
Her harfi 0-25 aralığına indirip shift ekler, `% 26` ile alfabenin dışına taşmayı önler:
```
şifreli = (harf - base + shift) % 26 + base
```

### Vigenère
Anahtar kelimenin her harfini shift değeri olarak kullanır, kelime bitince başa döner:
```
shift = anahtar[i % len(anahtar)]
şifreli = (harf - base + shift) % 26 + base
```

Büyük/küçük harf korunur. Harf olmayan karakterler (boşluk, rakam) değişmez.

## 🛠️ Gereksinimler

Sadece Python 3.x — harici kütüphane gerekmez.

## 📚 Kriptografi Notları

- Caesar cipher frekans analizi ile kolayca kırılır (sadece 25 olasılık vardır)
- Vigenère, Kasiski testi ile kırılabilir ancak kısa metinlerde güçlüdür
- Modern kriptografide kullanılmazlar; eğitim ve tarihsel öneme sahiptirler

## 👤 Yazar

**Muhammed Emin Şeker**  
Bilgisayar Mühendisliği Öğrencisi — RTEÜ  
[LinkedIn](https://www.linkedin.com/in/muhammed-emin-%C5%9Feker-b94937333/) | [GitHub](https://github.com/muhammedeminsekerr)
