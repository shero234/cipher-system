from cipher import CaesarCipher, VigenèreCipher

print("\n" + "="*50)
print("   CAESAR & VIGENÈRE CIPHER SYSTEM")
print("="*50)

# Caesar Cipher Example
print("\n--- CAESAR CIPHER ---")
caesar = CaesarCipher(shift=3)
text = "Hello World"
encrypted = caesar.encrypt(text)
decrypted = caesar.decrypt(encrypted)

print(f"Shift: 3")
print(f"Original:  {text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

# Vigenère Cipher Example
print("\n--- VIGENÈRE CIPHER ---")
vigenere = VigenèreCipher(key="SECRET")
text = "Hello World"
encrypted = vigenere.encrypt(text)
decrypted = vigenere.decrypt(encrypted)

print(f"Key: SECRET")
print(f"Original:  {text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

print("\n" + "="*50)
