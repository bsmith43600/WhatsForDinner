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