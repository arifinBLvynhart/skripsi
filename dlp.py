from myprime import MyPrime

class DLP:
    # dengan algoritma Silver-Pohlig-Hellman
    def shpDiscreteLog(self, base, log, prime):
        myPrime = MyPrime()
        
        primeMin1 = prime - 1

        # temukan faktor distinct primes
        distinctPrimes = self.findDistinctPrimes(primeMin1)
        pj = getattr(distinctPrimes, "pj")
        aj = getattr(distinctPrimes, "aj")
        B = log
        Bderet = []
        #ini adalah B[0]
        Bderet.append(B)
        b = []
        j = 0
        ej = []
        ejmcrt = []
        ejM = {}
                
        # hitung nilai e
        # untuk setiap pj
        for item in pj:
            j = j + 1
            # hitung b0
            # temukan k
            k = 0
            
            pangkatBase = 0
            pangkatB0 = 0
            # pastikan terlebih dahulu bahwa pangkat masing-masing
            # sisi (alpha dan BO) berupa bilangan bulat
            tem = ((prime - 1) * k) % item
            if (tem == 0):
                pangkatBase = (prime - 1) * k // item
            else:
                # jika hasil pembagian tidak 0
                # maka harus menemukan bilangan x yang
                # kongruen terhadap ((prime - 1) * k) % item
                x = 1
                a = (prime-1) * k % prime
                b = (item * x) % prime
                # selama masih belum kongruen, temukan x yang memenuhi
                while(a != b):
                    x = x + 1
                    b = (item * x) % prime
                # setelah ditemukan x yang tepat, maka pangkatBase adalah x
                pangkatBase = x
                
            # sama dengan di atas, jika hasil pembagian tidak bulat
            tem = (prime - 1) % item
            if (tem == 0):
                pangkatB0 = (prime - 1) // item
            else:
                x = 1
                a = (prime-1) % prime
                b = (item * x) % prime
                while(a != b):
                    x = x + 1
                    b = (item * x) % prime
                pangkatB0 = x

            # pada tahap ini, pangkat alpha dan B0 telah ditemukan
            # selanjutnya lakukan iterasi sampai didapati k yang tepat
            m = myPrime.modExp(base, pangkatBase, prime)
            n = myPrime.modExp(Bderet[0], pangkatB0, prime)

            while(m != n):
                k = k + 1

                # pastikan terlebih dahulu bahwa pangkat masing-masing
                # sisi (alpha dan BO) berupa bilangan bulat
                tem = ((prime - 1) * k) % item
                if (tem == 0):
                    pangkatBase = (prime - 1) * k // item
                else:
                    # jika hasil pembagian tidak 0
                    # maka harus menemukan bilangan x yang
                    # kongruen terhadap ((prime - 1) * k) % item
                    x = 1
                    p = (prime-1) * k % prime
                    q = (item * x) % prime
                    # selama masih belum kongruen, temukan x yang memenuhi
                    while(p != q):
                        x = x + 1
                        q = (item * x) % prime
                    # setelah ditemukan x yang tepat, maka pangkatBase adalah x
                    pangkatBase = x
                m = myPrime.modExp(base, pangkatBase, prime)

            # ini adalah b0    
            b.append(k)
            
            # =============================================
            # sampai pada tahap ini, b0 = k sudah ditemukan
            # selanjutnya, kita akan mencari nilai bi
            # untuk setiap i = 1, 2, .. ,aj - 1
            for i in range(1, aj[item]):
                # tentukan nilai Bi = B * (base ^ -(sigma k=0 hingga i-1 ((bk^j) ^ (pj^k))))
                # iterasi berikut untuk menghitung pangkat base (dalam bentuk sigma)
                sigma = 0
                for k in range(0, i):
                    sigma = sigma + (b[k] ** j) * (item ** k)

                # sigma akan bernilai dikalikan dengan minus 1, yang berarti minus
                # karena pangkat bernilai minus, maka yang harus dilakukan adalah
                # mencari inversi modulo, namun terlebih dahulu lihat nilai pangkat bukan 1
                # maka jadikan setara dengan 1, lalu cari inversi modulonya.
                tempBase = base
                if(sigma != 1):
                    tempBase = base ** sigma
                    sigma = -1
                invTempBase = myPrime.inversMod(tempBase, prime)
                #ini adalah Bderet[i]
                Bderet.append((B * invTempBase) % prime)
                # pada tahap ini nilai Bi sudah ditemukan, maka lakukan iterasi untuk mencari nilai
                # k yang memenuhi persamaan Bi ^ ((p-1) / (pj ^ (i+1))) kongruen base ^ ((p-1) * (bi^j) / pj) (mod prime)

                # lakukan hal yang sama seperti ketika mencari b0
                pangkatBi = 0
                pangkatBase = 0
                tem = ((prime - 1) * k) % item
                if (tem == 0):
                    pangkatBase = (prime - 1) * k // item
                else:
                    x = 1
                    p = (prime-1) * k % prime
                    q = (item * x) % prime
                    while(p != q):
                        x = x + 1
                        q = (item * x) % prime
                    pangkatBase = x
                
                tem = (prime - 1) % (item ** (i + 1))
                if (tem == 0):
                    pangkatBi = (prime - 1) // (item ** (i + 1))
                else:
                    x = 1
                    p = (prime - 1) % prime
                    q = ((item ** (i + 1)) * x) % prime
                    while(p != q):
                        x = x + 1
                        q = ((item ** (i + 1)) * x) % prime
                    pangkatBase = x

                m = myPrime.modExp(base, pangkatBase, prime)
                n = myPrime.modExp(Bderet[i], pangkatBi, prime)

                while(m != n):
                    tem = ((prime - 1) * k) % item
                    if (tem == 0):
                        pangkatBase = ((prime - 1) * k) // item
                    else:
                        x = 1
                        p = ((prime-1) * k) % prime
                        q = (item * x) % prime
                        while(p != q):
                            x = x + 1
                            q = (item * x) % prime
                        pangkatBase = x
                    m = myPrime.modExp(base, pangkatBase, prime)

                # ini adalah bi
                b.append(k)

            # ===================
            # sampai disini, telah didapat deret b[i] untuk pj
            # selanjutnya kita akan mencari nilai e untuk basis pj
            # dengan menjumlahkan semua deret b[i]

            tempe = 0
            for i in range(0, aj[item]):
                tempe = tempe + (b[i] ** j) * (item ** i)
                
            bentar = tempe % (item ** aj[item])
            # ini adalah ej[j]
            ej.append(bentar)
            ejmcrt.append(item ** aj[item])
            # ini adalah pemodulo dari ej
            ejM[bentar] = (item ** aj[item])
            x = self.chineseRT(ej, ejmcrt)
            x = x % self.lcm(ejmcrt)
            reval = HasilSHP(ej, ejM, x)
        return reval

    # mencari faktorisasi distinct primes
    def findDistinctPrimes(self, primeMin1):
        # pj dan aj akan diisi pada atribut reval
        pj = [] # list
        aj = {} # dictionary
        
        # metode trivial
        pembagi = 2
        eksponen = 0

        # coba pembagian 2, selanjutnya dimulai dari 3
        # dengan increment 2
        if(((primeMin1 % pembagi) == 0) and (pembagi < (primeMin1 / 2))):
            pj.append(pembagi)
            while((primeMin1 % pembagi) == 0):
                primeMin1 = primeMin1 // pembagi
                eksponen = eksponen + 1
            aj[pembagi] = eksponen

        # mulai dari sini pembagi dimulai dari 3
        pembagi = pembagi + 1

        # reset eksponen
        eksponen = 0

        # selama pembagi masih < primeMin1 / 2
        while(pembagi < (primeMin1 / 2)):
            while((primeMin1 % pembagi) == 0):
                primeMin1 = primeMin1 // pembagi
                eksponen = eksponen + 1
            if(eksponen > 0):
                pj.append(pembagi)
                aj[pembagi] = eksponen
                #restart eksponen
                eksponen = 0

            # setelah tidak bisa dibagi lagi,
            # pembagi dinaikkan valuenya dengan range 2
            pembagi = pembagi + 2

        if(primeMin1 > 1):
            pj.append(primeMin1)
            aj[primeMin1] = 1
        
        reval = DistinctPrimes()
        # Set attribute
        setattr(reval, 'pj', pj)
        setattr(reval, 'aj', aj)
        return reval

    def chineseRT(self, listA, listMod):
        myPrime = MyPrime()
        M = 1

        # hitung LCM dari setiap pemodulo
        # BELOM DISINI

        # hitung nilai M
        for i in range(len(listMod)):
            M = M * listMod[i]

        listM = []
        # hitung nilai M/m untuk setiap nilai m
        for i in range(len(listMod)):
            temp = M // listMod[i]
            listM.append(temp)

        # hitung inversi modulo
        listInvM = []
        for i in range(len(listM)):
            temp = myPrime.inversMod(listM[i], listMod[i])
            listInvM.append(temp)

        # hitung x
        x = 0
        for i in range(len(listA)):
            temp = listA[i] * listM[i] * listInvM[i]
            x = x + temp
        
        return x

    def lcm(self, listNumber):
        a = 1
        b = 1
        for item in listNumber:
            b = a * item
            a = b // self.gcdEuclidean(a, item)
        return a

    # mencari gcd dua buah bilangan
    # menggunakan euclidean algorithm
    def gcdEuclidean(self, a, b):
        x = 0
        while(b != 0):
            x = a % b
            a = b
            b = x
        return a

class DistinctPrimes:
    pj = [] #basis
    aj = {} #eksponen (pangkat)

    def showInfo(self):
        print("The Distinct Primes")
        for item in self.pj:
            print(item, "^", self.aj[item])

    def hitungProduct(self):
        hasil = 1
        for item in self.pj:
            hasil = hasil * (item * self.aj[item])
        return hasil

class HasilSHP:
    ej = []
    ejM = {}
    x = 0

    def __init__(self, initej, initejM, initx):
        self.ej = initej
        self.ejM = initejM
        self.x = initx
        
    def showInfo(self):
        print("Hasil SHP")
        for item in self.ej:
            print(item, "mod", self.ejM[item])
        print("x:", self.x)

dlp = DLP()
prime = 73
base = 5
log = 68
mylist = dlp.shpDiscreteLog(base, log, prime)
ej = getattr(mylist, "ej")
ejM = getattr(mylist, "ejM")
mylist.showInfo()
'''print("==========")
print("Ngetes CRT")
A = [2,3,2]
B = [3,5,7]
x = dlp.chineseRT(A,B)
print(x)
print("==========")
print("Ngetes LCM")'''
'''mylist = [3,4,8]
x = dlp.lcm(mylist)
print(x)'''
