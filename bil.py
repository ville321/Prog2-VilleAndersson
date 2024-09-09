class Bil:

    antalbilar = 0

    def __init__(self, maxHastighet):
        self.__maxHastighet = maxHastighet
        Bil.antalbilar += 1

    
    def getMaxhastighet(self):
        return self.__maxHastighet
    
    def setMaxhastighet(self, maxHastighet):
        self.__maxHastighet = maxHastighet

    @staticmethod
    def milestokm(miles):
        return miles * 1.60934

bil1 = Bil(500)


print(f"Maxhastighet: {bil1.getMaxhastighet()} km/h")

bil1.setMaxhastighet(1000)

print(f"Maxhastighet: {bil1.getMaxhastighet()} km/h")

print(Bil.antalbilar)

bil2 = Bil(200)

print(Bil.antalbilar)