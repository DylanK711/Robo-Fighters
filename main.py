import random
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