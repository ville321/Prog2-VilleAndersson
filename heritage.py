class Djur: 
    def __init__(self, namn):
        self.namn = namn


class Fisk(Djur):
    def __init__(self, maxdjup, namn):
        super().__init__(namn)
        self.maxdjup = maxdjup

class Fågel(Djur):
    def __init__(self, vingspann, namn):
        super().__init__(namn)
        self.vingspann = vingspann

class Torsk(Fisk):
    def __init__(self, maxdjup, namn, hastighet):
        super().__init__(maxdjup, namn)
        self.hastighet = hastighet

class Haj(Fisk):
    def __init__(self, maxdjup, namn, antalTänder):
        super().__init__(maxdjup, namn)
        self.antalTänder = antalTänder

def fånga(haj, torsk):
    if torsk.hastighet < 30 or haj.maxdjup >= torsk.maxdjup:
        return True
    else:
        return False
    


fisk1 = Torsk(15, "bob", 30)
haj1 = Haj(10, "bengt", 10 )
# print(haj1.antalTänder, haj1.namn, haj1.maxdjup)

print(fånga(haj1, fisk1))