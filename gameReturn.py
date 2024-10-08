"""
This module provides a function used to return games.
The datetime library is used to get the current date.
"""

from datetime import date

'''
Description:
    The return_game() function searches for a game by its ID and then assigns it's
    return date to the current date. The file is rewritten completely to update it. 
    Validity checks are completed in the related function in the menu.py module.
Parameters:
    1. game_ID - entered by the user, the ID of the game to be returned
Returns/Output:
    Updates the Rental.txt file with the return date of the game returned.
'''
def return_game(game_ID):
    with open('Rental.txt','r') as rental_data:
        individual_line = rental_data.readlines()

        updated_line = []
        for line in individual_line:
            line_split = line.strip().split(',')
            if line_split[0] == game_ID and line_split[2] == "":
                line_split[2] = date.today().strftime("%d/%m/%Y")
                updated_line.append(','.join(line_split) + '\n')
                print("Game " + game_ID + " Returned")
            else:
                updated_line.append(line)

    with open('Rental.txt','w') as rental_data:
        rental_data.writelines(updated_line)



def return_game_test():
    return_game("gbm03")
    #prints nothing - game already returned - this error dealt with in menu
    return_game("smsh14")
    #returns game

if __name__ == "__main__":
    return_game_test()


