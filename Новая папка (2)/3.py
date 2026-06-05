# Дан класс Character.
# 
# Вам необходимо:
# 1 - отнимать hp
# 2 - если hp <= 0, то выводить что персонаж склеил ласты

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self dmg):
        pass
