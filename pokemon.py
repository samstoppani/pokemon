import math

def attackPokemon(pokemonA, pokemonB):
    if (pokemonA.knockedOut):
        print("{} cannot attack... {} needs reviving.".format(pokemonA.name, pokemonA.name))
    else:
        if ((pokemonA.type == "Fire" and pokemonB.type == "Grass") or (pokemonA.type == "Grass" and pokemonB.type == "Water") or (pokemonA.type == "Water" and pokemonB.type == "Fire")):
            damage = 2 * pokemonA.attackPoints
            print("{}'s attack was super effective.".format(pokemonA.name))
            pokemonB.loseHealth(damage)

        elif ((pokemonA.type == "Fire" and pokemonB.type == "Water") or (pokemonA.type == "Grass" and pokemonB.type == "Fire") or (pokemonA.type == "Water" and pokemonB.type == "Grass")):
            damage = math.floor(0.5 * pokemonA.attackPoints)
            print("{}'s attack was not effective.".format(pokemonA.name))
            pokemonB.loseHealth(damage)

        else:
            damage = pokemonA.attackPoints
            print("{} attacked".format(pokemonA.name))
            pokemonB.loseHealth(damage)


class Pokemon:

    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.maxHealth = self.level * 10
        self.currentHealth = self.maxHealth
        self.attackPoints = self.level * 5
        self.knockedOut = False

    def loseHealth(self, lost):
        self.currentHealth -= lost
        if (self.currentHealth <= 0):
            self.knockedOut = True
            self.currentHealth = 0
            print("{} has been KO'd!".format(self.name))
    
        else :
            print("{} lost {}HP and has {}HP remaining.".format(self.name, lost, self.currentHealth))

    def gainHealth(self, gained):
        if (self.knockedOut):
            self.revive()
        self.currentHealth += gained
        if (self.currentHealth >= self.maxHealth):
            self.currentHealth = self.maxHealth
            print("{} now has full health at {}HP.".format(self.name, self.currentHealth))
        else:
            print("{} now has {}HP".format(self.name, self.currentHealth))

        # print("{} now has {}HP.".format(self.name, self.currentHealth))

    def revive(self):
        self.knockedOut = False
        print("{} was revived.".format(self.name))

    def attack(self, pokemon):
        attackPokemon(self, pokemon)


class Trainer:

    def __init__(self, name, pokemons, potions):
        self.name = name
        self.pokemons = pokemons[:6] # first 6 pokemons
        self.potions = potions
        self.currentPokemon = 0

    def attack(self, trainer):
        attackPokemon(self.pokemons[self.currentPokemon], trainer.pokemons[trainer.currentPokemon])
        
    def switchPokemon(self, index):
        noOfPokemon = len(self.pokemons)
        if (index <= (noOfPokemon - 1)):
            if (self.pokemons[index].knockedOut):
                print("{} is knocked out and needs reviving.".format(self.pokemons[self.currentPokemon].name))
            else:
                print('{}: \"That\'s enough {}\"'.format(self.name, self.pokemons[self.currentPokemon].name))
                self.currentPokemon = index
                print('{}: \"Go {}!\"'.format(self.name, self.pokemons[self.currentPokemon].name))
        else:
            print("No pokemon available in slot {}.".format(index))

    def healPokemon(self):
        if (self.potions > 0):
            print("{} used a health potion.".format(self.name))

            pokemon = self.pokemons[self.currentPokemon]
            pokemonHealthBefore = pokemon.currentHealth
            pokemon.gainHealth(100)
            self.potions -= 1
            pokemonHealthAfter = pokemon.currentHealth
            pokemonHealthGained = pokemonHealthAfter - pokemonHealthBefore

            print("{} gained {}HP.".format(pokemon.name, pokemonHealthGained))
            print("{} has {} health potion(s) remaining.".format(self.name, self.potions))

        else:
            print("{} has no health potions remaining.".format(self.name))
        
# Water Pokemons
squirtle = Pokemon("Squirtle", 10, "Water")
horsea = Pokemon("Horsea", 8, "Water")
magikarp = Pokemon("Magikarp", 12, "Water")
goldeen = Pokemon("Goldeen", 14, "Water")

# Grass Pokemons
bulbasaur = Pokemon("Bulbasaur", 15, "Grass")
oddish = Pokemon("Oddish", 6, "Grass")
shroomish = Pokemon("Shroomish", 7, "Grass")

# Fire Pokemons
charmander = Pokemon("Charmander", 10, "Fire")
slugma = Pokemon("Slugma", 6, "Fire")
charazard = Pokemon("Charazard", 15, "Fire")

# trainers
ash = Trainer("Ash", [charmander, magikarp, oddish], 3)
james = Trainer("James", [bulbasaur, slugma, shroomish], 2)


# simulation
ash.attack(james)
print("\n")

james.attack(ash)
print("\n")

ash.attack(james)
print("\n")

james.attack(ash)
print("\n")

james.healPokemon()
print("\n")

james.attack(ash)
print("\n")

ash.attack(james)
print("\n")

james.switchPokemon(1)
print("\n")

james.attack(ash)
print("\n")

ash.healPokemon()
print("\n")

ash.attack(james)
print("\n")

james.attack(ash)
print("\n")

ash.attack(james)
print("\n")

james.switchPokemon(0)
print("\n")

ash.healPokemon()
print("\n")



