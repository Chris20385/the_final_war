
import chapter1
import chapter2
import random
import time
import sys

weapon = None

print("Chapter 3: Underground Base")
print("="*30)
print("June 20, 2075")
print("Planet: Nefarax")
print()
print("The dark underground base is dimly lit with flickering lights and the hue of holographic screens.")
print("The enemy base seems abandoned, but you go in to have a look around. Maybe try to find the informant.")
print()
print(f"Your current HP: {chapter1.HP}")
print(f"Your current ammo: {chapter1.Ammo}")
print(f"Your current medkits: {chapter1.medkits}")
print()

time.sleep(5)  

def find_informant():
    print("You make your way into the base to find the informant.")

    random_list = ['Locked cell', 'Interrogation room', 'On the ground']

    location = random.choice(random_list)
    print()

    print(f"You found the informant in the {location}.")
    print()

    if location == 'Locked cell':
        print("You shoot the lock off.")
    elif location == 'Interrogation room':
        print("You kick the door in and pick the lock off his hands.")
    elif location == 'On the ground':
        print("You pick the lock off his hands and legs.")
        print()

    print("The informant tells you where the warlord is located and how to disrupt his supply chain.")
    print("You make your way to the nearby base that is the main source of supply for the warlord.")
    print()

    time.sleep(10)  

def blow_up():
    print("You need to plant explosives near the base, but be careful it is heavily guarded.")
    print()
    timer = random.randint(20, 30)
    print(f"You have {timer} seconds to plant the bomb and get away before it detonates!")
    time.sleep(1)
    print()

    
    event = random.choice(["A guard is walking towards you! HIDE", "The bomb’s timer is malfunctioning! You need to fix it."])
    print(f"[Event] {event}")
    print()
    print("What will you do?")
    print("1. Hide from the guard")
    print("2. Fix the bomb timer")

    choice = input("> ").strip()
    print()

    if choice == "":
        print("You didn't make a choice in time!")
        print("Game Over! You do know you're supposed to make a choice, right?")
        sys.exit()

    if choice == '1':
        print("You crawl to cover. Watch out! You almost got caught!")
        timer -= 10
    elif choice == '2':
        print("You quickly fix the timer.")
        timer += 5
    else:
        print("Invalid input, try 1 or 2.")
        print()

    if timer > 0:
        print("You planted the bomb!")
        print("BOOM!")
    else:
        print("The bomb didn't detonate.")
        print("The enemy found the bomb, and now they are on high alert.")

def ready_up():
    print("You get ready to fight the warlord!")
    print()
    print("Do you want to pick a new weapon up?")
    print("HINT: THIS MAKES A DIFFERENCE IN THE BOSS FIGHT.")
    print("1. Yes")
    print("2. No")

    choice = input("> ").strip()
    print()

    if choice == '1':
        weapon_list = ['Plasma sniper', 'Plasma LMG', 'Plasma Shotgun']
        print("Choose your new weapon!")
        print("1. Plasma sniper")
        print("2. Plasma LMG")
        print("3. Plasma Shotgun")
        print()

        weapon = input("Enter the number of the weapon you want to pick: ").strip()
        print()

        if weapon == '1':
            print("You have chosen the Plasma sniper!")
            print()
        elif weapon == '2':
            print("You have chosen the Plasma LMG!")
            print()
        elif weapon == '3':
            print("You have chosen the Plasma Shotgun!")
            print()
        else:
            print("Invalid input, try 1, 2, or 3.")
            print()

    elif choice == '2':
        print("You decided not to pick up a new weapon and keep your old one.")
        print()
    else:
        print("Invalid input, please choose 1 or 2.")
        print()

        print("You get on your ship to finally go end this war once and for all.")
        print()

def main():
    find_informant() 
    blow_up()
    ready_up()


main()