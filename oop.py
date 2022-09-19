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


class Unit:
    units = 0

    def __init__(self, name: str, army: str) -> None:
        self.name = name
        self.army = army
        self.burn = False
        self.bleeding = False
        self.health = 100
        self.damage = 10
        Unit.units += 1

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
                War.blue_army.remove(self)
                print(f'!!!!!!!!!!warrior{start_blue} {self.name} {finish_blue}  dead...!!!!!!!!!!')
            if self.army == 'red':
                War.red_army.remove(self)
                print(f'!!!!!!!!!!!warrior{start_red} {self.name} {end_red}  dead...!!!!!!!!!!!')

    def fight_personal(self, defender) -> None:
        """Provide one round of warriors fight one per one below incoming warriors
        working with incoming warriors"""
        armordamage = 0 if defender.armor <= 0 else \
            round(self.damage * random.uniform(0.3, 0.5))  # if more than 0 - counting armor absorption of damage (species)
        hpdamage = round((self.damage * random.uniform(0.89, 1.2))) - armordamage
        defender.armor -= armordamage
        defender.health -= hpdamage
        print(f'{self.name} gave {start_yellow}{hpdamage}{finish_yellow} hp damage to {defender.name}\n'
              f'{defender.name} hp left - {start_green}{defender.health}{finish_green} hp')
        defender.check_hp()


class Warrior(Unit):
    warriors = 0

    def __init__(self, name: str, army: str) -> None:
        Unit.__init__(self, name, army)
        self.damage = 20
        self.armor = 50
        Warrior.warriors += 1

    def warrior_attack(self, defender):
        armordamage = 0 if defender.armor <= 0 else \
            round(self.damage * random.uniform(0.3, 0.5))  # if more than 0 - counting armor absorption of damage
        hpdamage = round((self.damage * random.uniform(0.89, 1.1))) - armordamage
        if self.health in range(0, 15):  # if hp less than 10 - class warrior given critical damage (species)
            hpdamage = round(hpdamage * random.uniform(1.5, 3))
            armordamage = round(armordamage * random.uniform(1.5, 3))
            print('!!!CRITICAL DAMAGE!!!')
        if isinstance(defender, Lancer):    # ~1:3 chance for lancer to dodge attack (species)
            hpdamage = 0 if (random.randint(0, 10) % 3 == 0) else hpdamage
            if hpdamage == 0:
                print('!!!MISS ATTACK!!!')
        defender.armor -= armordamage
        defender.health -= hpdamage
        print(f'WARRIOR {self.name} gave {start_yellow}{hpdamage}{finish_yellow} hp damage to {defender.name}\n'
              f'{defender.name} hp left - {start_green}{defender.health}{finish_green} hp')
        defender.check_hp()


class Witcher(Unit):
    BURNDAMAGE = 4
    witchers = 0

    def __init__(self, name: str, army: str) -> None:
        Unit.__init__(self, name, army)
        self.mana = 60
        self.mana_per_attack = 8  # spent mana per one attack
        self.mana_regen = 6  # mana regeneration per one move
        self.mana_per_heal = 5  # spent mana per one healing of one brother in arms
        self.hp_per_heal = 6  # how many hp healing the Witcher per one heal
        self.damage = 6
        self.armor = 15
        Witcher.witchers += 1

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
                random_healing = random.choice(War.blue_army)
                random_healing.health += round(self.hp_per_heal * random.uniform(0.7, 1.3))
                print(f'{self.name} healing {random_healing.name}')
            if self.army == 'red':
                random_healing = random.choice(War.red_army)
                random_healing.health += round(self.hp_per_heal * random.uniform(0.7, 1.3))
                print(f'{self.name} healing {random_healing.name}')
            self.mana -= self.mana_per_heal
        self.mana += self.mana_regen  # regen of mana


class Lancer(Unit):
    BLEEDDAMAGE = 6  # every attack Lancer class main the opponent, and  blood loss
    lancers = 0

    def __init__(self, name: str, army: str) -> None:
        Unit.__init__(self, name, army)
        self.damage = 12
        self.armor = 30
        Lancer.lancers += 1

    def lancer_attack(self, defender):
        armordamage = 0 if defender.armor <= 0 else \
            round(self.damage * random.uniform(0.3, 0.5))  # if more than 0 - counting armor absorption of damage
        hpdamage = round((self.damage * random.uniform(0.89, 1.2))) - armordamage
        if isinstance(defender, Lancer):  # ~1:3 chance for lancer to dodge attack
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


