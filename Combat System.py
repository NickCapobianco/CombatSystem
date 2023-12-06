import time,random

def slow(x):
   time.sleep(x)
   
def gameOver():
   exit()
########################################################
   
class opponent():
   hp = 20
   endurance = 10
   x = 0
   
   def attack(self, player):
      player.self = player
      x = random.randint(1,4)
      
      if x == 1 or x == 3:
         opponent.hit(player)

      if x == 2:
         opponent.betray(opponent)
      
      if x == 4:
         opponent.miss()

   def hit(self, player):
      player.self = player
      rng = random.randint(1,3)
      chance = random.randint(1,45)
      if chance % 15 == 0:
         player.hp -= (rng * 2)
         print("Your opponent has hit you for", rng * 2, "damage")
      else:
         player.hp -= rng
         print("Your opponent has hit you for", rng , "damage")

   def betray(self, opponent):
      opponent.self = opponent
      rng = random.randint(1,2)
      print("Your opponent betrayed themself!")
      print("They take a self-inflicting", rng , "damage")
      opponent.hp -= rng

   def miss(self):
      print("Your opponent missed!")
      
#########################################################
      
class player():
   hp = 20
   endurance = 10
   y = 0

   def attack(self, opponent):
      print("1: Pistol, 2: Auto Rifle, 3: Sniper Rifle, 4: Knife")
      user = int(input("Choose an attack: "))
      while user != 1 and user != 2 and user != 3 and user != 4:
         print("Please choose from the numbers 1 - 4.")
         print("1: Pistol, 2: Auto Rifle, 3: Sniper Rifle, 4: Knife")
         user = int(input("Choose an attack: "))
         
      slow(1)

      if user == 1:
         player.pistol(opponent)
      if user == 2:
         player.autoRifle(opponent)
      if user == 3:
         player.sniperRifle(opponent)
      if user == 4:
         player.knife(opponent)
      
   def pistol(self, opponent):
      opponent.self = opponent
      rng = random.randint(1,2)
      opponent.hp -= rng
      player.endurance -= 1
      print("You shoot your opponent for", rng, "damage.")

   def autoRifle(self, opponent):
      opponent.self = opponent
      rng = random.randint(1,4)
      if rng == 4:
         opponent.hp += rng
         print("You missed!")
      else:
         opponent.hp -= rng
         player.endurance -= 1
         print("You shoot your opponent for", rng, "damage.")

   def sniperRifle(self, opponent):
      opponent.self = opponent
      rng = random.randint(2,5)
      if rng == 2:
         opponent.hp += rng
         print("You missed and your opponent had time to increase their health\
 by ", rng, ".",sep="")
      else: 
         opponent.hp -= rng
         player.endurance -= 2
         print("You snipe your opponent for", rng, "damage.")

   def knife(self, opponent):
      opponent.self = opponent
      rng = random.randint(1,15)
      if rng == 3 or rng == 6:
         rng = (rng * 2) // 3
         opponent.hp += rng
         print("Your opponent has turned the knife on you! You lost", rng, "health!")
         player.hp -= rng
         print("Your opponent has stolen the health from you!")
      else:    
         rng = random.randint(1,3)
         opponent.hp -= rng 
         player.endurance -= 1
         print("You stab your opponent for", rng, "damage.")
   
#########################################################

player = player()
opponent = opponent()
         
while opponent.hp > 0 and player.hp > 0:
   opponent.x = player.hp
   player.y = opponent.hp
   
   player.attack(opponent)
   opponent.attack(player)
   
   opponent.x -= player.hp
   player.y -= opponent.hp
   
   print("Player's HP: ", player.hp, " | HP lost this turn: ", opponent.x,sep="")
   print("Opponent's HP:", opponent.hp, " | HP lost this turn: ", player.y,sep="")
   print()
   
if player.hp <= 0:
   print("Player's HP: ", player.hp)
   print("Opponent's HP:", opponent.hp)
   print("Game over. Better luck next time!")
   gameOver()
if opponent.hp <= 0:
   print("Player's HP: ", player.hp)
   print("Opponent's HP:", opponent.hp)
   print("You have defeated your opponent! Congratulations!")
   gameOver()
