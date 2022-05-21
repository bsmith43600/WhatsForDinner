from wfd_helpers import *
from wfd_add_recipe import find_recipes_by_ingredient

def add_food(fridge, pantry, name = None, perish = None, servings = None, expiry = None):
    # Fridge - food heap of perishable items
    # Pantry - dictionary of non-perishable items
    # name - string name of food
    # perish - is food item perishable? 1 = perishable, 2 = non_perishable
    # servings - how many servings of the food are you adding?
    # expiry - days until food expires


    # Skip user prompts if values are input... allows for pre-stocking fridge
    if not name:
        display_all_ingredients(fridge, pantry)
        # Allow user to cancel if food is already in list
        print("\nWould you like to add a food?")
        print("1. Yes     2. No")
        y_n_choice = get_user_choice(2)
        if y_n_choice == 2:
            return

        name = input("What food are you adding? ")
    
    # Skip user prompts if values are input... allows for pre-stocking fridge
    if not perish:
        print("\nIs this {0} perishable?".format(name))
        print("1. Yes     2. No")
        perish = get_user_choice(2)
    
    if perish == 1:
        add_to_fridge(fridge, name, servings, expiry)
    elif perish == 2:
        add_to_pantry(pantry, name, servings)
        
    


def add_to_fridge(fridge, food_name, servings = None, expiry = None):
    # Skip user prompts if values are input... allows for pre-stocking fridge
    if not servings:
        # Prompt user to enter number of servings being added. Loop until input is valid
        while True:
            try:
                servings = float(input("\nHow many servings of {0} are you adding? ".format(food_name)))
                if servings <= 0:
                    print("\nInvalid input, please enter a number of servings")
                    continue
                break
            except:
                print("\nPlease enter a number of servings")
    
    # Skip user prompts if values are input
    if not expiry:
        # Prompt user to enter days until expiration. Loop until input is valid
        while True:
            try:
                expiry = int(input("\nIn how many days will {0} expire? ".format(food_name)))
                if expiry < 1:
                    print("\nInvalid input, please enter a number of days")
                    continue
                break
            except:
                print("\nPlease enter a number of days")

    # Build heap element to be inserted
    new_heap_element = [expiry, food_name, servings]
    fridge.add_to_heap(new_heap_element)
    print(fridge)

def add_to_pantry(pantry, food_name, servings = None):
    # Because there is no expiration on pantry items, if the item already exists, the
    # quantity of the existing item can be increased. Force all food names to title case
    # to prevent case sensitivity of inputs
    
    if not servings:
        # Prompt user to enter number of servings being added. Loop until input is valid
        while True:
            try:
                servings = float(input("\nHow many servings of {0} are you adding? ".format(food_name)))
                if servings <= 0:
                    print("\nInvalid input, please enter a number of servings")
                    continue
                break
            except:
                print("\nPlease enter a number of servings")
    
    if food_name.title() in pantry:
        pantry[food_name.title()] += servings
    else:
        pantry[food_name.title()] = servings

    print("\nYour pantry contains:")
    for food in pantry:
        print("{} - {} servings".format(food, pantry[food]))
    