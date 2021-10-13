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

    self.abilities = list()
    self.armors = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    my_hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.abilities)
    print(my_hero.name)
    print(my_hero.current_health)
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")x`

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
