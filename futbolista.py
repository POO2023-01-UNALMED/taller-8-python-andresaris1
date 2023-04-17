from deportista import Deportista
from persona import Persona


class Futbolista(Persona, Deportista):
    _listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self, targetasRojas):
        self._tarjetasRojas = targetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil

    @classmethod
    def getListaFutbolistas(cls):
        return cls._listaFutbolistas

    @classmethod
    def setListaFutbolistas(cls, listaFutbolistas):
        cls._listaFutbolistas = listaFutbolistas

    def __str__(self):
        return "Mi nombre es " + self.getNombre() \
            + " soy profesional en el deporte " + self.getDeporte() \
            + " Tengo " + str(self.getEdad()) \
            + " años de edad y llevo " + str(self.getAñosPracticando()) \
            + " años en el deporte"
