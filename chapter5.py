
import chapter1
import chapter2
import chapter3
import chapter4

print("Chapter 5: Warlords Base")
print("="*30)
print("June 20, 2075")
print("Planet: Nefarax")
print()
print("The sun begins to rise casting a warm light on the horizon.")
print("You can't believe it's all over—there is no more war.")
print()
print(f"Your current HP: {chapter1.HP}")
print(f"Your current ammo: {chapter1.Ammo}")
print(f"Your current medkits: {chapter1.medkits}")
print()

def help_choice():
    print("Do you want to help the injured people? ")
    print("1. Yes")
    print("2. No")
    print()

    choice = input("> ").strip()

    if choice == '1':
        print("You help out the injured and they thank you!")
        print()
    elif choice == '2':
        print("Wow, you are a terrible person.")
        print()
    else:
        print("Invalid input! Please choose 1 or 2")
        print()

def final_choice():
    print("Do you want to give a speech? ")
    print("1. Yes")
    print("2. No")
    print()

    choice = input("> ").strip()

    if choice == '1':
        print("You give your celebration speech and thank your team!")
        print()
    elif choice == '2':
        print("Now that the war is over, you go back to your town to reunite with your family.")
        print()
    else:
        print("Invalid input! Please choose 1 or 2")
        print()

def end_stats():
    print("These are your final stats: ")
    print(f"Your final health was: {chapter1.HP}")
    print(f"Your final ammo was: {chapter1.Ammo}")
    print("Thank you for playing!")

def main():
    help_choice()
    final_choice()
    end_stats()

main()
