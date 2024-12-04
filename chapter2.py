
import chapter1
import random

print("Chapter 2: Enemy Camp")
print("="*30)
print("June 18, 2075")
print("Planet: Nefarax")
print()
print("Arrived at the outskirts of the enemy camp there is treacherous terrain and it is being patrolled by hostile forces")
print("You land and you see many enemies in and out of the base")
print()
print(f"Your current HP: {chapter1.HP}")
print(f"Your current ammo: {chapter1.Ammo}")
print(f"Your current medkits: {chapter1.medkits}")
print()

def combat_choice():
    print("Do you want to go in loud or stealth?")
    print("1. Go in loud")
    print("2. Go in quiet")
    choice = input("> ").strip()
    print()

    if choice == '1':
        print("You start engaging in gunfire with your platoon and take out the enemies.")
        print()
        chapter1.HP -= 30
        chapter1.Ammo -= 50
    elif choice == '2':
        print("You decided to go in quiet and take them out one by one.")
        print()
        chapter1.HP -= 10
        chapter1.Ammo -= 0
    else:
        print("Invalid input, try 1 or 2.")
        print()

    print(f"Your current HP: {chapter1.HP}")
    print(f"Your current ammo: {chapter1.Ammo}")
    print()
    
    if chapter1.medkits > 0: 
        print("Do you want to use a medkit?")
        print("1. Yes")
        print("2. No")
        medkit_choice = input("> ").strip() 
        print()

        if medkit_choice == '1':
            print("You used a medkit.")
            print()
            chapter1.HP += 50
            chapter1.medkits -= 1
            print()
            print(f"Your current HP: {chapter1.HP}")
            print()
        elif medkit_choice == '2':
            print("You decided to save your medkit.")
            print()
            print(f"Your current HP: {chapter1.HP}")
            print()
        else:
            print("Invalid input! You didn't use a medkit.")
            print()
    else:
        print("You don't have any medkits left!")
        print()

def hacking_choice():
    print("After getting into the base, you find the server room. Do you want to hack into it?")
    print("1. Yes")
    print("2. No")
    choice = input("> ").strip()
    print()

    if choice == '1':
        print("You plug in your laptop to try and get the warlord's location and disable the alarm.")
        print()
        password = str(random.randint(100, 300))
        attempts = 6
        while attempts > 0:
            guess = input("Try and guess the password to get into the servers: ")

            if not guess.isdigit():
                print("Please enter a valid number!")
                continue

            if len(guess) != 3:
                print("Your guess must be a 3-digit number.")
                continue

            if guess == password:
                print("You successfully guessed the password! You now know where the warlord is located.")
                print("Your platoon heads back to the outpost to get ready to fight the warlord.")
                break
            else:
                attempts -= 1
                print(f"Wrong password! You have {attempts} attempts left.")

                correct_place = 0
                for i in range(len(guess)):
                    if guess[i] == str(password)[i]:
                        correct_place += 1

                print(f"Digits in the right place {correct_place} going from left to right: ")
                print()
        
        
        if attempts == 0:
            print("You've run out of attempts.")
            print ("Alarm has been tripped reinforcemtns are on there way!")
            print("You and your platoon fight them off.")
            print()
            chapter1.HP -= 15
            chapter1.Ammo -= 25
            print(f"Your current HP: {chapter1.HP}")
            print(f"Your current ammo: {chapter1.Ammo}")
            print()
            print("You head towards the next mission your general just assigned to you platoon but we still dont know where the warlord is located.")
            print()
    
    elif choice == '2':
        print("After looking around and finding nothing, you trip the alarm and hear reinforcements coming.")
        print("After fighting them off and taking some damage, your platoon starts heading out of the base.")
        print()
        chapter1.HP -= 15
        chapter1.Ammo -= 25
        print(f"Your current HP: {chapter1.HP}")
        print(f"Your current ammo: {chapter1.Ammo}")
        print()
        print("You head towards your next mission that the general just sent out.")
        print()
    else:
        print("Invalid input! Please choose 1 or 2.")


def main():
    combat_choice() 
    hacking_choice() 


main()