import random

from mimesis import Person


""""codes for colorful console"""
start_red = "\033[1;31m"
end_red = "\033[0;0m"
start_yellow = "\033[1;33m"
finish_yellow = "\033[0;0m"
start_green = "\033[1;32m"
finish_green = "\033[0;0m"
start_purple = "\033[1;35m"
finish_purple = "\033[0;0m"
start_blue = "\033[1;36m"
finish_blue = "\033[0;0m"


class Warrior:
    red_army = []
    blue_army = []
    warriors = 0
    red_attacks = 0
    blue_attacks = 0

    def __init__(self, name: str, army: str) -> None:
        self.name = name
        self.army = army
        self.damage = 20
        self.health = 100
        self.armor = 50
        self.burn = False
        self.bleeding = False
        Warrior.warriors += 1

    def getinfo(self) -> str:
        """Return info of stats entered warrior"""
        print()
        if isinstance(self, Warrior):
            return f'Class of warrior is {str(type(self))[17:-2]}, ' \
                   f'name - {self.name}, health - {self.health}, armor - {self.armor}, damage - {self.damage}, ' \
                   f'army - {self.army}'
        elif isinstance(self, Lancer):
            return f'Class of warrior is {str(type(self))[17:-2]}, ' \
                   f'name - {self.name}, health - {self.health}, armor - {self.armor}, damage - {self.damage}, ' \
                   f'army - {self.army}, bleeding damage - {Lancer.BLEEDDAMAGE}'
        elif isinstance(self, Witcher):
            return f'Class of warrior is {str(type(self))[17:-2]}, ' \
                   f'name - {self.name}, health - {self.health}, armor - {self.armor}, damage - {self.damage}, ' \
                   f'mana - {self.mana}, army - {self.army}, burn damage - {Witcher.BURNDAMAGE}, ' \
                   f'hp healing - {self.hp_per_heal}'

    def check_hp(self) -> None:
        """Checking hp of a defender and kill him if necessary."""
        if self and self.health <= 0:
            if self.army == 'blue':
                Warrior.blue_army.remove(self)
                print(f'!!!!!!!!!!warrior{start_blue} {self.name} {finish_blue}  dead...!!!!!!!!!!')
            if self.army == 'red':
                Warrior.red_army.remove(self)
                print(f'!!!!!!!!!!!warrior{start_red} {self.name} {end_red}  dead...!!!!!!!!!!!')

    def warrior_attack(self, defender):
        armordamage = 0 if defender.armor <= 0 else round(self.damage * random.uniform(0.3, 0.5))
        hpdamage = round((self.damage * random.uniform(0.89, 1.1))) - armordamage
        if self.health in range(0, 10):
            hpdamage = round(hpdamage * random.uniform(1.5, 3))
            armordamage = round(armordamage * random.uniform(1.5, 3))
            print('!!!CRITICAL DAMAGE!!!')
        if isinstance(defender, Lancer):
            hpdamage = 0 if (random.randint(0, 10) % 3 == 0) else hpdamage
            if hpdamage == 0:
                print('!!!MISS ATTACK!!!')
        defender.armor -= armordamage
        defender.health -= hpdamage
        print(f'WARRIOR {self.name} gave {start_yellow}{hpdamage}{finish_yellow} hp damage to {defender.name}\n'
              f'{defender.name} hp left - {start_green}{defender.health}{finish_green} hp')
        defender.check_hp()

    def fight_personal(self, defender) -> None:
        """Provide one round of warriors fight one per one below incoming warriors
        working with incoming warriors"""
        armordamage = 0 if defender.armor <= 0 else round(self.damage * random.uniform(0.3, 0.5))
        hpdamage = round((self.damage * random.uniform(0.89, 1.2))) - armordamage
        defender.armor -= armordamage
        defender.health -= hpdamage
        print(f'{self.name} gave {start_yellow}{hpdamage}{finish_yellow} hp damage to {defender.name}\n'
              f'{defender.name} hp left - {start_green}{defender.health}{finish_green} hp')
        defender.check_hp()

    @staticmethod
    def army_generator(input_warriors: int) -> list:
        """Army Generator for both sides. amount of warriors is equal for both sides """
        person = Person('en')
        how_many_witchers = round(input_warriors * random.uniform(0.1, 0.3))
        how_many_lancers = round(input_warriors * random.uniform(0.2, 0.4))
        how_many_warriors = input_warriors - how_many_witchers - how_many_lancers
        for i in range(how_many_warriors):
            warrior1_name = person.first_name()
            warrior2_name = person.first_name()
            warrior1 = Warrior(f'{warrior1_name}', army="red")
            warrior2 = Warrior(f'{warrior2_name}', army="blue")
            Warrior.red_army.append(warrior1)
            Warrior.blue_army.append(warrior2)
        for i in range(how_many_witchers):
            warrior1_name = person.first_name()
            warrior2_name = person.first_name()
            warrior1 = Witcher(f'{warrior1_name}', army="red")
            warrior2 = Witcher(f'{warrior2_name}', army="blue")
            Warrior.red_army.append(warrior1)
            Warrior.blue_army.append(warrior2)
        for i in range(how_many_lancers):
            warrior1_name = person.first_name()
            warrior2_name = person.first_name()
            warrior1 = Lancer(f'{warrior1_name}', army="red")
            warrior2 = Lancer(f'{warrior2_name}', army="blue")
            Warrior.red_army.append(warrior1)
            Warrior.blue_army.append(warrior2)
        return [Warrior.blue_army, Warrior.red_army]

    @staticmethod
    def burn_mana_bleed_check() -> None:
        """Checking if warrior burning, or bleeding"""
        for warrior in Warrior.red_army:
            if warrior.burn:
                damage = round(Witcher.BURNDAMAGE * random.uniform(0.7, 1.1))
                warrior.health -= damage
                warrior.burn = False
                print(f"{start_red}Ohhh warrior {warrior.name} is burning! - {damage} hp{end_red}")
                warrior.check_hp()
            if warrior.bleeding:
                damage = round(Lancer.BLEEDDAMAGE * random.uniform(0.8, 1.3))
                warrior.health -= damage
                warrior.bleeding = False
                print(f"{start_red}Ohhh warrior {warrior.name} is bleeding! - {damage} hp{end_red}")
                warrior.check_hp()
        for warrior in Warrior.blue_army:
            if warrior.burn:
                damage = round(Witcher.BURNDAMAGE * random.uniform(0.7, 1.1))
                warrior.health -= damage
                warrior.burn = False
                print(f"{start_red} Ohhh warrior {warrior.name} is burning! - {damage} hp{end_red}")
                warrior.check_hp()
            if warrior.bleeding:
                damage = round(Lancer.BLEEDDAMAGE * random.uniform(0.8, 1.3))
                warrior.health -= damage
                warrior.bleeding = False
                print(f"{start_red}Ohhh warrior {warrior.name} is bleeding! - {damage} hp{end_red}")
                warrior.check_hp()

    @staticmethod
    def fight_random() -> None:
        """Provide one round of random warriors fight one per one below incoming warriors
        working with generating army"""
        the_dice = random.randint(1, 100)
        red_army = Warrior.red_army.copy()
        blue_army = Warrior.blue_army.copy()
        if the_dice % 2 != 0:
            Warrior.red_attacks += 1
            print(f'{start_red}RED ARMY ATTACKING{end_red}')
            attacker = random.choice(red_army)
            defender = random.choice(blue_army)
            blue_army.remove(defender)
            if len(blue_army) >= 2:
                defender2 = random.choice(blue_army)
                blue_army.remove(defender2)
                defender3 = random.choice(blue_army)
            elif len(blue_army) == 1:
                defender2 = random.choice(blue_army)
                defender3 = ''
            elif len(blue_army) == 0:
                defender2 = ''
                defender3 = ''
        elif the_dice % 2 == 0:
            Warrior.blue_attacks += 1
            print(f'{start_blue}BLUE ARMY ATTACKING{finish_blue}')
            attacker = random.choice(blue_army)
            defender = random.choice(red_army)
            red_army.remove(defender)
            if len(red_army) >= 2:
                defender2 = random.choice(red_army)
                red_army.remove(defender2)
                defender3 = random.choice(red_army)
            elif len(red_army) == 1:
                defender2 = random.choice(red_army)
                defender3 = ''
            elif len(red_army) == 0:
                defender2 = ''
                defender3 = ''
        if isinstance(attacker, Witcher):
            attacker.witcher_attack(defender)
            attacker.witcher_attack(defender2)
            attacker.witcher_attack(defender3)
        elif isinstance(attacker, Lancer):
            attacker.lancer_attack(defender)
        else:
            attacker.warrior_attack(defender)

    @staticmethod
    def war() -> None:
        """Starting a big war below red and blue army, until one of them will be destroyed"""
        print(f'let`s the battle begin\n'
              f'There are {start_red} {len(Warrior.red_army)} warriors for RED ARMY{end_red} and{start_blue} '
              f'{len(Warrior.blue_army)} warriors for BLUE ARMY{finish_blue}')
        while True:
            if len(Warrior.red_army) and len(Warrior.blue_army):
                Warrior.fight_random()
                print(f'left Warriors red army - {len(Warrior.red_army)}, '
                      f'left Warriors blue army - {len(Warrior.blue_army)}')
            else:
                break
            Warrior.burn_mana_bleed_check()
        if len(Warrior.red_army) == 0:
            print(f"{start_blue}Blue army WIN!!!{finish_blue} Red army was totally destroyed\n"
                  f"That`s the list of alive warriors of {start_blue}blue army{finish_blue}:")
            for number, name, in enumerate(Warrior.blue_army):
                print(f' {start_purple} {number + 1}, {str(type(name))[17:-2]} {name.name}, '
                      f'left hp {name.health}  {finish_purple}')
        if len(Warrior.blue_army) == 0:
            print(f"{start_red}Red army WIN!!!{end_red} Blue army was totally destroyed\n"
                  f"That`s the list of alive warriors of {start_red}red army{end_red}:")
            for number, name in enumerate(Warrior.red_army):
                print(f' {start_purple} {number + 1}, {str(type(name))[17:-2]} {name.name}, '
                      f'left hp {name.health}  {finish_purple}')


