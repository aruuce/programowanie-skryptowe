from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def encrypt(inputs, output):
    key=get_random_bytes(32)
    cipher=AES.new(key, AES.MODE_CBC)
    
    with open (inputs, 'rb') as file:
        text=file.read()
    
    padtext=pad(text, AES.block_size)
    ciphertext=cipher.encrypt(padtext)

    with open (output, 'wb') as file:
        file.write(ciphertext)
    
if __name__=='__main__':
    inputs=input('podaj nazwe pliku do zaszyfrowania: ')
    output='encrypted_'+inputs
    encrypt(inputs, output)