from random import randint

def checkHealth(hp):
    if hp <= 0:
        return True
    else:
        return False
    
toysword = False
rock = True

def backpack(toysword, rock):
    print("These are the items in your backpack:")
    if toysword:
        print("toy-sword")
    if rock:
        print("rock")
    
def combat(enemyName, enemyHp, playerHp, enemyMaxDmg, enemyMinDmg, enemyHitChance, playerMaxDmg, playerMinDmg, playerHitChance, playerWeapon):
    while True:
        print()
        print(f"The {enemyName} has {enemyHp} Hp, and you have {playerHp} HP")
        input(f"Press ENTER to attack the {enemyName}: ")
        
        if randint(0, 100) < playerHitChance:
            dmg = randint(playerMinDmg, playerMaxDmg)
            enemyHp -= dmg
            print()
            print(f"You hit the {enemyName} with your {playerWeapon} for {dmg} damage, the {enemyName} now has {enemyHp} HP")
        else:
            print()
            print("You missed your attack")

        if checkHealth(enemyHp):
            print(f"Congrats, you killed the {enemyName}")
            win = True
            break
        
        input(f"Press ENTER to let the {enemyName} attack: ")

        if randint(0, 100) < enemyHitChance:
            dmg = randint(enemyMinDmg, enemyMaxDmg)
            playerHp -= dmg
            print()
            print(f"The {enemyName} hit you for {dmg} damage, you now have {playerHp} HP")
        else:
            print()
            print(f"The {enemyName} missed his attack")

        if checkHealth(playerHp):
            print("You got killed")
            input("")
            win = False
            break

    return(playerHp, win)

playerHp = 100

print("You wake up at the toilets at Storo Storsenter, you don't feel very well, but you quickly piece together what has happened. You probably fell asleep here after you ate that massive sausage at 7eleven, hmm, never eating at 7eleven again you think to yourself.")
print("But something is off, you hear no sound at all, Storo Storsenter is never this quiet. You check the clock and see that it is in the middle of the night! 03:14 it says.")
print("You walk out of the toilets, and see the janitor staring at you, he does not look happy. You can see him reaching for his broom, and you realize he is going to attack you")
print()
while True:
    weaponChoose = input("in front of you, there is a toy-sword from Ringo and a rock, which one do you pick up and try to fight back with? A for toy-sword, B for rock -> ").upper()
    if weaponChoose == "A":
        print()
        print("you chose the toy-sword")
        print("The toy-sword has low damage, but high hit-chance")
        playerWeapon = "toy-sword" 
        playerMaxDmg = 40
        playerMinDmg = 20
        playerHitChance = 80
        toysword = True
        break
    elif weaponChoose == "B":
        print()
        print("you chose the rock")
        print("The rock has high damage, but low hit-chance")
        playerWeapon = "rock" 
        playerMaxDmg = 100
        playerMinDmg = 70
        playerHitChance = 50
        rock = True
        break
    else:
        print("Invalid input, try again")

enemyMaxDmg = 50
enemyMinDmg = 5
enemyHitChance = 60
enemyHp = 100
enemyName = "janitor"

while True:
    print()
    valg = input("A to start combat, B to view your backpack -> ").upper()
    if valg == "A":
        break
    elif valg == "B":
        print()
        backpack(toysword, rock)

combat(enemyName, enemyHp, playerHp, enemyMaxDmg, enemyMinDmg, enemyHitChance, playerMaxDmg, playerMinDmg, playerHitChance, playerWeapon)


def room1():
    print()
    print("You walk through the door, and you see a sign, ROOM 1")
    while True:
        valg = input("You see two doors in front if you, door A and door B, which do you choose? -> ").upper()
        if valg == "A":
            room3()
        elif valg == "B":
            room2()
        else:
            print("Invalid input, try again")

def room2():
    print()
    print("You walk through the door, and you see a sign, ROOM 2")
    while True:
        valg = input("You see two doors in front if you, door A and door B, which do you choose? -> ").upper()
        if valg == "A":
                room1()
        elif valg == "B":
                room4()
        else:
                print("Invalid input, try again")

def room3():
    print()
    print("You walk through the door, and you see a sign, ROOM 3")
    while True:
        valg = input("You see two doors in front if you, door A and door B, which do you choose? -> ").upper()
        if valg == "A":
            room2()
        elif valg == "B":
            room5()
        else:
            print("Invalid input, try again")

def room4():
    print()
    print("You walk through the door, and you see a sign, ROOM 4")
    while True:
        valg = input("You see two doors in front if you, door A and door B, which do you choose? -> ").upper()
        if valg == "A":
            room6()
        elif valg == "B":
            room1()
        else:
            print("Invalid input, try again")

def room5():
    print()
    print("You walk through the door, and you see a sign, ROOM 5")
    while True:
        valg = input("You see two doors in front if you, door A and door B, which do you choose? -> ").upper()
        if valg == "A":
            room7()
        elif valg == "B":
            room8()
        else:
            print("Invalid input, try again")

def room6():
    print()
    print("You walk through the door, and you see a sign, ROOM 6")
    while True:
        valg = input("You see two doors in front if you, door A and door B, which do you choose? -> ").upper()
        if valg == "A":
            room1()
        elif valg == "B":
            room10()
        else:
            print("Invalid input, try again")

def room7():
    print()
    print("You walk through the door, and you see a sign, ROOM 7")
    while True:
        valg = input("You see two doors in front if you, door A and door B, which do you choose? -> ").upper()
        if valg == "A":
            room9()
        elif valg == "B":
            room1()
        else:
            print("Invalid input, try again")

def room8():
    print()
    print("You walk through the door, and you see a sign, ROOM 7")
    while True:
        valg = input("You see two doors in front if you, door A and door B, which do you choose? -> ").upper()
        if valg == "A":
            room6()
        elif valg == "B":
            room1()
        else:
            print("Invalid input, try again")

def room9():
    print()
    print("You walk through the door, and you see a sign, ROOM 9")
    while True:
        valg = input("You see two doors in front if you, door A and door B, which do you choose? -> ").upper()
        if valg == "A":
            room1()
        elif valg == "B":
            room2()
        else:
            print("Invalid input, try again")

def room10():
    print()
    print("You walk through the door, and you see a sign, ROOM 10")
    print("But this time there is only one door, and it says EXIT")


print("You killed the janitor and now you can finally escape, you see 2 doors in front of you")
valg = input("Door A and door B, which do you choose? -> ").upper()

while True:
    if valg == "A":
        room1()
    elif valg == "B":
        room2()
    else:
        print("Invalid input, try again")