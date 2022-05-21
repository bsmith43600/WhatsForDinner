from wfd_helpers import get_user_choice, print_recipe_list

def add_recipe(recipe_list, recipe_name = None, ingredients = {}):




    
    # Skip prompts if recipe name is in call (allows to hard-code recipe generation wihtout user inputs)
    if not recipe_name:
        # Print out recipe list
        print_recipe_list(recipe_list)

        # Allow user to cancel if recipe is already in list
        print("\nWould you like to add a recipe?")
        print("1. Yes     2. No")
        y_n_choice = get_user_choice(2)
        if y_n_choice == 2:
            return
        
        recipe_name = input("What is the name of the recipe you would like to add? ")
    
    # Skip prompts if recipe ingredients are in call
    if len(ingredients) < 1:
        # Prompt user to input ingredients one at a time
        ing_name = input('\nWhat is the first ingredient in {}? '.format(recipe_name)).title()
        ing_serv = float(input('\nHow many servings of {} are in {}? '.format(ing_name, recipe_name)))
        
        # Save ingredient as dictionary entry with name as key and number of servings as value. Servings are save as float
        # to allow for fractional servings.
        ingredients[ing_name] = ing_serv
        while True:
            print("{} requires:".format(recipe_name))
            for ing in ingredients:
                print("     {}: {} servings".format(ing, ingredients[ing]))
            print("\nAre there additional ingredients in {}".format(recipe_name))
            print("1. Yes     2. No")

            # Break loop when user indicates that they have entered all of the ingredients
            y_n_choice = get_user_choice(2)
            if y_n_choice == 2:
                break
            ing_name = input('\nWhat is the next ingredient in {}? '.format(recipe_name)).title()
            ing_serv = float(input('\nHow many servings of {} are in {}? '.format(ing_name, recipe_name)))
            ingredients[ing_name] = ing_serv
    
    # Add new recipe with ingredients to recipe_list dictionary
    recipe_list[recipe_name] = ingredients

    print("Your recipe list now contains {0}.".format(recipe_name))

    # Print out full recipe list
    print_recipe_list(recipe_list)

# Function to search for which recipes in the dictionary contain the input ingredient. Returns
# a list of recipe names.
def find_recipes_by_ingredient(recipe_list, ingredient):
    recipes_with_ingredient = []
    for recipe in recipe_list:
        if ingredient.title() in recipe_list[recipe]:
            recipes_with_ingredient.append(recipe)

    return recipes_with_ingredient


