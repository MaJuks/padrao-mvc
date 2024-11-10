class Modelo:
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1

    def resetar(self):
        self.contador = 0

    def obter_contador(self):
        return self.contador
