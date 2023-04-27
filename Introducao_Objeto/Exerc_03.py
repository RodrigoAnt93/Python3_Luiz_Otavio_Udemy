class Pokemon:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        return f'O {self.nome} atacou!'

    def executar(self):
        return self.atacar()


charizard = Pokemon("Charizard")

print(charizard.executar())