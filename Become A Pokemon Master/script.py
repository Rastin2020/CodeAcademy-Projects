# -------------------- Pokemon Class --------------------:
class Pokemon:
  def __init__(self, name, level, elementType, currentHealth):
    self.name = name;
    self.level = level;
    self.elementType = elementType;
    self.currentHealth = currentHealth;
    self.maxHealth = 90 + (10*level);
    self.alive = True;
  
  # ----- Class functionality -----: 
  def pokemonFainted(self):
    self.alive = False;
    self.currentHealth = 0;
    print("-----------------------------------");
    print("{} has fainted!".format(self.name));
    print("-----------------------------------");
  def pokemonRevived(self):
    self.alive = True;
    print("-----------------------------------");
    print("{} has been revived!".format(self.name));
    print("-----------------------------------");
  def levelUp(self):
    self.level += 1;
    print("-----------------------------------");
    print("{} has leveled up ----> Level {}".format(self.name, self.level));
    print("-----------------------------------");
  
  def loseHealth(self, damage):
    self.currentHealth -= damage;
    if (self.currentHealth < 0):
      self.currentHealth = 0;
    print("-----------------------------------");
    print("{} has taken {} damage ----> Health remaining {}".format(self.name, damage, self.currentHealth));
    print("-----------------------------------");
    if (self.currentHealth == 0):
      self.pokemonFainted();
      
  def gainHealth(self, gain):
    if (self.alive == False):
      self.pokemonRevived();
    if (gain > self.maxHealth-self.currentHealth):
      print("-----------------------------------");
      print("{} has gained {} health:".format(self.name, (self.maxHealth-self.currentHealth)));
    else:
      print("-----------------------------------");
      print("{} has gained {} health:".format(self.name, (gain)));
    self.currentHealth += gain;
    if (self.currentHealth > self.maxHealth):
      self.currentHealth = self.maxHealth;
    print("Health remaining {}".format(self.currentHealth));
    
    # Class interaction method (attack):
  def attackPokemon(self, pokemon, damage):
      print("-----------------------------------");
      print("{} has attacked {}!".format(self.name, pokemon.name))
      print("-----------------------------------");
      
      if (self.elementType == "Fire" and pokemon.elementType == "Water"):
        pokemon.loseHealth(damage*0.5);
      elif (self.elementType == "Water" and pokemon.elementType == "Fire"):
        pokemon.loseHealth(damage*1.5);
      elif (self.elementType == "Grass" and pokemon.elementType == "Fire"):
        pokemon.loseHealth(damage*0.5);
      elif (self.elementType == "Fire" and pokemon.elementType == "Grass"):
        pokemon.loseHealth(damage*1.5);
      elif (self.elementType == "Water" and pokemon.elementType == "Grass"):
        pokemon.loseHealth(damage*0.5);
      elif (self.elementType == "Grass" and pokemon.elementType == "Water"):
        pokemon.loseHealth(damage*0.5);
      else:
        pokemon.loseHealth(damage);
        
# -------------------- Trainer Class --------------------:
class Trainer:
  def __init__(self, name, pokemons, potions, activePokemon):
    self.name = name;
    self.pokemons = pokemons;
    self.potions = potions;
    self.activePokemon = activePokemon
    
  # Class functionality:
  def switchPokemon(self, target):
    self.activePokemon = target;
    print("Switching pokemon to {}".format(self.pokemons[self.activePokemon]).name);
    
  def usePotion(self):
    self.pokemons[self.activePokemon].gainHealth(80);
    self.potions -= 1;
    
  def attackTrainer(self, trainer):
    print("{}'s".format(self.name)); self.pokemons[self.activePokemon].attackPokemon(trainer.pokemons[trainer.activePokemon], 11);

charizard = Pokemon("Charizard", 35, "Fire", 150);
pikachu = Pokemon("Pikachu", 15, "Electric", 80);
turtle = Pokemon("Turtle", 25, "Water", 90);
charmander = Pokemon("Charmander", 15, "Fire", 80);

jack = Trainer("Jack", [charizard, pikachu, turtle, charmander], 3, 1);
jill = Trainer("Jill", [charizard, pikachu, turtle, charmander], 13, 3);

jack.attackTrainer(jill);