class Witcher(Warrior):
    BURNDAMAGE = 4
    witchers = 0

    def __init__(self, name: str, army: str) -> None:
        self.mana = 60
        self.mana_per_attack = 8
        self.mana_regen = 6
        self.mana_per_heal = 5
        self.hp_per_heal = 6
        self.burn = False
        self.bleeding = False
        Witcher.witchers += 1
        Warrior.__init__(self, name, army)
        self.damage = 6
        self.armor = 10

    def witcher_attack(self, defender) -> None:
        """Provide witcher attacking"""
        if self.mana >= self.mana_per_attack and defender:
            hpdamage = round(self.damage * random.uniform(0.5, 1.15))
            defender.health -= hpdamage
            self.mana -= self.mana_per_attack
            defender.burn = True
            print(f'WITCHER {self.name} gave {start_yellow}{hpdamage}{finish_yellow} hp damage to {defender.name}\n'
                  f'and {defender.name} is burnung!\n'
                  f'his hp left - {start_green}{defender.health}{finish_green} hp')
            defender.check_hp()
        if self.mana >= self.mana_per_heal:
            if self.army == 'blue':
                random_healing = random.choice(Warrior.blue_army)
                random_healing.health += round(self.hp_per_heal * random.uniform(0.7, 1.3))
                print(f'{self.name} healing {random_healing.name}')
            if self.army == 'red':
                random_healing = random.choice(Warrior.red_army)
                random_healing.health += round(self.hp_per_heal * random.uniform(0.7, 1.3))
                print(f'{self.name} healing {random_healing.name}')
            self.mana -= self.mana_per_heal
        self.mana += self.mana_regen


