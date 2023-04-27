class Pokemon:
    def __init__(self, nome, atacando=False, voar=False):
        self.nome = nome
        self.atacando = atacando
        self.voando = voar

    def ataque(self):
       if not self.voando:
            if self.atacando:
                print(f'{self.nome} já está atacando...')
                return
            print(f'{self.nome} está em ataque...')
            self.atacando = True
       else:
           print(f'{self.nome} não pode atacar em voou.')

    def para_ataque(self):
        if self.atacando:
            print(f'{self.nome} parou de atacar.')
            self.atacando = False
            return
        print(f'{self.nome} não está em ataque.')

    def voar(self):
        if self.atacando:
            print(f'{self.nome} não pode voar enquanto está em ataque.')
            return
        print(f'{self.nome} começou a voar!')
        self.voando = True

    def para_voar(self):
        if self.voando:
            print(f'{self.nome} parou de voar.')
            self.voando = False
            return
        print(f'{self.nome} não está voando')


charizar = Pokemon('Charizard')
charizar.ataque()
charizar.voar()
charizar.para_voar()
charizar.para_ataque()
charizar.voar()