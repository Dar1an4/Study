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


class Warriors:
    red_army = []
    blue_army = []
    warriors = 0
    red_attacks = 0
    blue_attacks = 0

    def __init__(self, name: str, army: str, damage: int) -> None:
        self.name = name
        self.army = army
        self.health = 100
        self.armor = 50
        self.damage = damage
        self.burn = False
        self.bleeding = False
        Warriors.warriors += 1

    def getinfo(self) -> str:
        """Return info of stats entered warrior"""
        if isinstance(self, Warriors):
            return f'name - {self.name}, health - {self.health}, armor - {self.armor}, damage - {self.damage}, ' \
                   f'army - {self.army}'
        elif isinstance(self, Lancer):
            return f'name - {self.name}, health - {self.health}, armor - {self.armor}, damage - {self.damage}, ' \
                   f'army - {self.army}, bleeding damage - {Lancer.bleeddamage}'
        elif isinstance(self, Witcher):
            return f'name - {self.name}, health - {self.health}, armor - {self.armor}, damage - {self.damage}, ' \
                   f'mana - {self.mana}, army - {self.army}, burn damage - {Witcher.burndamage}, ' \
                   f'hp healing - {self.hp_per_heal}'

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
            warrior1 = Warriors(f'{warrior1_name}', army="red", damage=20)
            warrior2 = Warriors(f'{warrior2_name}', army="blue", damage=20)
            Warriors.red_army.append(warrior1)
            Warriors.blue_army.append(warrior2)
        for i in range(how_many_witchers):
            warrior1_name = person.first_name()
            warrior2_name = person.first_name()
            warrior1 = Witcher(f'{warrior1_name}', army="red", damage=6)
            warrior2 = Witcher(f'{warrior2_name}', army="blue", damage=6)
            Warriors.red_army.append(warrior1)
            Warriors.blue_army.append(warrior2)
        for i in range(how_many_lancers):
            warrior1_name = person.first_name()
            warrior2_name = person.first_name()
            warrior1 = Lancer(f'{warrior1_name}', army="red", damage=12)
            warrior2 = Lancer(f'{warrior2_name}', army="blue", damage=12)
            Warriors.red_army.append(warrior1)
            Warriors.blue_army.append(warrior2)
        return [Warriors.blue_army, Warriors.red_army]

    @staticmethod
    def check_hp(defender) -> None:
        """Checking hp of a defender and kill him if necessary."""
        if defender and defender.health <= 0:
            if defender.army == 'blue':
                Warriors.blue_army.remove(defender)
                print(f'!!!!!!!!!!warrior{start_blue} {defender.name} {finish_blue}  dead...!!!!!!!!!!')
            if defender.army == 'red':
                Warriors.red_army.remove(defender)
                print(f'!!!!!!!!!!!warrior{start_red} {defender.name} {end_red}  dead...!!!!!!!!!!!')

    @staticmethod
    def burn_mana_bleed_check() -> None:
        """Checking if warrior burning, or bleeding"""
        for warrior in Warriors.red_army:
            if warrior.burn:
                damage = int(Witcher.burndamage * random.uniform(0.7, 1.1))
                warrior.health -= damage
                warrior.burn = False
                print(f"{start_red}Ohhh warrior {warrior.name} is burning! - {damage} hp{end_red}")
                Warriors.check_hp(warrior)
            if warrior.bleeding:
                damage = int(Lancer.bleeddamage * random.uniform(0.8, 1.3))
                warrior.health -= damage
                warrior.bleeding = False
                print(f"{start_red}Ohhh warrior {warrior.name} is bleeding! - {damage} hp{end_red}")
                Warriors.check_hp(warrior)
        for warrior in Warriors.blue_army:
            if warrior.burn:
                damage = int(Witcher.burndamage * random.uniform(0.7, 1.1))
                warrior.health -= damage
                warrior.burn = False
                print(f"{start_red} Ohhh warrior {warrior.name} is burning! - {damage} hp{end_red}")
                Warriors.check_hp(warrior)
            if warrior.bleeding:
                damage = int(Lancer.bleeddamage * random.uniform(0.8, 1.3))
                warrior.health -= damage
                warrior.bleeding = False
                print(f"{start_red}Ohhh warrior {warrior.name} is bleeding! - {damage} hp{end_red}")
                Warriors.check_hp(warrior)

    @staticmethod
    def warrior_attack(attacker, defender):
        armordamage = 0 if defender.armor <= 0 else int(attacker.damage * random.uniform(0.3, 0.5))
        hpdamage = int((attacker.damage * random.uniform(0.89, 1.1))) - armordamage
        if attacker.health in range(0, 10):
            hpdamage = int(hpdamage * random.uniform(1.5, 3))
            armordamage = int(armordamage * random.uniform(1.5, 3))
        if isinstance(defender, Lancer):
            hpdamage = 0 if (random.randint(0, 10) % 3 == 0) else hpdamage
        defender.armor -= armordamage
        defender.health -= hpdamage
        print(f'WARRIOR {attacker.name} gave {start_yellow}{hpdamage}{finish_yellow} hp damage to {defender.name}\n'
              f'{defender.name} hp left - {start_green}{defender.health}{finish_green} hp')
        Warriors.check_hp(defender)

    @staticmethod
    def fight_personal(attacker, defender) -> None:
        """Provide one round of warriors fight one per one below incoming warriors
        working with incoming warriors"""
        armordamage = 0 if defender.armor <= 0 else int(attacker.damage * random.uniform(0.3, 0.5))
        hpdamage = int((attacker.damage * random.uniform(0.89, 1.2))) - armordamage
        defender.armor -= armordamage
        defender.health -= hpdamage
        print(f'{attacker.name} gave {start_yellow}{hpdamage}{finish_yellow} hp damage to {defender.name}\n'
              f'{defender.name} hp left - {start_green}{defender.health}{finish_green} hp')
        if defender.health < 0:
            print(f'warrior {defender.name} {start_red} dead{end_red}...')
            if defender.army == 'blue':
                Warriors.blue_army.remove(defender)
            if defender.army == 'red':
                Warriors.red_army.remove(defender)

    @staticmethod
    def fight_random() -> None:
        """Provide one round of random warriors fight one per one below incoming warriors
        working with generating army"""
        the_dice = random.randint(1, 100)
        red_army = Warriors.red_army.copy()
        blue_army = Warriors.blue_army.copy()
        if the_dice % 2 != 0:
            Warriors.red_attacks += 1
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
            Warriors.blue_attacks += 1
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
            Witcher.witcher_attack(attacker, defender)
            Witcher.witcher_attack(attacker, defender2)
            Witcher.witcher_attack(attacker, defender3)
        elif isinstance(attacker, Lancer):
            Lancer.lancer_attack(attacker, defender)
        else:
            Warriors.warrior_attack(attacker, defender)

    @staticmethod
    def war() -> None:
        """Starting a big war below red and blue army, until one of them will be destroyed"""
        print(f'let`s the battle begin\n'
              f'There are {start_red} {len(Warriors.red_army)} warriors for RED ARMY{end_red} and{start_blue} '
              f'{len(Warriors.blue_army)} warriors for BLUE ARMY{finish_blue}')
        while True:
            if len(Warriors.red_army) and len(Warriors.blue_army):
                Warriors.fight_random()
                print(f'left Warriors red army - {len(Warriors.red_army)}, '
                      f'left Warriors blue army - {len(Warriors.blue_army)}')
            else:
                break
            Warriors.burn_mana_bleed_check()
        if len(Warriors.red_army) == 0:
            print(f"{start_blue}Blue army WIN!!!{finish_blue} Red army was totally destroyed\n"
                  f"That`s the list of alive warriors of {start_blue}blue army{finish_blue}:")
            for number, name, in enumerate(Warriors.blue_army):
                print(f' {start_purple} {number + 1}, {str(type(name))[17:-2]} {name.name}, '
                      f'left hp {name.health}  {finish_purple}')
        if len(Warriors.blue_army) == 0:
            print(f"{start_red}Red army WIN!!!{end_red} Blue army was totally destroyed\n"
                  f"That`s the list of alive warriors of {start_red}red army{end_red}:")
            for number, name in enumerate(Warriors.red_army):
                print(f' {start_purple} {number + 1}, {str(type(name))[17:-2]} {name.name}, '
                      f'left hp {name.health}  {finish_purple}')


