import random

random.randint(2, 7)

from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''
    def fight(self, opponent):
        ''' Current Hero will take turn fighting the opponet hero passed in.
        '''

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attaacks.
            return: total_damage:Int
        '''
        total_damage = 0
            for ability in self.abilities:
                total_damage += ability.attack()
            return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
        return: total_block:Int
        '''

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        pass

    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.
        '''
        pass

    self.abilities = list()
    self.armors = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.current_health())
    print(hero.abilities)
    print(my_hero.name)
    print(my_hero.current_health)
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)




class Ability:
    def __init__(self, name, max_damage):
        '''
        Initalize the values passed into this method as instance variables
        '''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        '''Return a value between 0 and the value set by self.max_damage.'''
        random_value = random.randint(0,self.max_damage)
        return random_value

    if __name__ == "__main":
        ability = Ability("Debugging Ability", 20)
        print(ability.name)
        print(ability.attack())

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        # TODO: Create instance variables for the values passed in
        pass

    def block(self):
        '''return a random value between 0 and the initialized max_block strength.
        '''
        pass

    if __name__ == "__main__":
        armor = Armos("Debugging Shield", 10)
        print(armor.name)
        print(armor.block())
