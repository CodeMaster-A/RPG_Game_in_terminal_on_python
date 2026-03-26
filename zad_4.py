from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, health, max_health, resource, max_resource, armore, magical_protection=0, damage=0, level=1, experience=0, max_experience=400):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.resource = resource
        self.max_resource = max_resource
        self.armore = armore
        self.magical_protection = magical_protection
        self.damage = damage
        self.level = level
        self.experience = experience
        self.max_experience = max_experience

    def deal_damage(self):
        pass

    def take_damage(self):
        pass

    def check_info(self):
        info = {
            'Имя': self.name,
            'Уровень': self.level,
            'Здоровье': f"{self.health}/{self.max_health}",
            'Ресурс': f"{self.resource}/{self.max_resource}",
            'Броня': self.armore,
            'Магическая защита': self.magical_protection,
            'Опыт': f"{self.experience}/{self.max_experience}",
            'Опыт до следующего уровня': self.max_experience - self.experience
        }

        print('ИНФОРМАЦИЯ О ПЕРСОНАЖЕ')
        for key, val in info.items():
            print(f"{key}: {val}")



class Rogue(Player):
    def __init__(self, name):
        super().__init__(name, health=100, max_health=100, resource=100, max_resource=100, armore=200)



class Warrior(Player):
    pass

class Paladin(Player):
    pass

class DeathKnight(Player):
    pass

class Warlock(Player):
    pass

class Priest(Player):
    pass

class Mag(Player):
    pass

class Druid(Player):
    pass

class Hunter(Player):
    pass

class Shaman(Player):
    pass


r1 = Rogue('Jack')
r1.check_info()