class War:
    red_army = []
    blue_army = []
    red_attacks = 0  # count how many attack each army did
    blue_attacks = 0

    def __init__(self) -> None:
        pass

    @staticmethod
    def warrior_generator(how_many_warriors: int, warrior_class: Unit, warrior_army: list) -> None:
        """Generate random warrior with set class and army flag"""
        for i in range(how_many_warriors):
            person = Person('en')
            warrior1_name = person.first_name()
            army = 'blue' if warrior_army is War.blue_army else 'red'
            warrior1 = warrior_class(f'{warrior1_name}', army=army)
            warrior_army.append(warrior1)

    @staticmethod
    def army_generator(input_warriors: int) -> list:
        """Army Generator for both sides. amount of warriors is equal for both sides of three classes if possible """
        how_many_witchers = round(input_warriors * random.uniform(0.1, 0.3))
        how_many_lancers = round(input_warriors * random.uniform(0.2, 0.4))
        how_many_warriors = input_warriors - how_many_witchers - how_many_lancers
        War.warrior_generator(how_many_witchers, Witcher, War.red_army)
        War.warrior_generator(how_many_witchers, Witcher, War.blue_army)
        War.warrior_generator(how_many_lancers, Lancer, War.red_army)
        War.warrior_generator(how_many_lancers, Lancer, War.blue_army)
        War.warrior_generator(how_many_warriors, Warrior, War.red_army)
        War.warrior_generator(how_many_warriors, Warrior, War.blue_army)

        return [War.blue_army, War.red_army]

    @staticmethod
    def burn_bleed_check(what_army_check: list) -> None:
        """Checking if warrior burning, or bleeding"""
        for warrior in what_army_check:
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

    @staticmethod
    def fight_random() -> None:
        """Provide one round of random warriors fight one per one below incoming warriors
        working with generating army"""
        the_dice = random.randint(1, 100)  # start the random machine, to decide, who will attack now
        red_army = War.red_army.copy()
        blue_army = War.blue_army.copy()
        if the_dice % 2 != 0:
            War.red_attacks += 1
            print(f'{start_red}RED ARMY ATTACKING{end_red}')
            attacker = random.choice(red_army)
            defender = random.choice(blue_army)
            blue_army.remove(defender)
            if len(blue_army) >= 2:  # checking how many opponent warriors left, to except out of len error
                defender2 = random.choice(blue_army)
                blue_army.remove(defender2)
                defender3 = random.choice(blue_army)
            elif len(blue_army) == 1:
                defender2 = random.choice(blue_army)
                defender3 = ''  # if opp warriors almost die - assign an empty variable, since there is no one to beat
            elif len(blue_army) == 0:
                defender2 = ''
                defender3 = ''
        elif the_dice % 2 == 0:
            War.blue_attacks += 1
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
              f'There are {start_red} {len(War.red_army)} warriors for RED ARMY{end_red} and{start_blue} '
              f'{len(War.blue_army)} warriors for BLUE ARMY{finish_blue}')
        while True:
            if len(War.red_army) and len(War.blue_army):
                War.fight_random()
                print(f'left Warriors red army - {len(War.red_army)}, '
                      f'left Warriors blue army - {len(War.blue_army)}')
            else:
                break
            War.burn_bleed_check(War.red_army)
            War.burn_bleed_check(War.blue_army)
        if not len(War.red_army):
            print(f"{start_blue}Blue army WIN!!!{finish_blue} Red army was totally destroyed\n"
                  f"That`s the list of alive warriors of {start_blue}blue army{finish_blue}:")
            for number, name, in enumerate(War.blue_army):
                print(f' {start_purple} {number + 1}, {str(type(name))[17:-2]} {name.name}, '
                      f'left hp {name.health}  {finish_purple}')
        if not len(War.blue_army):
            print(f"{start_red}Red army WIN!!!{end_red} Blue army was totally destroyed\n"
                  f"That`s the list of alive warriors of {start_red}red army{end_red}:")
            for number, name in enumerate(War.red_army):
                print(f' {start_purple} {number + 1}, {str(type(name))[17:-2]} {name.name}, '
                      f'left hp {name.health}  {finish_purple}')


War.army_generator(10)

# attacker = random.choice(War.red_army)
# defender = random.choice(War.blue_army)
#
# print(Unit.getinfo(attacker))

War.war()
