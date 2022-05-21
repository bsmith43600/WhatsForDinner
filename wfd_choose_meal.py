
from wfd_helpers import *
import copy
from wfd_add_recipe import find_recipes_by_ingredient

def choose_meal(fridge, pantry, recipe_list):
    temp_fridge = copy.deepcopy(fridge)
    
    # Extract food heap for convenience
    food_heap = temp_fridge.heap_list

    # Intiate loop break variable as none
    ing_chosen = None
    # Loop until an ingredient is selected or there are no ingredients left.
    while not ing_chosen and len(food_heap) > 1:
        # Get expiration of top element in fridge:
        exp_check = food_heap[1][0]

        # Initiate ingredient to check queue. This queue will be used to store all indexes of ingredients needing a check for expiration
        idx_to_check_list = [1]

        # Initial ingredient options list
        ing_options = []

        # Check for children with same expiration:
        
        while len(idx_to_check_list) > 0:
            idx_to_check = idx_to_check_list[0]

            # If ingredient has the minimum expiration, add it to the options list
            if food_heap[idx_to_check][0] == exp_check:
                ing_options.append(food_heap[idx_to_check][1])

                # Only add children to idx_to_check list if current item is equal to expiration
                left_child = temp_fridge.get_left_child_idx(idx_to_check)
                right_child = temp_fridge.get_right_child_idx(idx_to_check)

                # Don't append None
                if left_child:
                    idx_to_check_list.append(left_child)
                if right_child:
                    idx_to_check_list.append(right_child)

            # Remove current index from idx_to_check queue
            idx_to_check_list.pop(0)

        ### Removed case handling for single ingredient - different formatting breaks flow of user input
        # Include special text if only one ingredient is found
        # if len(ing_options) == 1:
        #     print("\nYou have {} that expires in {} days.".format(ing_options[0], exp_check))
        #     print("\nWould you like to make a meal using {}?".format(ing_options[0]))
        #     print("1. Yes     2. No")
        #     y_n_choice = int(get_user_choice(2))
        #     if y_n_choice == 1:
        #         ing_chosen = ing_options[0]
                
        #     else:
        #         # If user rejects options, remove ingredient from temp_fridge, and call recursively
        #         for ing in ing_options:
        #             temp_fridge.remove_all_of_food(ing)

                
                
                
            
        #else:
        print("\nYou have...")
        item_count = 1
        for item in ing_options:
            print("{}. {}".format(item_count, item))
            item_count += 1
        print("{}. None of the above".format(item_count))
        print("...all expiring in {} days.".format(exp_check))
        print("\nWhich item would you like to cook with?")
        user_choice = get_user_choice(item_count)
        if user_choice < item_count:
            # Proceed to recipe options
            ing_chosen = ing_options[user_choice - 1]
        else:
            # Remove all ing_options
            for ing in ing_options:
                temp_fridge.remove_all_of_food(ing)

                    
    if len(food_heap) < 2:
        print("\nThat's all the food in your fridge.")
        print("Would you like to make a meal based on available pantry items?")
        print("1. Yes     2. No")
        y_n_choice = get_user_choice(2)
        if y_n_choice == 2:
            return
        else:
            print("\nYou have...")
            item_count = 1
            for item in pantry:
                print("{}. {}".format(item_count, item))
                item_count += 1
            print("{}. None of the above".format(item_count))
            print("\nWhich item would you like to cook with?")
            user_choice = get_user_choice(item_count)
            if user_choice < item_count:
                # Proceed to recipe options
                ing_chosen = list(pantry.keys())[user_choice - 1]
            else:
                return



    ppl_to_serve = int(input("\nHow many people are you cooking for? "))
    
    # Create list of all recipes which con
    possible_recipes = find_recipes_by_ingredient(recipe_list, ing_chosen)

    # Initialize offered_recipes list to track which recipes are actually presented to the user.
    offered_recipes = []

    recipe_count = 0
    for recipe in possible_recipes:
        # Use 'fridge' instead of 'temp_fridge' to check recipe ingredients - allows recipes to be presented even if
        # one of the ingredients had been previously rejected. Rejected ingredients are removed from 'temp_fridge'
        if has_all_ingredients(fridge, pantry, recipe_list[recipe], ppl_to_serve):
            recipe_count += 1

            offered_recipes.append(recipe)

            # If one recipe is found, print header
            if recipe_count == 1:
                print("\nUsing {}, you can make the following recipes for {} people: ".format(ing_chosen, ppl_to_serve))
            print("{}. {}".format(recipe_count, recipe))
        
    
    # If no recipes are found print message
    if recipe_count == 0:
        print("\nSorry, you don't have enough ingredients to serve {} people using {}".format(ppl_to_serve, ing_chosen))
        # choose_meal(temp_fridge, pantry, recipe_list)
        return
    
    recipe_count += 1
    print("{}. None of the above".format(recipe_count))

    print("\nWhat would you like to make?")
    user_choice = get_user_choice(recipe_count)
    if user_choice == recipe_count:
        return
    recipe = offered_recipes[user_choice - 1]

    if user_choice == recipe_count:
        return
    
    # Initiate fridge_food list
    fridge_foods = []
    fridge_needs = []

    # Loop through ingredients in recipe
    for item in recipe_list[recipe]:
        # Consume required quantity of item
        if item in pantry:
            # Reduce pantry servings by servings used. Because pantry items can be refilled, it is not necessary to remove empty items,
            print("Removing {} serving(s) of {} from your pantry".format(recipe_list[recipe][item] * ppl_to_serve, item))
            
            pantry[item] -= recipe_list[recipe][item] * ppl_to_serve

        else:
            # Add item to fridge_foods list. Code will pass list to consume foods and execute on all fridge foods
            # at the same time.
            fridge_foods.append(item)
            fridge_needs.append(recipe_list[recipe][item] * ppl_to_serve)
            print("Removing {} serving(s) of {} from your fridge.".format(recipe_list[recipe][item] * ppl_to_serve, item))


    # Remove cooked recipe foods from main fridge
    if len(fridge_foods) > 0:
        fridge.consume_food(fridge_foods, fridge_needs)


    


        
        
# Checks to see if fridge and/or pantry has enough ingredients to make requested recipe
def has_all_ingredients(fridge, pantry, ingredient_list, ppl_to_serve):
    for ing in ingredient_list:
        qty_needed = ingredient_list[ing]*ppl_to_serve
        
        # Check for ingredient in pantry
        if ing in pantry:
            if  qty_needed > pantry[ing]:
                return False
        else: 
            # Loop through fridge heap looking for ingredient
            for item in fridge.heap_list:
                # First item in heap will be 'none'
                if item is None:
                    continue
                # If item is found check if there are enough servings
                elif item[1] == ing:
                    if qty_needed <= item[2]:
                        qty_needed = 0
                        break
                    # If there isn't enough, continue searching to see if there is more of the item available
                    else:
                        qty_needed -= item[2]
                        continue
            
            # If qty_needed > 0, then there is not enough of the necessary ingredient, return false
            if qty_needed > 0:
                return False


    # If this line of code is reached, then there is enough of all the required ingredients to make the requested meal    
    return True




