#Trocando os moves do pokemon usando property e setter
class Captured_Poke:
    def __init__(self, name, move_one, move_two):
        self.name = name
        self._move_one = move_one
        self._move_two = move_two

    @property
    def hm_tm_one(self):
        return self._move_one

    @hm_tm_one.setter
    def hm_tm_one(self, new_move):
        self._move_one = new_move

    @property
    def hm_tm_two(self):
        return self._move_two

    @hm_tm_two.setter
    def hm_tm_two(self, new_move):
        self._move_two = new_move


charizard = Captured_Poke('Charizard', 'Flamethrower', 'Slash')
print(charizard._move_one)
charizard.hm_tm_one = 'Dragon Breath'
print(charizard._move_one)
print()
print(charizard._move_two)
charizard.hm_tm_two = 'Fire Spin'
print(charizard._move_two)
