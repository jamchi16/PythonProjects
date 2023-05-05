import time
import random

weapon = False
Francisco = False
key_ring = False
orb_of_revealing = False
memories = False
fizzychips = False
goblin = True
skeleton = True
gargoyle = True
name = ""

def startroom():
    directions = ["forward", "backward", "left", "right"]
    print("You notice 4 doors, one in each direction, where would you like to go?")
    userinput = ""
    while userinput not in directions:
        print("Options: forward, backward, left, or right.")
        userinput = input()
        if userinput == "forward":
            room_A1()
        elif userinput == "backward":
            room_A7()
        elif userinput == "left":
            room_A4()
        elif userinput == "right":
            room_A5()
        else:
            print("That wasn\'t an option ya dingus.")

def room_A1 ():
    directions = ["forward", "backward", "left"]
    print("You entered another room and you notice 3 doors, one going forwards, one backwards, and one left, where would you like to go?")
    userinput = ""
    while userinput not in directions:
        print("Options: forward, backward, or left.")
        userinput = input()
        if userinput == "forward":
            room_A2()
        elif userinput == "backward":
            startroom()
        elif userinput == "left":
            room_A3()
        else:
            print("That wasn\'t an option ya dingus.")

def room_A2():
    global weapon
    global goblin
    if goblin:
        print("You entered another room and you see a goblin to your left snoozing in front of a jail cell.")
        time.sleep(2)
        print("What action would you like to take?")
        directions = ["go backwards","fight","sneak past"]
        userinput = ""
        while userinput not in directions:
            print("Options: go backwards, fight, sneak past")
            userinput = input()
            if userinput == "go backwards":
                room_A1()
            elif userinput == "fight":
                if weapon:
                    print("You slice the goblin in half and approach the door to the jail cell.")
                    goblin = False
                    jail_cell()
                else:
                    print("You try to punch the goblin as he's sleeping, but he wakes up and stabs you.")
                    print("You fall over and lose consciousness.")
                    game_over()
            elif userinput == "sneak past":
                stealth_check = random.randint(0,1)
                if stealth_check == 1:
                    print("You sneak past the goblin.")
                    jail_cell()
                else:
                    print("You trip over the goblin and he wakes up and stabs you.")
                    game_over()
            else:
                print("That wasn\'t an option ya dingus.")
        else:
            print("You see a jail cell to the left.")
            directions = ["go backwards", "jail cell"]
            userinput = ""
            while userinput not in directions:
                print("Options: go backwards, jail cell")
                userinput = input()
                if userinput == "go backwards":
                    room_A1()
                elif userinput == "jail cell":
                    jail_cell()
                else:
                    print("That wasn\'t an option ya dingus.")

def jail_cell ():
    global key_ring
    global memories
    global fizzychips
    global name
    if fizzychips:
        print("This is a jail cell. You return to the previous room.")
        room_A1()
    else:
        if key_ring:
            print("You unlock the door using a key on the key ring you found and walk inside.")
            if memories:
                print("You walk inside, see Francisco chained to a wall, and unlock him with one of the keys.")
                time.sleep(1)
                print(
                    "Fizzy Chips! I\'ve been looking all over for you! Quick! Lets get out of here before more monsters come!")
                time.sleep(1)
                print(f"Fizzy Chips responds, \" Its so good to see you {name}. I agree, as much as I love BDSM, chains, and my wife\'s feet, ")
                print("this has all been a little much. ")
                print("I\'m right behind you!")
                fizzychips = True
                room_A2()
            else:
                print("You walk inside and see a man chained to the wall.")
                time.sleep(1)
                print("As you approach him, he exclaims, \" Oh thank god you're alive!\"")
                time.sleep(2)
                print("You ask the man,\"Who are you and how do you know who I am?\"")
                time.sleep(2)
                print(f"He responds, \"C\'mon {name}! You remember Fizzy Chips! I play Lillia top lane in League of legends!")
                print("uwu XD\"")
                time.sleep(2)
                print("Idk, seems weird, lets get out of here.")
                fizzychips = True
                room_A2()
        else:
            print("The jail cell door is locked. You return to the previous room.")
            room_A1()

def room_A3():
    global weapon
    global skeleton
    global orb_of_revealing
    if skeleton:
        print("You entered another room and you see an animated skeleton walking around a chest")
        print("What action would you like to take?")
        directions = ["go backwards", "fight", "sneak past"]
        userinput = ""
        while userinput not in directions:
            print("Options: go backwards, fight, sneak past")
            userinput = input()
            if userinput == "go backwards":
                    room_A1()
            elif userinput == "fight":
                    if weapon:
                        print("You slice apart the skeleton and approach the chest. You open it and look inside and find an Orb of Revealing.")
                        print("You pickup the orb and head back to the previous room.")
                        orb_of_revealing = True
                        skeleton = False
                        room_A1()
                    else:
                        print("You try to punch the skeleton, but the skeleton ignores your punch and tears out your throat.")
                        print("You fall over and lose consciousness.")
                        game_over()
            elif userinput == "sneak past":
                stealth_check = random.randint(0, 1)
                if stealth_check == 1:
                        print("You sneak past the skeleton, grab the chest, and run out.")
                        print("As you are leaving the room you see that there is an Orb of Revealing in the chest.")
                        orb_of_revealing = True
                        room_A1()
                else:
                        print("You trip over your own feet like an idiot, the skeleton catches you and rips out your throat.")
                        game_over()
            else:
                    print("That wasn\'t an option ya dingus.")
    else:
        print("It is an empty room.")
        room_A1()
