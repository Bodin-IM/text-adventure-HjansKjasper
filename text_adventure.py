from random import randint

def checkHealth(hp):
    if hp <= 0:
        return True
    else:
        return False


playerMaxDmg = 100
playerMinDmg = 10
playerHitChance = 90


enemyMaxDmg = 50
enemyMinDmg = 5
enemyHitChance = 70

enemyHp = 200
playerHp = 200

print("You are stuck at Storo Storsenter and you need to defeat the janitor to escape")

combat = True
while combat:
    print()
    print(f"The janitor has {enemyHp} Hp, and you have {playerHp} HP")
    input("Press ENTER to attack the janitor: ")
    
    if randint(0, 100) < playerHitChance:
        dmg = randint(playerMinDmg, playerMaxDmg)
        enemyHp -= dmg
        print()
        print(f"You hit the janitor for {dmg} damage, he now has {enemyHp} HP")
    else:
        print()
        print("You missed your attack")

    if checkHealth(enemyHp):
        print("Congrats, you killed the janitor")
        combat = False
        break
    
    input("Press ENTER to let the janitor attack: ")

    if randint(0, 100) < enemyHitChance:
        dmg = randint(enemyMinDmg, enemyMaxDmg)
        playerHp -= dmg
        print()
        print(f"The janitor hit you for {dmg} damage, you now have {playerHp} HP")
    else:
        print()
        print("The janitor missed his attack")

    if checkHealth(playerHp):
        print("You got killed")
        combat = False
        exit()

def room1():
    print("You walk through the door, and you see a sign, ROOM 1")
    valg = input("You see two doors in front if you, door A and door B, which do you choose? -> ").upper()
    while True:
        if valg == "A":
            room3()
        elif valg == "B":
            room2()
        else:
            print("Invalid input, try again")


def room2():
    print("You walk through the door, and you see a sign, ROOM 2")
    valg = input("You see two doors in front if you, door A and door B, which do you choose? -> ").upper()
    while True:
        if valg == "A":
            room1()
        elif valg == "B":
            room4()
        else:
            print("Invalid input, try again")


def room3():
    print("You walk through the door, and you see a sign, ROOM 3")
    valg = input("You see two doors in front if you, door A and door B, which do you choose? -> ").upper()
    while True:
        if valg == "A":
            room2()
        elif valg == "B":
            room5()
        else:
            print("Invalid input, try again")

def room4():
    print("You walk through the door, and you see a sign, ROOM 4")
    valg = input("You see two doors in front if you, door A and door B, which do you choose? -> ").upper()

def room5():
    print("You walk through the door, and you see a sign, ROOM 5")
    valg = input("You see two doors in front if you, door A and door B, which do you choose? -> ").upper()



print("You killed the janitor and now you can finally escape, you see 2 doors in front of you")
valg = input("Door A and door B, which do you choose? -> ").upper()

while True:
    if valg == "A":
        room1()
    elif valg == "B":
        room2()
    else:
        print("Invalid input, try again")


