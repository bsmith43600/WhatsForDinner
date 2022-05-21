# This program was created as a final project for the CS102: Data Structures and Algorithms course on Codecademy.
# The purpose of the program is to monitor the expiration of foods in the fridge and recommend meals based on
# what is going to expire next. It will initially present the user with 6 options - Get meal recommendation, Add food to fridge/pantry,
# Add recipe, Elapse time, Display available ingredients, and Display recipe list. 
# 
# 
# GET MEAL RECOMMENDATION:
#   This option will inform the user which meat or vegetable is going to expire next and suggest using it in a dish.
#   The user will have the option to reject the recommendation, if the do the function will continue to traverse the
#   meat and vegetable heaps until there are no options left. 
#
#   If the user chooses to use the ingredient, the program will search for recipes which include the ingredient, while verifying
#   that all of the necessary ingredients are available. The user will be presented with all of the recipe options that can be 
#   made with the ingredients in the fridge   
#
# ADD FOOD TO FRIDGE/PANTRY
#   Adding food to the fridge will store the input food, along with days until expiration
#   in the appropriate data structure. Data will be stored in min-heaps based on the food's expiration, such that the
#   next to expire is always on top. Meat and vegetables will be stored in separate heaps
# 
# ADD RECIPE
#   Allows the user to add new recipes to the recipes dictionary
#
# ELAPSE TIME
#   This option will traverse the ingredient heaps and decrement the days-until-expiration for all of the food stored.
#   In a real-life implementation this would not be a user option, but would be driven by a real-time clock. Given the purpose
#   and intent of this exercise, this implementation is more practical and useful.
#
# DISPLAY AVAILABLE INGREDIENTS
#   This will print all ingredients, expirations, and quantities of items in both the fridge and pantry.
#
# DISPLAY RECIPE LIST
#   This will print all the recipes contained in the recipe list.
#   
#   Originally created by Bryan Smith on 5/21/2022
#   A blog post discussing the development can be found at: https://medium.com/@bsmith4360/building-a-program-to-recommend-meals-based-on-food-expiration-1ff4ee745364



from wfd_helpers import *
from wfd_choose_meal import choose_meal    
from wfd_add_food import add_food
from wfd_add_recipe import *
from wfd_increment_time import increment_time


# Build fridge heap - the fridge heap is used to store all perishable foods. FoodHeap class is defined in helpers file.
fridge = FoodHeap()

# Build pantry dictionary - the pantry dictionary is used to store all non-perishable foods. A dictionary is more useful here
# as we are more likely to search by food name than any other property

pantry = {}

# Recipe list is a dictionary with the recipe names as keys and ingredients list as values. Initiate as empty
recipe_list = {}

# Add pre-filled recipes
add_recipe(recipe_list, "Bolognese", {"Ground Beef": 0.5, "Onion": 0.5,"Tomato": 0.5, "Pasta":1})
add_recipe(recipe_list, "BLT", {"Bacon": 1, "Lettuce": 0.1, "Tomato": 0.1, "Bread":1})
add_recipe(recipe_list, "Steak & Potatoes", {"Steak": 1, "Potato": 3})
add_recipe(recipe_list, "Potato Skins", {"Potato": 1, "Bacon": 1})
add_recipe(recipe_list, "Rice and Beans", {"Rice": 1, "Beans": 1})
add_recipe(recipe_list, "Noodles with a Side of Noodles", {"Pasta": 1.5})
add_recipe(recipe_list, "Egg Sandwich", {"Egg":1, "Bread":1, "Bacon":1, "Cheese":1})

# Stock fridge with foods call: add_food(fridge, pantry, name, perishable, servings, expiration)
add_food(fridge, pantry, "Onion", 1, 4, 3)
add_food(fridge, pantry, "Steak", 1, 3, 7)
add_food(fridge, pantry, "Potato", 1, 8, 14)
add_food(fridge, pantry, "Ground Beef", 1, 4, 6)
add_food(fridge, pantry, "Tomato", 1, 3, 5)
add_food(fridge, pantry, "Bacon", 1, 8, 4)
add_food(fridge, pantry, "Onion", 1, 4, 8)
add_food(fridge, pantry, "Steak", 1, 3, 2)
add_food(fridge, pantry, "Potato", 1, 8, 6)
add_food(fridge, pantry, "Ground Beef", 1, 4, 3)
add_food(fridge, pantry, "Tomato", 1, 3, 4)
add_food(fridge, pantry, "Bacon", 1, 8, 9)
add_food(fridge, pantry, "Cheese", 1, 15, 10)
add_food(fridge, pantry, "Cheese", 1, 5, 5)

# Stock pantry with foods
add_food(fridge, pantry, "rice", 2, 10)
add_food(fridge, pantry, "pasta", 2, 2)
add_food(fridge, pantry, "beans", 2, 3)
add_food(fridge, pantry, "sugar", 2, 50)
add_food(fridge, pantry, "Bread", 2, 10)


print("\033c")
print("\nWelcome to What's for Dinner!")

# Begin main function loop. Loop is terminated by break point when user indicates that the are done.
while True:
    print("\nWould you like to...")
    print("1. Get meal recommendation     2. Add food to fridge/pantry     3. Add recipe     4. Elapse time     5. Display available ingredients     6. Display recipe list")

    action_choice = get_user_choice(6)

    if action_choice == 1:
        choose_meal(fridge, pantry, recipe_list)
    
    elif action_choice == 2:
        add_food(fridge, pantry)

    elif action_choice == 3:
        add_recipe(recipe_list, None, {})

    elif action_choice == 4:
        increment_time(fridge)
    
    elif action_choice == 5:
        display_all_ingredients(fridge, pantry)

    elif action_choice == 6:
        print_recipe_list(recipe_list)

    print("\nWould you like to do something else?")
    print("1. Yes   2. No")

    is_done = get_user_choice(2)
    if is_done == 2:
        print("\n\nGoodbye!\n\n")
        
        break


