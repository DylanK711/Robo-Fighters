import random

class player:

    def __init__(self, name, health, attack, money):
        self.name = name
        self.health = health
        self.attack = attack
        self.money = money

playerInfo = player("", 50, 15, 20)

enemyInfo = [
    {
        "name:": "Roberto",
        "attack": random.randint(10, 14)
    },
    {
        "name:": "Amy Android",
        "attack:": random.randint(10,14)
    },
     {
        "name:": "Robo Trumble",
        "attack:": random.randint(10,14)
    }
]

#game functions
def randomNumber (min, max):
    """Generates a random number between minumum and maximum"""
    value = random.randint(min, max)
    return value

def fight_or_skip():
    """function to check if the player wants to fight or skip"""
    #ask player if they want to fight or run
    prompt_fight = input("Would you like to fight or skip? Enter fight or skip. ")

    #validate prompt_fight
    if prompt_fight == "" or prompt_fight == None:
        print("Invalid answer try again.")
        return fight_or_skip()
    
    #convert promptFight to all lowercase
    prompt_fight = prompt_fight.lower()

    if prompt_fight == "skip":
        #confirm player wants to skip
        confirm_skip = input("Are you sure that you want to skip? Enter yes or no.  ")
        #if yes leave fight
        if confirm_skip.lower() == "yes":
            print(playerInfo.name + " has decided to skip this fight. Goodbue!")
            #subtract money from playerMoney for skipping, but not < 0
            playerInfo.money = max(0, playerInfo.money - 10)
            #stop while() loop using a break, and enter next fight

            # return true if player wants to leave
            return True
        return False
    
def fight(enemy):
    """fight function(now with parameter for enemy objects, HP, AP, and name)"""
    #keep track of who goes first
    isPLayerTurn = True

    #randomly change who goes first
    if random.random() > 0.5:
        isPLayerTurn = False

    while playerInfo.health > 0 and enemy.health > 0:
        if isPLayerTurn:
            #ask player if they would like to fight or skip
            if fight_or_skip():
                break
            damage = random.randint(playerInfo.attack - 3, playerInfo.attack)

            #remove enemy health by subtracting dmg
            enemy.health = enemy.health - damage
            print(playerInfo.name + " attacked " + enemy.name + ". " + enemy.name + " now has " + str(enemy.health) + " health remaining.")

            #check enemy health
        if enemy.health <= 0:
            print(enemy.name + " has died.")

            #give player money for winning
            playerInfo.money = playerInfo.money + enemy.money

            print("You have " + str(playerInfo.money) + " gold.")

            #leave the loop since enemy is dead
            break
        else:
            damage = random.randint(enemy.attack - 3, enemy.attack)

            playerInfo.health = max(0, playerInfo.health - damage)

            print(enemy.name + " attacked " + playerInfo.name + ". " + playerInfo.name + " now has " + str(playerInfo.health) + " health remaining.")
        if playerInfo.health <= 0:
            print(playerInfo.name + " has died.")
            break
        else:
            print(playerInfo.name + " has " + str(playerInfo.health) + " health remainging.")
    
    isPLayerTurn = not isPLayerTurn
#end of fight function

#start a new game
def startGame():
    """Starts a new game"""
    playerInfo = player("", 50, 15, 20)
    playerInfo.name = input("What is your name? ")
    # fight the other enemy with loop and fighting them one at a time
    for enemy in range(0, len(enemyInfo)):
        if playerInfo.health > 0:
            #let them know what round they are on
            print("Wlecome to Robot Fighters Round " + str(enemy + 1))
            pickedEnemy = enemyInfo[enemy]

            #set enemy health
            pickedEnemy.health = randomNumber(40,60)

            fight(pickedEnemy)

            #if player is still alive and there are more enemies ask if they want to shop
            if playerInfo.health > 0 and enemy < len(enemyInfo) - 1:
                store_confirm = input("The fight is over, visit the store before next round?(y/n)    ")
                if "y" in store_confirm.lower():
                    shop(playerInfo)
        else:
            print("You lost, Game Over, L.")
            break


