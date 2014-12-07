import random

class MyPrime:
    # men-generate bilangan prima antara batasmin dan batasmax
    def primeGenerate(self, batasMin, batasMax):
        x = random.randint(batasMin, batasMax)
        #Belum selesai
        while(not self.rabinMillerPrimeTest(x)):
            x = random.randint(batasMin, batasMax)
        return x

    # pengetesan bilangan prima menggunakan
    # algoritma miller rabin
    def rabinMillerPrimeTest(self, n):
        nmin1 = n-1
        #Belum selesai
        s = self.getSForEksponen(nmin1)
        d = nmin1 / (2 ** s)
        d = int(d)

        for i in range (0, 20):
            nmin2 = n - 2
            if(nmin2 < 2):
                nmin2 = 2
            a = random.randint(2, nmin2)
            x = self.modExp(a, d, n)
            if((x == 1) or (x == n-1)):
                continue
            for j in range (0, s - 1):
                x = (x ** 2) % n
                if(x == 1):
                    return False
                if(x == n-1):
                    continue
            return False
        return True
        
    # mencari gcd dua buah bilangan
    # menggunakan euclidean algorithm
    def gcdEuclidean(self, a, b):
        x = 0
        while(b != 0):
            x = a % b
            a = b
            b = x
        return a

    # Mencari inversi modulo
    # m adalah pemodulo
    def inversMod(self, x, m):
        i = 1
        while(((x * i) % m) != 1):
            i = i + 1
        return i

    #nilai modulo eksponensial dari x pangkat e mod n
    def modExp(self, x, e, n):
        r = 1
        for i in range(0,e):
            r = (x * r) % n
        return r

    #langkah pertama dalam algoritma miller rabin
    #adalah mencari nilai d * 2^s untuk n-1
    #method ini untuk mencari nilai s.
    def getSForEksponen(self, xmin1):
        x = 0
        while(((xmin1 % 2) == 0) and (xmin1 > 0)):
            xmin1 = xmin1 / 2
            x = x + 1
        return x

