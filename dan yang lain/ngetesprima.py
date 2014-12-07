class NgetesPrima:
    #deterministik
    def caraPrimitif(self, x):
        if(x % 2 == 0):
            return False
        pembagi = 3
        while(pembagi < (x // 2)):
            if(x % pembagi == 0):
                return False
            pembagi = pembagi + 2
        return True

tes = NgetesPrima()
print(tes.caraPrimitif(1615))
