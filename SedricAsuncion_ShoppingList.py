###########################################
#FP1-S04 Shopping List
#Sedric Asuncion
#
###########################################

## ----- Imports ----- ##
from time import sleep

## ----- Storage ----- ##

shopping_list = {}

## ----- Functions ----- ##

def add_item():
    while True:
        # Get user input for item and number of items
        item = input("Please enter item name: ").lower()
        try:
            num_items = int(input("Please enter the number of items: "))
            break
        except ValueError:
            print("Please enter a valid integer for the number of items.")

    # Get user input for the price of each item
    while True:
        price = input("Please enter the price of each item: ")
        try:
            price = float(price)
            break
        except ValueError:
            print("Please enter a valid number for the price of each item.")

    # Add item to the shopping list with specified quantity 
    shopping_list[item] = {'price': price, 'quantity': num_items}
    print(f"{num_items} {item}s have been added to your shopping list.")




def remove_item(): 
    while True:
        remove_item = input("\nPlease enter item name: (enter 'q' to quit) ").lower()

        if remove_item == "q":
            return
        elif remove_item in shopping_list:
            del shopping_list[remove_item]
            print(f"{remove_item} has been removed from your shopping list")
            break
        else: 
            print("Item not found in list")
            sleep(1)
            continue

def modify_item():
    while True:
        modify_item = input("\nPlease enter item name: (enter 'q' to quit) ").lower()

        if modify_item == "q":
            return
        elif modify_item in shopping_list:
            action = input("Would you like to add or remove items? (+/-): ")
            if action == "+":
                quantity = int(input(f"How many {modify_item} do you want to add? "))
                shopping_list[modify_item]['quantity'] += quantity
                print(f"{quantity} {modify_item} have been added to your shopping list")
                break
            elif action == "-":
                quantity = int(input(f"How many {modify_item} do you want to remove? "))
                shopping_list[modify_item]['quantity'] -= quantity
                if shopping_list[modify_item]['quantity'] <= 0:
                    del shopping_list[modify_item]
                    print(f"All {modify_item} have been removed from your shopping list")
                    break
                else:
                    print(f"{quantity} {modify_item} have been removed from your shopping list")
                    break
            else:
                print("Invalid action entered. Please try again.")
                sleep(1)
            continue
        else: 
            print("Item not found in list")
            sleep(1)
            continue



def clear_list(): 
    shopping_list.clear() 
    print("Your shopping list has been cleared") 


def show_list():
    if len(shopping_list) != 0:
        for item, details in shopping_list.items():
            if details['quantity'] > 2:
                total = details['price'] * details['quantity']
                print(f"{item} : {details['price']} (Quantity: {details['quantity']}, Total: ${total})")
            else:
                print(f"{item} : {details['price']} (Quantity: {details['quantity']})")
    else:
        print("Your shopping list is empty")



def add_total(): 
    total_cost = 0 
    total_items = 0 
    for item, details in shopping_list.items():
        total_items += details['quantity'] 
        total_cost += details['price'] * details['quantity']

    print(f"\nTotal items: {total_items} \nTotal cost: ${total_cost} ")
    # Create a function to make a total item count 


# Create a function for the user's options 
def user_options(): 
    # Print user options 
    sleep(1)
    print("""\nEnter 'A' to add an item,\n 'R' to remove an item,
 'S' to show the list,
 'M' to modify an item,
 'C' to clear the list,\n 'Q' to quit.""") 
    # Get user input for option 
    action = input("\nPlease enter an option: ").lower() 
    # Add item, remove item, or quit 
    if action == 'a': 
        add_item() 
    elif action == 'r':
        add_total()
        show_list()
        remove_item()
    elif action == 'm':
        add_total()
        show_list()
        modify_item()
    elif action == "s":
        add_total()
        show_list()
    elif action == "c":
        clear_list()
    elif action == 'q':
        add_total()
        quit() 
    else: 
        print("Invalid option")

## ----- Main Code ----- ##
        
while True: 
    user_options() 