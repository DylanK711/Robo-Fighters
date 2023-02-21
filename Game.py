
playerAttack = 10
playerHealth = 100
playerName = input("Enter your robots name:  ")
playerMoney = 10

print(playerName, playerAttack, playerHealth)

enemyNames = ["Bill", "Bob", "Bobby", "Bab", "Bib"]
enemyHealth = 50
enemyAttack = 12

def fight(enemy):
    
    print("The fight has begun")

    global enemyHealth
    global playerAttack
    global playerName
    global playerHealth
    global enemyAttack
    global playerMoney

    while enemyHealth > 0:
        prompt_fight = input("Would you like to fight or run? (enter 'fight' or 'run')  ")
        if prompt_fight == "fight"  or prompt_fight == "FIGHT":
            print("you have chosen to fight!")

            enemyHealth = enemyHealth - playerAttack
            print(playerName + " attacked " + enemyName +".")

            if enemyHealth == 0:
                print(enemyName + " is dead!")
            else:
                print(enemyName + " is alive.")

            print(enemyName + " now has " + str(enemyHealth) + " health remaining.")

            playerHealth = playerHealth - enemyAttack

            print(enemyName + " attacked " + playerName +".")
            print(playerName + " now has " + str(playerHealth) + " health remaining.")

            if playerHealth == 0:
                print(playerName + " is dead.")
            else:
                print(playerName + " is alive!")
        elif prompt_fight == "run" or prompt_fight == "RUN":
            confirm = input("Are you sure you want to run?  ")
            if confirm == "yes" or confirm == "YES":
                playerMoney = playerMoney - 2
                print("You chose to run. You have " + str(playerMoney) + " money left. ")
            else:
                fight()

        else:
            print("Invalid option, try again.")
    


for (enemyName) in enemyNames:
    fight(enemyName)


