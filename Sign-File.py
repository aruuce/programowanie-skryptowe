from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

def sign(inputs):
    privkey=RSA.generate(2048)
    
    with open (inputs, 'rb') as file:
        text=file.read()

    hash256=SHA256.new()
    hash256.update(text)

    signature=PKCS1_v1_5.new(privkey).sign(hash256)
    print(signature)

if __name__=='__main__':
    inputs=input('podaj plik do podpisu: ')
    sign(inputs)