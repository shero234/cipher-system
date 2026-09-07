class CaesarCipher:
    def __init__(self, shift=3):
        self.shift = shift % 26
    
    def encrypt(self, text):
        result = []
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - start + self.shift) % 26
                result.append(chr(start + shifted))
            else:
                result.append(char)
        return ''.join(result)
    
    def decrypt(self, text):
        result = []
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - start - self.shift) % 26
                result.append(chr(start + shifted))
            else:
                result.append(char)
        return ''.join(result)


class VigenèreCipher:
    def __init__(self, key):
        self.key = key.upper()
    
    def encrypt(self, text):
        text = text.upper()
        result = []
        key_index = 0
        
        for char in text:
            if char.isalpha():
                shift = ord(self.key[key_index % len(self.key)]) - ord('A')
                encrypted = (ord(char) - ord('A') + shift) % 26
                result.append(chr(encrypted + ord('A')))
                key_index += 1
            else:
                result.append(char)
        
        return ''.join(result)
    
    def decrypt(self, text):
        text = text.upper()
        result = []
        key_index = 0
        
        for char in text:
            if char.isalpha():
                shift = ord(self.key[key_index % len(self.key)]) - ord('A')
                decrypted = (ord(char) - ord('A') - shift) % 26
                result.append(chr(decrypted + ord('A')))
                key_index += 1
            else:
                result.append(char)
        
        return ''.join(result)