class Lancer(Warrior):
    BLEEDDAMAGE = 6
    lancers = 0

    def __init__(self, name: str, army: str) -> None:
        self.burn = False
        self.bleeding = False
        Lancer.lancers += 1
        Warrior.__init__(self, name, army)
        self.damage = 12
        self.armor = 30

    def lancer_attack(self, defender):
        armordamage = 0 if defender.armor <= 0 else round(self.damage * random.uniform(0.3, 0.5))
        hpdamage = round((self.damage * random.uniform(0.89, 1.2))) - armordamage
        if isinstance(defender, Lancer):
            hpdamage = 0 if (random.randint(0, 10) % 3 == 0) else hpdamage
            if hpdamage == 0:
                print('!!!MISS ATTACK!!!')
        defender.bleeding = True
        defender.armor -= armordamage
        defender.health -= hpdamage
        print(f'LANCER {self.name} gave {start_yellow}{hpdamage}{finish_yellow} hp damage to {defender.name}\n'
              f'{defender.name} hp left - {start_green}{defender.health}{finish_green} hp\n'
              f'and {defender.name} is bleeding!!!!')
        defender.check_hp()


Warrior.army_generator(100)

attacker = random.choice(Warrior.red_army)
defender = random.choice(Warrior.blue_army)

print(attacker.getinfo())
print(defender.getinfo())

Witcher.war()

print(f'{Warrior.red_attacks = }, {Warrior.blue_attacks = }')



