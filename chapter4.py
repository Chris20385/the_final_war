
import chapter1
import chapter2
import chapter3
import random
import sys

print("Chapter 4: Warlords Base")
print("="*30)
print("June 20, 2075")
print("Planet: Nefarax")
print()
print("The atmosphere is full of tension, storm clouds move in and thunder is heard.")
print("You're nervous for this fight; there is a lot on the line.")
print()
print(f"Your current HP: {chapter1.HP}")
print(f"Your current ammo: {chapter1.Ammo}")
print(f"Your current medkits: {chapter1.medkits}")
print()

def fight_enemies():
    print("What direction do you want to go?")
    print("1. Move forward")
    print("2. Go left")
    print("3. Go right")
    print()

    choice = input("> ").strip()

    if choice == '1':
        print("You take out all of the warlord's army.")
        print()
        chapter1.HP -= 40
        chapter1.Ammo -= 100
    
    elif choice == '2':
        print("You sneak by the warlord's army.")
        print()
        chapter1.HP -= 0
        chapter1.Ammo -= 0
    
    elif choice == '3':
        print("You only take out the enemies that are in your way.")
        print()
        chapter1.HP -= 10
        chapter1.Ammo -= 30

    else:
        print("Invalid input! Please choose 1, 2, or 3")
        print()
    
    if chapter1.medkits > 0:
        print("Do you want to use a medkit?")
        print("1. Yes")
        print("2. No")
        print()

        choice = input("> ").strip()

        if choice == '1':
            print("You used a medkit.")
            chapter1.HP += 25  
            chapter1.HP = min(chapter1.HP, 100) 
            chapter1.medkits -= 1
        elif choice == '2':
            print("It will come in handy later.")
        else:
            print("Invalid input. Please choose 1 or 2.")
    else:
        print("You have no medkits left.")
        print()

def final_fight():
    print("You finally come across the warlord.")
    print("It's time to end this!")

    chance = 50  

    
    if chapter3.weapon == "Plasma sniper":
        chance -= 5  
    elif chapter3.weapon == "Plasma LMG":
        chance += 20  
    elif chapter3.weapon == "Plasma Shotgun":
        chance += 10

    
    if chapter1.HP >= 75:
        chance += 25  
    elif chapter1.HP >= 50:
        chance += 15  
    elif chapter1.HP < 25:
        chance -= 15  

    
    chance = max(0, min(100, chance))
    print()

    print(f"Your chance to defeat the warlord is {chance}%")

    success_chance = random.randint(1, 100)
    if success_chance <= chance:
        print()
        print("You have defeated the warlord!")
    else:
        print("The warlord defeated you.")
        sys.exit() 

def main():
    fight_enemies() 
    final_fight()

main() 
