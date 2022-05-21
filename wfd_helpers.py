# Function to collect integer input between 1 and num. Calls recursively until a valid input is returned.
from cmath import inf


def get_user_choice(num):
    try:
        user_choice = int(input("Enter number: "))
        if user_choice < 1 or user_choice > num:
            print("Please enter a number between 1 and {}".format(num))
            return get_user_choice(num)
        else:
            print("\033c") 
            return user_choice
    except:
        print("Please enter a number between 1 and {}".format(num))
        get_user_choice(num)

    


def display_all_ingredients(fridge, pantry):
    print(fridge)   
    print("\nYour pantry contains:")
    for food in pantry:
        print("{} - {} servings".format(food, pantry[food]))
    
def print_recipe_list(recipe_list):
    print("\nYour current recipe list is:\n")
    for key in recipe_list:
        print("{0}".format(key))
    
    

# Create FoodHeap class to manage food categories. FoodHeap is a min-heap in which each element is a list.
# The first item in the list is the expiry date of the food in days-until-expiration. The second element is
# the food name.
class FoodHeap:
    def __init__(self):

        # Initialize heap_list with "None" element. Heap_list at index 0 will always be None.
        self.heap_list = [None]

    def __repr__(self):
        out_string = "\nYour fridge currently has:\n"
        for idx in range(1, len(self.heap_list)):
            food = self.heap_list[idx]
            out_string += "{} - {} servings. Expires in {} days\n".format(food[1], food[2], food[0])
        
        return out_string
        

    # new_food is a list of the form: [expiry in days, food name, servings]
    def add_to_heap(self, new_food):
        # Add new food to back of heap_list
        self.heap_list.append(new_food)
        # Restore heap with new element
        self.heapify_up()

    def get_parent_idx(self, idx):
        return idx // 2
    
    # Return nothing if idx is out of range
    def get_right_child_idx(self, idx):
        if idx * 2 + 1 > len(self.heap_list)-1:
            return
        return idx * 2 + 1

    # Return nothing if idx is out of range
    def get_left_child_idx(self, idx):
        if idx * 2 > len(self.heap_list)-1:
            return
        return idx * 2

    # Heapify up to compare elements starting with the bottom element to move lowest expiry to the top
    def heapify_up(self):
        idx = len(self.heap_list) - 1

        while self.get_parent_idx(idx) > 0:
            current_element = self.heap_list[idx]
            parent_idx = self.get_parent_idx(idx)
            parent_element = self.heap_list[parent_idx]
            
            # If current element expires sooner than parent, swap current and parent elements
            if current_element[0] < parent_element[0]:
                self.heap_list[parent_idx] = current_element
                self.heap_list[idx] = parent_element
            idx = parent_idx
    
    def heapify_down(self):
        idx = 1

        # If left child is not none, continue loop
        while self.get_left_child_idx(idx):
            # Find smaller child and assign to smaller_child_idx
            left_child_idx = self.get_left_child_idx(idx)
            right_child_idx = self.get_right_child_idx(idx)

            if right_child_idx and self.heap_list[left_child_idx][0] > self.heap_list[right_child_idx][0]:
                smaller_child_idx = right_child_idx
            else: 
                smaller_child_idx = left_child_idx
            
            if self.heap_list[smaller_child_idx][0] <= self.heap_list[idx][0]:
                # If child is smaller than index, swap child and index
                temp = self.heap_list[idx]
                self.heap_list[idx] = self.heap_list[smaller_child_idx]
                self.heap_list[smaller_child_idx] = temp

                # Move index to new position
            idx += 1
            
    # food_list is a list of strings of food names needed. food_need is a correlated list of quantities required.
    def consume_food(self, food_list, food_need):
        # Search heap for lowest expiration of input food
        self.sort_self()
        food_heap = self.heap_list
        food_heap[1:].sort()

        fridge_idx = 1

        # loop_ends when all food needs are met
        while sum(food_need) > 0:

            # Loop through foods in food heap in order to grab ingredients in order of what will expire first
            current_food = food_heap[fridge_idx][1]
            if current_food in food_list:

                # See how much of the current food is needed
                current_food_need = food_need[food_list.index(current_food)]

                # If current food need is met, move on to next food
                if current_food_need <= 0:
                    pass

                # If current need is greater than or equal to current fridge item servings, then set servings to 0 and subtract
                # fridge quantity from neew
                elif current_food_need >= food_heap[fridge_idx][2]:
                    food_need[food_list.index(current_food)] -= food_heap[fridge_idx][2]
                    food_heap[fridge_idx][2] = 0
                
                else:
                    food_heap[fridge_idx][2] -= current_food_need
                    food_need[food_list.index(current_food)] = 0

            fridge_idx += 1

        self.clean_fridge()


            
                    
    def sort_self(self):
        new_heap = [None]
        old_heap = self.heap_list

        new_heap.append(old_heap.pop(1))

        while len(old_heap) > 1:
            self.heapify_down()
            new_heap.append(old_heap.pop(1))

        self.heap_list = new_heap

    def clean_fridge(self):
        items_to_remove = []
        
        # Loop through items, removing every item that has a quantity of 0 or less
        for item in self.heap_list:
            if not item:
                continue

            if item[2] <= 0 or item[0] <= 0:
                items_to_remove.append(item)
                if item[0] <= 0:
                    print("{} servings of {} have expired. Removing from fridge".format(item[2], item[1]))
            
        for item in items_to_remove:
            self.heap_list.remove(item)

        # Heapify down to re-establish heap structure
        self.heapify_down()



    def remove_all_of_food(self, food_to_remove):
        items_to_remove = []
        
        # Loop through items, removing every item that has a quantity of 0 or less
        for item in self.heap_list:
            if not item:
                continue

            if item[1] == food_to_remove:
                items_to_remove.append(item)
            
        for item in items_to_remove:
            self.heap_list.remove(item)

        # Heapify down to re-establish heap structure
        self.heapify_down()



    
