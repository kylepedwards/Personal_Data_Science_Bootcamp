import os 


def band_name_generator():
    clear_terminal_screen = os.system("clear || cls")
    clear_terminal_screen

    user_home_town_input = input("\nEnter the name of your home town/city: ")
    pet_name_input = input("Enter your pet's name (or any pet name in general): ")

    print(f"\nYour band's name is: {user_home_town_input} {pet_name_input}s\n")


band_name_generator()