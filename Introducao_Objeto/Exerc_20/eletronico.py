from log import LogFileMixin


class Eletronico:
    def __init__(self, name):
        self._name = name
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False


class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()
        if self._ligado:
            msg = f'{self._name} foi ligado'
            self.log_success(msg)

    def desligar(self):
        super().desligar()
        if not self._ligado:
            msg = f'{self._name} foi desligado'
            self.log_success(msg)
