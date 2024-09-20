from random import randint

enemyMaxDmg = 50
enemyMinDmg = 5
enemyHitChance = 60
enemyHp = 100
enemyName = "The Janitor"

toyswordMaxDmg = 40
toyswordMinDmg = 20
toyswordHitChance = 80

rockMaxDmg = 100
rockMinDmg = 70
rockHitChance = 50

cactusMaxDmg = 150
cactusMinDmg = 100
cactusHitChance = 100

akMaxDmg = 1000
akMinDmg = 1
akHitChance = 50

pistolMaxDmg = 200
pistolMinDmg = 100
pistolHitChance = 80

def checkHealth(hp):
    if hp <= 0:
        return True
    else:
        return False
    
def backpack(toysword, rock, cactus, ak, pistol, healpotion):
    print("These are the items in your backpack:")
    if toysword:
        print("toy-sword")
    if rock:
        print("rock")
    if cactus:
        print("cactus")
    if ak:
        print("AK-47")
    if pistol:
        print("pistol")
    if healpotion:
        print("healing potion")
    
def combat(enemyName, enemyHp, enemyMaxDmg, enemyMinDmg, enemyHitChance, playerMaxDmg, playerMinDmg, playerHitChance, playerWeapon):
    global playerHp
    while True:
        print()
        print(f"{enemyName} has {enemyHp} Hp, and you have {playerHp} HP")
        input(f"Press ENTER to attack {enemyName}: ")
        
        if randint(0, 100) < playerHitChance:
            dmg = randint(playerMinDmg, playerMaxDmg)
            enemyHp -= dmg
            if enemyHp < 0:
                enemyHp = 0
                print()
            else:
                print()
            print(f"You hit {enemyName} with your {playerWeapon} for {dmg} damage, {enemyName} now has {enemyHp} HP")
        else:
            print()
            print("You missed your attack")

        if checkHealth(enemyHp):
            print(f"Congrats, you killed {enemyName}")
            win = True
            break
        
        input(f"Press ENTER to let {enemyName} attack: ")

        if randint(0, 100) < enemyHitChance:
            dmg = randint(enemyMinDmg, enemyMaxDmg)
            playerHp -= dmg
            if playerHp < 0:
                playerHp = 0
                print()
            else:
                print()
            print(f"{enemyName} hit you for {dmg} damage, you now have {playerHp} HP")
        else:
            print()
            print(f"{enemyName} missed his attack")

        if checkHealth(playerHp):
            print("You got killed")
            print()
            win = False
            break

    return(win)

def choice():
    while True:
        answer = input(": ").upper()
        if answer == "A" or answer =="B":
            break
        else:
            print("Invalid input, please try again")
    return(answer)

def prepare():
    global healpotion
    global playerHp
    global playerWeapon
    global playerMaxDmg
    global playerMinDmg
    global playerHitChance
    backpack(toysword, rock, cactus, ak, pistol, healpotion)
    if healpotion:
        print(f"Your HP is {playerHp}, do you want to use your healing potion? A = Yes B = No ->")
        answer = choice()
        if answer == "A":
            playerHp = 150
            healpotion = False
            print(f"You used the potion, you fully recovered and even gained some extra HP, your HP is now {playerHp}")
        elif answer == "B":
            print("You chose to not use the potion")
    print("You must choose a weapon to fight with")
    print()
    backpack(toysword, rock, cactus, ak, pistol, healpotion)
    while True:
        answer = input("What weapon do you want to use? ->").upper()
        if answer =="TOYSWORD" or answer == "TOY SWORD" or answer == "TOY-SWORD":
            print("You chose the toy-sword")
            playerWeapon = "toy-sword" 
            playerMaxDmg = toyswordMaxDmg
            playerMinDmg = toyswordMinDmg
            playerHitChance = toyswordHitChance
            break
        elif answer == "ROCK":
            print("You chose the rock")
            playerWeapon = "rock" 
            playerMaxDmg = rockMaxDmg
            playerMinDmg = rockMinDmg
            playerHitChance = rockHitChance
            break
        elif answer == "CACTUS":
            print("You chose the cactus")
            playerWeapon = "cactus" 
            playerMaxDmg = cactusMaxDmg
            playerMinDmg = cactusMinDmg
            playerHitChance = cactusHitChance
            break
        elif answer == "AK-47" or answer == "AK47" or answer == "AK 47" or answer == "AK":
            print("You chose the AK-47")
            playerWeapon = "AK-47" 
            playerMaxDmg = akMaxDmg
            playerMinDmg = akMinDmg
            playerHitChance = akHitChance
            break
        elif answer == "PISTOL":
            print("You chose the pistol")
            playerWeapon = "pistol" 
            playerMaxDmg = pistolMaxDmg
            playerMinDmg = pistolMinDmg
            playerHitChance = pistolHitChance
            break
        else:
            print("Invalid input, try again")
    print()
    print("The stats of your weapon are:")
    print(f"Max damage: {playerMaxDmg}")
    print(f"Min damage: {playerMinDmg}")
    print(f"Hit chance: {playerHitChance}")

