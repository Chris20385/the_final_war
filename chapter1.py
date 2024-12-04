
HP = 100
Ammo = 150
medkits = 0

print("Chapter 1: The Small Outpost")
print("="*30)
print("June 18, 2075")
print("Planet: Nefarax")
print()
print("Dark skies and jagged cliffs surround you. You hear distant explosions and firepower throughout the valley.")
print("You can feel the tension in the air, and you are ready to fight in the war.")
print()
print(f"Your current HP: {HP}")
print(f"Your current ammo: {Ammo}")
print (f"Your current medkits: {medkits}")


def training_choice():
    global Ammo 
    print("\nDo you want to train with your weapon?")
    print("1. Yes")
    print("2. No")
    choice = input("> ").strip()
    print()

    if choice == '1':
        print("You walk over to the firing range to practice your aim.")
        print("After training, you swap out your pistol for a plasma rifle.")
        print("After doing some training, you feel dialed in.")

    elif choice == '2':
        print("This could be a big mistake.")
        print("You walk past the firing range and ignore it.")

    else:
        print("Invalid input, please enter 1 or 2.")
        training_choice() 


def platoon_choice():
    print("You make your way over to your platoon.")
    print("They are having a conversation, and you start listening in.")
    print()
    print("What do you want to do?")
    print("1. Have an informative conversation")
    print("2. Have a casual conversation")
    print()
    
    choice = input("> ").strip() 

    if choice == '1':
        print("You chose to have an informative conversation.")
        print("You learned that you will get deployed on a mission to gather intel.")
        print()
    elif choice == '2':
        print("You chose to have a casual conversation.")
        print("You talk about wondering if you will make it out of the war and live in peace again.")
        print()
    else:
        print("Invalid input, try 1 or 2.")
        platoon_choice()  
        print()

def explore():
    global Ammo, medkits
    print("Do you want to explore the outpost?")
    print("1. Yes")
    print("2. No")
    print()

    choice = input("> ").strip()  
    if choice == '1':
        print("After having a conversation, you decide to explore the outpost.")
        print("You walk into a supply tent and pick up 20 rounds of ammo and 1 medkit.")
        print("You make your way to the ship that will take you to your mission")
        print()

        print("Moving on to chapter 2: ")
        Ammo += 20
        medkits += 1  
        print()

    elif choice == '2':
        print("\nAfter having a conversation you head to the ship that will take you to your mission")
        print()

    else:
        print("Invalid input, try 1 or 2.")




def main():
    training_choice()  
    platoon_choice()   
    explore()      


main()
   