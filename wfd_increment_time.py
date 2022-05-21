
def increment_time(fridge):
    try:
        time_to_elapse = int(input("\nHow many days would you like to elapse? "))
        if time_to_elapse < 1:
            print("\nPlease enter a number greter than 0")
            increment_time(fridge)

    except:
        print("\nPlease enter a number greater than 0")
        increment_time(fridge)

    for item in fridge.heap_list:
        if not item:
            continue

        item[0] -= time_to_elapse
    
    fridge.clean_fridge()