def room1():
    global room1chest
    global cactus
    print()
    print("You walk through the door, and it's just a boring room")
    if room1chest:
        print("You see a chest, do you want to open it? A = yes B = no")
        answer = choice()
        if answer == "A":
            room1chest = False
            print("You opened the chest and found a cactus, you realize it can be used as a weapon")
            print("You put the cactus in your backpack")
            cactus = True
        elif answer == "B":
            print("You didn't open the chest")
    else:
        print("This room seems familiar, you see a opened chest")

    print("You see two doors in front if you, door A and door B, which do you choose? -> ")
    answer = choice()
    if answer == "A":
        room2()
    elif answer == "B":
        room3()

def room2():
    print()
    print("You walk through the door, and it's another room")
    print("You see two doors in front if you, door A and door B, which do you choose? -> ")
    answer = choice()
    if answer == "A":
        room4()
    elif answer == "B":
        room5()

def room3():
    global room3chest
    global ak
    global pistol
    print()
    print("You walk through the door, and you are now in a store")
    if room3chest:
        print("You are in an XXL")
        print("Do you want to scavange the store for stuff? A = yes B = no")
        answer = choice()
        if answer == "A":
            room3chest = False
            print("You look around and find the weapon section, you see a fully automatic AK-47, and a tiny pistol, which do you choose? A = AK-47 B = Pistol")
            answer = choice()
            if answer == "A":
                print("You chose the AK-47, you put the gun in your backpack")
                ak = True
            elif answer == "B":
                print("you chose the tiny pistol, you put it in your backpack")
                pistol = True
        elif answer == "B":
            print("You choose to not look for stuff")
    else:
        print("This room seems familiar, yes you are back at XXL")
    print("You see two doors in front if you, door A and door B, which do you choose? -> ")
    answer = choice()
    if answer == "A":
        room6()
    elif answer == "B":
        room7()

def room4():
    print()
    print("You walk through the door, and it's another room")
    print("You see two doors in front if you, door A and door B, which do you choose? -> ")
    answer = choice()
    if answer == "A":
        room1()
    elif answer == "B":
        room8()

def room5():
    global room5chest
    print()
    print("You walk through the door, and it's another room")
    if room5chest:
        print("You see a cardboard box on the floor, do you want to open it? A = yes B = no")
        answer = choice()
        if answer == "A":
            room5chest = False
            print("You opened the box, and it was empty")
            print("Your disapointment is immeasurable, and your day is ruined")
        elif answer == "B":
            print("You didn't open the box")
    else:
        print("This room seems familiar, you see a opened cardboard box on the floor")
    print("You see two doors in front if you, door A and door B, which do you choose? -> ")
    answer = choice()
    if answer == "A":
        room4()
    elif answer == "B":
        room6()

def room6():
    global room6chest
    global healpotion
    print()
    print("You walk through the door")
    if room6chest:
        print("You are now in a Subway")
        print("You are kind of hungry, but no one is working there of course, but you see a fridge in the back, do you want to open it? A = yes B = no")
        answer = choice()
        if answer == "A":
            room6chest = False
            print("You opened the fride and found a healing potion")
            print("You put the healing potion in your backpack")
            healpotion = True
        elif answer == "B":
            print("You didn't open the fridge")
    else:
        print("This room seems familiar, you see an opened fridge, yes you are back at Subway")

    print("You see two doors in front if you, door A and door B, which do you choose? -> ")
    answer = choice()
    if answer == "A":
        room5()
    elif answer == "B":
        room7()

def room7():
    print()
    print("You walk through the door, and it's another room")
    print("You see two doors in front if you, door A and door B, which do you choose? -> ")
    answer = choice()
    if answer == "A":
        room10()
    elif answer == "B":
        room1()

def room8():
    print()
    print("You walk through the door, and it's another room")
    print("This time there is only one door, you walk toward the door, but the closer you come, you start to notice a sound")
    print("You hear a monster of some sort on the other side")
    print()
    input("You should prepare for battle, press ENTER to look in your backpack ")
    print()
    prepare()
    print()
    input("You are now ready for combat, press ENTER to go through the door -> ")
    room9()

