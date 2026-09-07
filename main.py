#!/usr/bin/env python3
from cipher import CaesarCipher, VigenèreCipher

def caesar_menu():
    """Interactive Caesar Cipher menu"""
    print("\n" + "="*50)
    print("      CAESAR CIPHER")
    print("="*50)
    
    try:
        shift = int(input("\nEnter shift value (1-25): "))
        if shift < 1 or shift > 25:
            print("❌ Shift must be between 1 and 25!")
            return
        
        cipher = CaesarCipher(shift=shift)
        
        print("\n1. Encrypt")
        print("2. Decrypt")
        choice = input("Select (1/2): ").strip()
        
        if choice == '1':
            text = input("\nEnter text to encrypt: ")
            result = cipher.encrypt(text)
            print(f"\n✓ Encrypted: {result}")
        elif choice == '2':
            text = input("\nEnter text to decrypt: ")
            result = cipher.decrypt(text)
            print(f"\n✓ Decrypted: {result}")
        else:
            print("❌ Invalid option!")
    except ValueError:
        print("❌ Please enter a valid number!")

def vigenere_menu():
    """Interactive Vigenère Cipher menu"""
    print("\n" + "="*50)
    print("      VIGENÈRE CIPHER")
    print("="*50)
    
    try:
        key = input("\nEnter cipher key (letters only): ").strip().upper()
        
        if not key or not key.isalpha():
            print("❌ Key must contain only letters!")
            return
        
        cipher = VigenèreCipher(key=key)
        
        print("\n1. Encrypt")
        print("2. Decrypt")
        choice = input("Select (1/2): ").strip()
        
        if choice == '1':
            text = input("\nEnter text to encrypt: ")
            result = cipher.encrypt(text)
            print(f"\n✓ Encrypted: {result}")
        elif choice == '2':
            text = input("\nEnter text to decrypt: ")
            result = cipher.decrypt(text)
            print(f"\n✓ Decrypted: {result}")
        else:
            print("❌ Invalid option!")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Main menu"""
    while True:
        print("\n" + "="*50)
        print("  CIPHER ENCRYPTION/DECRYPTION SYSTEM")
        print("="*50)
        print("\n1. Caesar Cipher")
        print("2. Vigenère Cipher")
        print("3. Exit")
        
        choice = input("\nSelect option (1-3): ").strip()
        
        if choice == '1':
            caesar_menu()
        elif choice == '2':
            vigenere_menu()
        elif choice == '3':
            print("\n👋 Thank you! Goodbye!\n")
            break
        else:
            print("❌ Invalid option!")

if __name__ == "__main__":
    main()