class Witcher(Warriors):
    burndamage = 4
    witchers = 0

    def __init__(self, name, army, damage):
        self.mana = 60
        self.health = 100
        self.mana_per_attack = 8
        self.mana_per_heal = 4
        self.hp_per_heal = 10
        Witcher.witchers += 1
        self.burn = False
        self.bleeding = False
        Warriors.__init__(self, name, army, damage)

    @staticmethod
    def witcher_attack(attacker, defender) -> None:
        """Provide witcher attacking"""
        if attacker.mana >= attacker.mana_per_attack and defender:
            hpdamage = int(attacker.damage * random.uniform(0.5, 1.15))
            defender.health -= hpdamage
            attacker.mana -= attacker.mana_per_attack
            defender.burn = True
            print(f'WITCHER {attacker.name} gave {start_yellow}{hpdamage}{finish_yellow} hp damage to {defender.name}\n'
                  f'and {defender.name} is burnung!\n'
                  f'his hp left - {start_green}{defender.health}{finish_green} hp')
            Warriors.check_hp(defender)
        if attacker.mana >= attacker.mana_per_heal:
            if attacker.army == 'blue':
                random_healing = random.choice(Warriors.blue_army)
                random_healing.health += int(attacker.hp_per_heal * random.uniform(0.7, 1.3))
                print(f'{attacker.name} healing {random_healing.name}')
            if attacker.army == 'red':
                random_healing = random.choice(Warriors.red_army)
                random_healing.health += int(attacker.hp_per_heal * random.uniform(0.7, 1.3))
                print(f'{attacker.name} healing {random_healing.name}')
            attacker.mana -= 5
        attacker.mana += 6

class Lancer(Warriors):
    bleeddamage = 6
    lancers = 0

    def __init__(self, name, army, damage):
        self.health = 100
        self.armor = 30
        self.burn = False
        self.bleeding = False
        Lancer.lancers += 1
        Warriors.__init__(self, name, army, damage)

    @staticmethod
    def lancer_attack(attacker, defender):
        armordamage = 0 if defender.armor <= 0 else int(attacker.damage * random.uniform(0.3, 0.5))
        hpdamage = int((attacker.damage * random.uniform(0.89, 1.2))) - armordamage
        if isinstance(defender, Lancer):
            hpdamage = 0 if (random.randint(0, 9) % 3 == 0) else hpdamage
        defender.bleeding = True
        defender.armor -= armordamage
        defender.health -= hpdamage
        print(f'LANCER {attacker.name} gave {start_yellow}{hpdamage}{finish_yellow} hp damage to {defender.name}\n'
              f'{defender.name} hp left - {start_green}{defender.health}{finish_green} hp\n'
              f'and {defender.name} is bleeding!!!!')
        Warriors.check_hp(defender)

Warriors.army_generator(100)

print(f'{Warriors.warriors = }{Lancer.lancers = }, {Witcher.witchers = }')
Warriors.war()

print(f'{Warriors.red_attacks = }, {Warriors.blue_attacks = }')
