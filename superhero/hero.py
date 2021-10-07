import random

random.randint(2, 7)

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          name: String
          starting_health: Integer
          current_health: Integer
        '''
    def fight(self, opponent):
        ''' Current Hero will take turn fighting the opponet hero passed in.
        '''

    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

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
