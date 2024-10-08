"""
This module provides a function used to search for games.
The database.py module is used to check if a game exists and is available
"""

import database as d


'''
Description:
    The search() function searches for a game by its title, genre, or platform in the Game_Info.txt file.
    It stores the games applicable in a list which is then printed. 
Parameters:
    1. choice - whether searching by title, genre, or platform.
    2. split_index - the index of the choice parameter in each line of the Game_Info.txt file.
Returns/Output:
    Prints a list of applicable games along with their availability status.
'''
def search(choice,split_index):
    games_found = []
    if d.game_exists(choice):
        #all games of title/platform/genre
        with open('Game_Info.txt','r') as sgi:
            individual_line = sgi.readlines()
            for line in individual_line:
                individual_line_split = line.split(',')
                if individual_line_split[split_index] == choice:
                    games_found.append(line)
            #availability of each game
            for games in games_found:
                games_split = games.split(',')
                is_available = d.availability(games_split[0])
                if is_available:
                    status = "Available"
                else:
                    status = "Unavailable"
                message = "Game Info: {} is {}"
                print(message.format(games.strip(),status))


def search_test():
    search("Call Of Duty",3)
    #prints games for call of duty - search by title
    search("Horror",2)
    #prints games with horror genre
    search("Playstation",1)
    #prints all games on playstation platform
    search("Bananas",2)
    #doesnt exist

if __name__ == "__main__":
    search_test()