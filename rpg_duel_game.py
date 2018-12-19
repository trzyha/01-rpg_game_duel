import os
from random import randint
from colorama import Fore, Back, Style

#all program start variables
hero_hp = 10
hero_power = 10
experience = 0

class creature(object):
  num_of_creatures = 0
  def __init__(self):
    
    self.breed = self.random_creature()
    self.power = randint(0,20)
    self.hp = randint(0,20)
  
    creature.num_of_creatures += 1
    
  def random_creature(self):
    creature_containter = ["Rat", "Dog", "Angry rabbit", "Wild cat"]
    #random_charakter = charakter_containter(randint(0,3))
    return creature_containter[randint(0,3)]
    
def clean(): #cleans the screen
  cls = lambda: print('\n'*100)
  cls()

def still_alive(hero_hp):
  if hero_hp > 0:
    return True
  else:
    return False

def gain_exp():
  global experience
  global hero_hp, hero_power
  experience_gain = randint(1,5)
  experience = experience + experience_gain
  if experience >= 10:
    experience = 0
    choose = input("You promote to next level choose upgrade health \"h\" or power \"p\"")
    if choose == "h":
      hero_hp += randint(1,2)
      print (f"You gain {Fore.YELLOW}%s{Style.RESET_ALL} health. Now you have {Fore.YELLOW}%s{Style.RESET_ALL} power and {Fore.YELLOW}%s{Style.RESET_ALL} health" %(hero_hp, hero_power, hero_hp))
    elif choose == "p":
      hero_power += randint(1,2)
      print (f"You gain {Fore.YELLOW}%s{Style.RESET_ALL} power. Now you have {Fore.YELLOW}%s{Style.RESET_ALL} power and {Fore.YELLOW}%s{Style.RESET_ALL} health" %(hero_power, hero_power, hero_hp))
    else:
      choose = input("Choose again. Health \"h\" or Power \"p\":")
  else:
    print (f"You get %s exp of %s collected" % (experience_gain, experience))
    
def did_found():
  if randint(0,1) == 1:
    print ("He found you! Prepare to fight")
  else:
    print ("You have luck! Creature walked away.")
  

    
def fight(cret_breed, cret_power, cret_hp):
  hero_hp = 10
  print ("\n\n")
  print ("You looked closer and %s have %s power and %s health" % (cret_breed, cret_power, cret_hp))
  print (f'{Fore.WHITE}{Back.BLUE}Hit (enter) /auto-fight "a" / retreet "r"{Style.RESET_ALL}')
  while cret_hp > 0 and hero_hp > 0:
    attack = input()
    if attack == "":
      hero_hit = randint(0,hero_power) #hero chance to hit with his actual power
      if hero_hit>3:
        print (f"You've hit %s with {Fore.CYAN}%s{Style.RESET_ALL} power and it has {Fore.CYAN}%s{Style.RESET_ALL} health left" % (cret_breed, hero_hit, cret_hp)) 
        cret_hp -= hero_hit
      else:
        print ("You have MISSED!")
      cret_attack = randint(0,10) #creature attacks
      if cret_attack > 6:
        print("%s hit you with %s power" % (cret_breed, cret_attack))
        print(f"You have still {Fore.YELLOW}%s health" % hero_hp)
        hero_hp -= cret_power
      else:
        print("%s missed you!"%cret_breed)
    elif attack.lower() == "a":
      while cret_hp > 0:
        hero_hit = randint(0,10) #random chance to hit
        if hero_hit>3:
          print ("%s have %s health" % (cret_breed, cret_hp))
          hero_hp = randint(0,10)
          cret_hp -= hero_hp
        else:
          print ("You have MISSED!")
          cret_attack = randint(0,10)
        if cret_attack > 6:
          print("%s hit you with %s power" % (cret_breed, cret_attack))
        else:
          print("%s missed you!"%cret_breed)
    elif attack.lower() == "r": #when retreet creature attack last time
      cret_attack = randint(0,10)
      if cret_attack > 6:
        print("You wanted retreet, but creature hit you last time with %s power" % (cret_breed, cret_attack))
      else:
        print("%s missed you!"%cret_breed)
        cret_hp = 0 #this closing loop
  if cret_hp <=0: #checking is creatorue won or lose
    print(f"{Fore.RED}%s is dead{Style.RESET_ALL}"% cret.breed)
  elif hero_hp <=0:
    print(f"{Back.RED}{Style.BRIGHT}{Fore.BLACK}YOU DIED!!!{Style.RESET_ALL}")
  #gain_exp()
  
  gain_exp() #after fight get health and exp
  input("Press enter to continue...")
  clean()

#game
clean()
print (f"You are a {Fore.YELLOW}HERO{Style.RESET_ALL} with initial {Fore.YELLOW}%s{Style.RESET_ALL} power and {Fore.YELLOW}%s{Style.RESET_ALL} health" %(hero_power, hero_hp))
print ("You have to fight with creatures, because you get in wrong place in wrong time")
print (f"{Back.BLUE}{Fore.WHITE}Rules are simple. Thanks to this fights you gain experience. \nAfter 10 points of experience you get level UP. \nYou retore some health after each fight or hide. \nYou restore 100% health afret level UP{Style.RESET_ALL}")
print ("Good luck")
print ("\n\n")

while still_alive(hero_hp) == True:
  cret = creature()
  print (f"{Fore.CYAN}{Style.BRIGHT}%s{Style.RESET_ALL} appears! What you do?" % cret.breed)
  decision = input (f"{Back.BLUE}{Fore.WHITE}Fight \"f\" \ hide \"h\" \ Give up \"g\": {Style.RESET_ALL}")
  
  if decision.lower() == "f":
    fight(cret.breed, cret.power, cret.hp)
  elif decision.lower() == "h":
    print ("You have 50% chance to hide...")
    if randint(0,1) == 1:
      print ("...but not this time")
      fight(cret.breed, cret.power, cret.hp)
    else:
      print ("You have luck! Creature walked away.")
  elif decision.lower() == "g":
    print (f"You've give up. But creature wasn't so kind. {Back.RED}{Style.BRIGHT}{Fore.BLACK}YOU DIED!!!{Style.RESET_ALL}")
    break
  else:
    print ('Wrong decision. Choose again: fight "y" retreat "r"')
  

print (creature.num_of_creatures)