# Создаём мини-игру в консольке
# 
# У вас есть базовый класс:
class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, other):
        pass

# Вам необходимо:

# 1 - Реализовать метод attack():
#    - он должен уменьшать hp у другого персонажа
#    - и выводить сообщение об атаке

# 2 - Создать класс Player (наследуется от Character)

# 3 - Создать класс Enemy (наследуется от Character)

# 4 - В классе Enemy добавить уникальный метод (например roar())

# 5 - Создать бой, например:
hero = Player("Герой", 100, 20)
monster = Enemy("Орк", 80, 15)

hero.attack(monster)
monster.roar()
monster.attack(hero)

# И выводите игроку на экран всё, что происходит
