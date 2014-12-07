import random
from myprime import MyPrime

class ElGamal:
    def bangkitkanKunci(self):
        my = MyPrime()
        a = 0
        b = 0
        p = 0
        d = 0
        
        #1. tentukan bilangan prima p dengan batas min dan max
        p = my.primeGenerate(2000,10000)

        #2. Pilih a sebagai primitive roots (yang mendekati saja)
        a = random.randint(2, p - 2)
        while(not self.isNearPrimitive(a, p, 256)):
            a = random.randint(2, p - 2)

        #3. ambil d dengan syarat 1 <= d <= p - 2
        d = random.randint(2, p-2)

        #4. Hitung b = a pangkat d mod p.
        b = my.modExp(a, d, p)

        key = ElGamalKey(a, b, p, d)
        return key

    def enkripsi(self, message, pubKeyA, pubKeyB, pubKeyP):
        my = MyPrime()
        #z dipilih acak
        z = random.randint(2, pubKeyP-1)
        C1 = my.modExp(pubKeyA, z, pubKeyP)
        C2 = my.modExp(message * my.modExp(pubKeyB, z, pubKeyP), 1, pubKeyP)

        cipherText = ElGamalCipherText(C1, C2)
        return cipherText

    def dekripsi(self, C1, C2, pubKeyP, privKeyD):
        my = MyPrime()
        plainText = my.modExp(C2 * my.modExp(C1, (pubKeyP - 1 - privKeyD), pubKeyP), 1, pubKeyP)
        return plainText

    def isNearPrimitive(self, x, n, orderneeded):
        my = MyPrime()
        i = 1
        while(i < orderneeded):
            if(my.modExp(x, i, n) <= 1):
                return False
            i = i + 1
        return True

class ElGamalKey:
    pubKeyA = 0
    pubKeyB = 0
    pubKeyP = 0
    privKeyD = 0

    def __init__(self, a, b, p, d):
        self.pubKeyA = a
        self.pubKeyB = b
        self.pubKeyP = p
        self.privKeyD = d

class ElGamalCipherText:
    cipherText1 = 0
    cipherText2 = 0
    
    def __init__(self, c1, c2):
        self.cipherText1 = c1
        self.cipherText2 = c2


#PROGRAM BEGINNING

elGamal = ElGamal()
key = elGamal.bangkitkanKunci()
print("Public Key")
pubKeyA = getattr(key, 'pubKeyA')
pubKeyB = getattr(key, 'pubKeyB')
pubKeyP = getattr(key, 'pubKeyP')
privKeyD = getattr(key, 'privKeyD')
print("a :", pubKeyA)
print("b :", pubKeyB)
print("p :", pubKeyP)
print("Private Key")
print("d :", privKeyD)

print("====================")

message = 19
print("Plain Text :", message)

cipherText = elGamal.enkripsi(message, pubKeyA, pubKeyB, pubKeyP)
C1 = getattr(cipherText, 'cipherText1')
C2 = getattr(cipherText, 'cipherText2')
print("Cipher Text 1:", C1)
print("Cipher Text 2:", C2)

plainText = elGamal.dekripsi(C1, C2, pubKeyP, privKeyD)
print("Plain Text :", plainText)

