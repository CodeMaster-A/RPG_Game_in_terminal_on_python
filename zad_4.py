from abc import ABC, abstractmethod
from time import sleep

class Player(ABC):
    def __init__(self, name, health, max_health, resource, max_resource, armore, auto_attak_hand, magical_protection=0, level=1, experience=0, max_experience=400, count_death=0, count_kill=0, weapon=None):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.resource = resource
        self.max_resource = max_resource
        self.armore = armore
        self.auto_attak_hand = auto_attak_hand
        self.magical_protection = magical_protection
        self.level = level
        self.experience = experience
        self.max_experience = max_experience
        self.count_death = count_death
        self.count_kill = count_kill
        self.weapon = weapon
        self.spells_book = {}

    def learn_spell(self, spell):
        if spell not in self.spells_book:
            self.spells_book[spell] = spell
            print(f"{self.name} выучил новую способность: {spell}")
        else:
            print('Вам уже известна эта способность!')

    def use_spell(self, spell, target):
        while target.health > 0:
            if spell in self.spells_book:
                if not spell.use(self, target):
                    break
            else:
                print('Неизвестная способность!')
                break

            if target.health <= 0:
                self.counter_kill()
                break

        else:
            self.counter_kill(target)

    def deal_damage(self, target):
        while target.health > 0:
            target.take_damage(self.auto_attak_hand)
            print(f"Вы атаковали монстра {target.name} автоатакой")
            print(f"Здоровье монстра: {target.health}|{target.max_health}")

    def take_damage(self, amount):
        if self.health > 0: 
            self.health -= amount

        if self.health <= 0:
            self.health = 0
            self.counter_death()
            print('Вы погибли!')
            self.respown()

        return f"{max(0, self.health)}|{self.max_health}"

    def respown(self):
        sleep(35)
        self.health = self.max_health
        self.resource = self.max_resource

        print('Ваш персонаж воскрешен!')
        return f"Ваш персонаж воскрешен! {self.health}|{self.resource}"
    
    def counter_death(self):
        self.count_death += 1

        return self.count_death 

    def counter_kill(self):
        self.count_kill += 1
            
        return self.count_kill

    def check_info(self):
        info = {
            'Имя': self.name,
            'Класс': self.__class__.__name__,
            'Уровень': self.level,
            'Оружие': self.weapon,
            'Способности': self.spells_book,
            'Здоровье': f"{self.health}/{self.max_health}",
            'Ресурс': f"{self.resource}/{self.max_resource}",
            'Урон от автоатаки': self.auto_attak_hand,
            'Броня': self.armore,
            'Магическая защита': self.magical_protection,
            'Опыт': f"{self.experience}/{self.max_experience}",
            'Опыт до следующего уровня': self.max_experience - self.experience,
            'Количество смертей': self.count_death,
            'Количество убитых монстров': self.count_kill
        }

        print('-'*35)
        print('ИНФОРМАЦИЯ О ПЕРСОНАЖЕ')
        print('-'*35)
        for key, val in info.items():
            print(f"{key}: {val}")
        print('-'*35)
    
    def check_spells(self):
        return self.spells_book

class Monster:
    def __init__(self, name, health=35, max_health=35, base_damage=5, level=1):
        self.name = name 
        self.health = health
        self.max_health = max_health
        self.base_damage = base_damage
        self.level = level

    def take_damage(self, amount):
        if self.health > 0: 
            self.health -= amount

        if self.health <= 0:
            self.health = 0
            print('Монстр погиб!')
            self.respown()

        return f"{max(0, self.health)}|{self.max_health}"

    def respown(self):
        sleep(5)
        self.health = self.max_health

        print(f"Монстр воскрешен! {self.health}|{self.max_health}")
    
    def get_info(self):
        info = {
            'Имя': self.name,
            'Здоровье': f"{self.health}/{self.max_health}",
            'Уровень': self.level,
            'Урон': self.base_damage,
        }

        print('-'*35)
        print('ИНФОРМАЦИЯ О МОНСТРЕ')
        print('-'*35)
        for key, val in info.items():
            print(f"{key}: {val}")
        print('-'*35)

class Weapon:
    def __init__(self, name, bonus_damage, interval):
        self.name = name
        self.bonus_damage = bonus_damage
        self.interval = interval

class Spell:
    def __init__(self, name, damage, size_res):
        self.name = name
        self.damage = damage
        self.size_res = size_res

    def use(self, player: Player, target: Monster):
        if player.resource >= self.size_res:
            player.resource -= self.size_res
            print(f"[{player.name}] использует [{self.name}]!")
            target.take_damage(self.damage)
            print(f"Здоровье монстра: {target.health}")
            return True
        else:
            print('Недостаточно ресурса!')
            return False

    def __str__(self):
        return self.name


class Rogue(Player):
    def __init__(self, name):
        super().__init__(name, health=90, max_health=100, resource=100, max_resource=100, armore=200, auto_attak_hand=7)



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
sniky_hit = Spell('Коварный удар', 30, 35)

r1.learn_spell(sniky_hit)
r1.check_info()
r1.check_spells()

m1 = Monster('Monster')


r1.use_spell(sniky_hit, m1)
r1.check_info()