# 🔐 Cipher Tool

A Python implementation of Caesar and Vigenère classical encryption algorithms.

## 📌 What Does It Do?

This tool implements two classical cryptography algorithms:

- **Caesar Cipher:** Shifts each letter by a fixed number in the alphabet. Use a positive `shift` to encrypt, negative to decrypt.
- **Vigenère Cipher:** Uses a keyword to generate a different shift value for each letter. Significantly stronger than Caesar.

## 📁 File Structure

```
cipher-tool/
├── cipher.py       # Core algorithm functions
├── examples.py     # Usage examples
└── README.md       # Documentation
```

## 🚀 Usage

### Run directly:
```bash
python cipher.py
python examples.py
```

### Import and use:
```python
from cipher import caesar, vigenere

# Caesar - Encrypt
encrypted = caesar("Hello World", 3)
print(encrypted)   # Khoor Zruog

# Caesar - Decrypt (negative shift)
decrypted = caesar("Khoor Zruog", -3)
print(decrypted)   # Hello World

# Vigenere - Encrypt
encrypted = vigenere("Hello World", "key")
print(encrypted)

# Vigenere - Decrypt
decrypted = vigenere(encrypted, "key", decrypt=True)
print(decrypted)   # Hello World
```

## ⚙️ How It Works

### Caesar
Shifts each letter by a fixed amount using modular arithmetic to wrap around the alphabet:
```
encrypted = (char - base + shift) % 26 + base
```

### Vigenère
Uses each character of the keyword as a shift value, cycling through when exhausted:
```
shift = key[i % len(key)]
encrypted = (char - base + shift) % 26 + base
```

Uppercase/lowercase is preserved. Non-alphabetic characters (spaces, digits) remain unchanged.

## 🛠️ Requirements

Python 3.x only — no external libraries required.

## 📚 Cryptography Notes

- Caesar cipher is trivially broken via frequency analysis (only 25 possible keys)
- Vigenère can be broken with the Kasiski test but is much stronger on short texts
- Neither is used in modern cryptography; they serve educational and historical purposes

## 👤 Author

**Muhammed Emin Şeker**  
Computer Engineering Student — RTEÜ  
[LinkedIn](https://www.linkedin.com/in/muhammed-emin-%C5%9Feker-b94937333/) | [GitHub](https://github.com/muhammedeminsekerr)