def room_A4():
    global weapon
    if not weapon:
        print("You entered another room and you walk in and and see a sword on the ground")
        time.sleep(1)
        print("However, try as you might, you are unable to pick it up.")
        time.sleep(1)
        print("Suddenly a text appears on the blade: \"To pick me up, write the name of my owner on the hilt\"")
        password = input("Write the name of the owner: ")
        if password == "fizzychips":
            print("You pickup the sword and leave the room.")
            weapon = True
            startroom()
        else:
            print("The sword does not budge and you leave the room.")
            startroom()
    else:
        print("The room is empty and you return to the previous room.")
        startroom()

def room_A5 ():
    global gargoyle
    global memories
    if gargoyle:
        print("You entered another room and you walk in and see a stone gargoyle.")
        time.sleep(2)
        print("As you approach the gargoyle you see it is clutching a journal that you faintly recognize.")
        time.sleep(2)
        print("Try as you might, you are unable to free the journal.")
        time.sleep(2)
        print("As you struggle, the gargoyle statue begins to stir and shake.")
        time.sleep(2)
        print("Suddenly, the gargoyle comes to life! The gargoyle then says: ")
        print("If you want this journal answer this riddle!")
        riddle_answer = input("What has hands, but cannot clap? (single word): ")
        if riddle_answer == "clock":
            print("That is correct! Here is the journal. The statue crumbles to dust.")
            time.sleep(2)
            print("You pickup the journal and it says, \"fizzychip\'s journal\".")
            print("As you read it, the memories of you and your adventure partner come flooding back to you.")
            time.sleep(2)
            print("You also notice a line that says, the name to pickup my sword is: fizzychips")
            time.sleep(2)
            print("You realize that the scream you heard earlier was his scream, you must find him.")
            time.sleep(2)
            print("You leave the way you came in.")
            gargoyle = False
            memories = True
            startroom()
        else:
            print("Incorrect!")
            print("A gust of wind from the gargoyle's mouth pushes you back out the door.")
            startroom()
    else:
        print("You see a pile of dust where the gargoyle was. You leave the room.")
        startroom()

def room_A7():
    global key_ring
    global orb_of_revealing
    if orb_of_revealing:
        directions = ["forward", "backward", "left","right"]
        print("You walk in the room and the Orb of Revealing shines brightly!")
        print("You now see 4 doors, one going forwards, one backwards, one right, and one left, select a direction.")
        userinput = ""
        while userinput not in directions:
            print("Options: forward, backward, left, or right.")
            userinput = input()
            if userinput == "forward":
                startroom()
            elif userinput == "left":
                print("You walk in the room and suddenly arrows fly straight at you!")
                time.sleep(0.5)
                print("You jump to evade the arrows!")
                time.sleep(2)
                dodge = random.randint(1,4)
                if dodge >= 2:
                    print("You weren't quick enough and got hit with multiple arrows and died.")
                    game_over()
                else:
                    print("You dodged the arrows! Too bad the room\'s empty. You leave the room.")
                    room_A7()
            elif userinput == "right":
                if not key_ring:
                    print("You walk in the room and find a key ring lying on the ground and leave the room.")
                    key_ring = True
                    room_A7()
                else:
                    print("You walk into an empty room and leave the way you came.")
                    room_A7()
            elif userinput == "backward":
                exit_door()
            else:
                print("That wasn\'t an option ya dingus.")
    else:
        print("You entered another room and you notice a door off to the left.")
        directions = ["forward", "left"]
        userinput = ""
        while userinput not in directions:
            print("Options: forward or left.")
            userinput = input()
            if userinput == "forward":
                startroom()
            elif userinput == "left":
                print("You walk in the room and suddenly arrows fly straight at you!")
                time.sleep(0.5)
                print("You jump to evade the arrows!")
                time.sleep(2)
                dodge = random.randint(1, 4)
                if dodge >= 2:
                    print("You weren't quick enough and got hit with multiple arrows and died.")
                    game_over()
                else:
                    print("You dodged the arrows! Too bad the room\'s empty. You leave the room.")
                    room_A7()
            else:
                print("That wasn\'t an option ya dingus.")

def exit_door():
    print("You open the door to stairs that lead out of the dungeon!")
    global fizzychips
    global memories
    global name
    if fizzychips and memories:
        print(f"{name} and fizzychips made it out alive! Congratulations, you escaped The Depths!")
        quit()
    elif fizzychips and not memories:
        print(f"{name} and the weird uwu Lillia main leave. I guess you win?")
        quit()
    elif not fizzychips and memories:
        choice = input("You have not found Fizzy Chips yet, are you sure you want to leave? (y/n)")
        if choice == "y":
            print(f"Woooooow, who knew {name} was such a fake friend.")
            print("Too bad I\'m a decent human being so I\'m not letting you leave without him!")
            room_A7()
        elif choice == "n":
            print("You decide not to leave and return to find Fizzy Chips.")
            room_A7()
        else:
            print("That wasn\'t an option ya dingus.")
    elif not fizzychips and not memories:
        print("You should probably find out where that scream came from first.")
        room_A7()

def game_over ():
    print(f"{name} has died, GAME OVER.")
    quit()


def introscene():
    global name
    print("You wake up in a dimly lit room.")
    time.sleep(2)
    print("As you sit up you, you feel the cold, damp air on your skin as the smell of mold and mildew hits you.")
    time.sleep(2)
    name = input("You blink a couple times and think to yourself, what was my name again? ")
    time.sleep(2)
    print(f"Ah! thats right, my name is {name}.")
    time.sleep(2)
    print("You here a scream off in the distance, followed by footsteps, but you can\'t seem to pinpoint the sound's source.")
    time.sleep(2)
    print("\" Well\", you think to yourself, \"time to get moving I guess.\"")
    time.sleep(2)
    print("You stand up, stretch and look around.")
    startroom()

print("Welcome to THE DEPTHS. I hope you can make it out alive!")
time.sleep(2)
introscene()