def room9():
    global playerWeapon, enemyName, playerHp, playerWeapon, playerMaxDmg, playerMinDmg, playerHitChance
    enemyHp = 1000
    enemyMaxDmg = 60
    enemyMinDmg = 10
    enemyHitChance = 60
    enemyName = "Jens Stoltenberg"
    print()
    print(f"You walk through the door with your {playerWeapon} in your hand, you are scared of what you will find on the other side, but you really want to leave Storo Storsenter, so you push through")
    print(f"On the other side there is no monster, but a handsome man is waiting for you, yes it is {enemyName}")
    print("But he doesen't look very friendly, he reaches for his knife and rushes towards you")
    print()
    input("Press ENTER to enter combat ->")
    win = combat(enemyName, enemyHp, enemyMaxDmg, enemyMinDmg, enemyHitChance, playerMaxDmg, playerMinDmg, playerHitChance, playerWeapon)
    if win:
        print()
    else:
        input("You sadly lost, press A to start over, or B to close the game")
        answer = choice()
        if answer == "A":    
            print()
            start()
        elif answer == "B":
            exit()

def room10():
    print()
    print("You walk through the door, and it's another room")
    print("This time there is only one door, you walk toward the door, but the closer you come, you start to notice a sound")
    print("You hear a monster of some sort on the other side")
    print()
    input("You should prepare for battle, press ENTER to look in your backpack ")
    print()
    prepare()
    print()
    input("You are now ready for combat, press ENTER to go through the door -> ")
    room9()

def start():
    global playerWeapon, playerMaxDmg, playerMinDmg, playerHitChance, toysword, toyswordMaxDmg, toyswordMinDmg, toyswordHitChance, rock, rockMinDmg, rockMaxDmg, rockHitChance, cactus, ak, pistol, healpotion, enemyName, enemyHp, enemyMaxDmg, enemyMinDmg, enemyHitChance, playerHp
    global room1chest, room3chest, room5chest, room6chest, room7chest
    playerHp = 100

    toysword = False
    rock = False
    cactus = False
    ak = False
    pistol = False
    healpotion = False

    room1chest = True
    room3chest = True
    room5chest = True
    room6chest = True
    room7chest = True

    print("You wake up at the toilets at Storo Storsenter, you don't feel very well, but you quickly piece together what has happened. You probably fell asleep here after you ate that massive sausage at 7eleven, hmm, never eating at 7eleven again you think to yourself.")
    print("But something is off, you hear no sound at all, Storo Storsenter is never this quiet. You check the clock and see that it is in the middle of the night! 03:14 it says.")
    print("You walk out of the toilets, and see the janitor staring at you, he does not look happy. You can see him reaching for his broom, and you realize he is going to attack you")
    print()
    print("in front of you, there is a toy-sword from Ringo and a rock, which one do you pick up and try to fight back with? A for toy-sword, B for rock")

    answer = choice()

    if answer == "A":
        print()
        print("You chose the toy-sword")
        print("The toy-sword has low damage, but high hit-chance")
        playerWeapon = "toy-sword" 
        playerMaxDmg = toyswordMaxDmg
        playerMinDmg = toyswordMinDmg
        playerHitChance = toyswordHitChance
        toysword = True

    elif answer == "B":
        print()
        print("You chose the rock")
        print("The rock has high damage, but low hit-chance")
        playerWeapon = "rock" 
        playerMaxDmg = rockMaxDmg
        playerMinDmg = rockMinDmg
        playerHitChance = rockHitChance
        rock = True

    while True:
        print()
        print("A to start combat, B to view your backpack -> ")
        answer = choice()
        if answer == "A":
            break
        elif answer == "B":
            print()
            backpack(toysword, rock, cactus, ak, pistol, healpotion)

    win = combat(enemyName, enemyHp, enemyMaxDmg, enemyMinDmg, enemyHitChance, playerMaxDmg, playerMinDmg, playerHitChance, playerWeapon)

    if win:
        print()
    else:
        input("You sadly lost, press A to start over, or B to close the game")
        answer = choice()
        if answer == "A":    
            print()
            start()
        elif answer == "B":
            exit()

start()

print(f"You killed {enemyName} and now you can finally escape, you see a door in front of you")
input("Press enter to walk through the door ->")

room1()

print()
print("With Jens Stoltenberg dead, you finally walk free")
print("You step outside, smell the fresh air but immediately get hit by a bus and dies")

print("Press A to play again, or B to close the game")
answer = choice()
if answer == "A":
    print()
    start()
elif answer == "B":
    exit()