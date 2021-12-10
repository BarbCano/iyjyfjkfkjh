"""Unidad 4 polimorfismo"""

class InstMusic:
    def _init_(self):
        pass

    def tocarinstrumento(self):
        print(type(self)._name_, "Reproduciendo acorde")


class Cuerdas(InstMusic):
    def _init_(self):
        pass

class Ukelele(Cuerdas):
    def _init_(self):
        pass
    def tocarinstrumento(self, nota = None):
        if  nota == None:
            print("La nota del Ukelele es Fa mayor")
        else:
            for x in range(nota):
                print("La nota es Fa menor")
class Bajo(Cuerdas):
    def _init_(self):
        pass
    def tocarinstrumento(self, NumCompass = 5):
        print("La secuencia en bajo es:")
        print("Si, Re#, Fa#, Sol, "*NumCompass)
class Piano(InstMusic):
    def _init_(self):
        pass

    def tocarinstrumento(self):
        print("El piano tiene 5 octavas")