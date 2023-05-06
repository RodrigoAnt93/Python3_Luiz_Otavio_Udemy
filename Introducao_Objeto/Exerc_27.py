class Pokemon:
    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self._lvl = lvl

    def up_lvl(self):
        self._lvl += 1
        return f'{self.name} evoluiu para {self._lvl}.'

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(name = {self.name!r}, type = {self.type!r}, lvl = {self._lvl!r})'


gengar = Pokemon('Gengar', ['Fantasma', 'Venenoso'], 45)
print(gengar.__repr__())
print(gengar.up_lvl())
print(gengar.__repr__())





