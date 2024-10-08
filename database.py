'''
This module contains common functions used:
- Validate customer ID format
- Validate if customer exists
- Validate if game exists
- Validate if game is available
'''

'''
Description:
    The validate_customer_ID_format() function ensures the customer ID is a sequence of 4 lowercase letters.
Parameters:
    1. customer_ID - entered within the rent function
Returns:
    Returns bool - true if the format is correct, otherwise false
'''
def validate_customer_ID_format(customer_ID):
    if len(customer_ID) == 4:
        for letter in customer_ID:
            if ('a' <= letter <= 'z'):
                #print("Customer ID Valid Format")
                return True
            else:
                print("Customer ID Invalid - Can only contain letters")
                return False
    else:
        print("Customer ID Invalid Length")
        return False


'''
Description:
    The customer_ID_format() function ensures the customer exists within the Subscription_Info.txt file.
Parameters:
    1. customer_ID - entered within the rent function
Returns:
    Returns bool - true if the customer exists, otherwise false
'''
def customer_exists(customer_ID):
    with open('Subscription_Info.txt','r') as fsi:
        if customer_ID in fsi.read():
            #print("Customer ID Exists")
            return True
        else:
            print("Customer ID Doesn't Exist")
            return False


'''
Description:
    The game_exists() function ensures the game exists within the Game_Info.txt file.
Parameters:
    1. game - entered within the rent or return function 
Returns:
    Returns bool - true if the game exists, otherwise false
'''
def game_exists(game):
    with open('Game_Info.txt','r') as gsi:
        if game in gsi.read():
            #print("Game Exists")
            return True
        else:
            print("Game Doesn't Exist")
            return False


'''
Description:
    The availability() function ensures the game is available within the Rental.txt file.
    It loops through each line and checks if the last instance of that game has a return date.
Parameters:
    1. game_ID - entered by the user, the game to be rented or searched
Returns:
    Returns bool - true if the game is available, otherwise false
'''
def availability(game_ID):
    with open('Rental.txt','r') as rental_data:
        individual_line = rental_data.readlines()
        for line in reversed(individual_line):
            line_split = line.split(',')
            if line_split[0] == game_ID:
                if line_split[2].strip() == "":
                    #print("Game Not Available")
                    return False
                else:
                    #print("Game Available")
                    return True


#Unit Testing
def check_database():
    validate_customer_ID_format("ghjkl")
    #Invalid as too long
    validate_customer_ID_format("ghjl")
    #Valid as correct length - no print
    customer_exists("axvu")
    #Valid as customer exists - no print
    game_exists("asas19")
    #Valid as game exists - no print
    game_exists("hello")
    # Invalid as game doesn't exist
    availability("asas19")
    #Check rental file to see availability


if __name__ == "__main__":
    check_database()