# Cipher Encryption/Decryption System

Simple Python system for encrypting and decrypting text.

## Features
- **Caesar Cipher** - Shifts letters by a fixed number
- **Vigenère Cipher** - Uses a keyword for encryption

## Quick Start

```bash
python example.py
```

## Usage

### Caesar Cipher
```python
from cipher import CaesarCipher

cipher = CaesarCipher(shift=3)
encrypted = cipher.encrypt("Hello")     # Khoor
decrypted = cipher.decrypt("Khoor")     # Hello
```

### Vigenère Cipher
```python
from cipher import VigenèreCipher

cipher = VigenèreCipher(key="SECRET")
encrypted = cipher.encrypt("Hello")    # Zggmq
decrypted = cipher.decrypt("Zggmq")    # HELLO
```
