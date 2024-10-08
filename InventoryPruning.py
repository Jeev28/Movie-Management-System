'''
This module checks each game for pruning against certain conditions
1. Number of times it has been rented
2. The average feedback for that game
3. How many days it has been since it has last been rented
The pruning method is located in the menu.py module, as the bar chart had to be locally programmed to work.
'''


from datetime import date
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.animation as animation

'''
Description:
    The number_of_rents() function calculates how many times a game has been rented. 
Parameters:
    1. game_ID - this is done for each game in the Rental.txt file
Returns:
    Returns the rent count for that game
'''
def number_of_rents(game_ID):
    with open('Rental.txt','r') as rental_data:
        individual_line = rental_data.readlines()

        rent_count = 0
        for line in individual_line:
            line_split = line.strip().split(',')
            if line_split[0] == game_ID:
                rent_count += 1

    return rent_count

'''
Description:
    The game_feedback() function calculates the average feedback for a game, by searching through the 
    Game_Feedback.txt file, and finding the sum all scores for that game (total), and then dividing it by the number of 
    feedbacks that game has (number_of_feedbacks).
Parameters:
    1. game_ID - this is done for each game in the Rental.txt file
Returns:
    Returns the average feedback for each game. 
    In some cases where a game has no feedback, it produced a zero division error, 
    which is why it returns 0 in that case.
'''
def game_feedback(game_ID):
    with open('Game_Feedback.txt','r') as feedback_data:
        individual_line = feedback_data.readlines()
        #get parameters for avg = total sum/number of
        total = 0
        number_of_feedbacks = 0
        for line in individual_line:
            line_split = line.strip().split(',')
            if line_split[0] == game_ID:
                total += int(line_split[1])
                number_of_feedbacks +=1
        if number_of_feedbacks > 0:
            avg_feedback = total/number_of_feedbacks
        elif number_of_feedbacks == 0:
            return 0 #zero division error
        return avg_feedback

'''
Description:
    The game_date_difference() function calculates the differnece in days between the last time it was rented 
    and the current date. The datetime library was used to aid this function. 
Parameters:
    1. game_ID - this is done for each game in the Rental.txt file
Returns:
    Returns the difference between today and the last time it was rented. 
    Returns -1 if the game has never been rented. 
'''
def game_date_difference(game_ID):
    today = date.today().strftime("%d/%m/%Y")
    #format date into datetime
    today_datetime = datetime.strptime(today, "%d/%m/%Y")
    with open('Rental.txt','r') as rental_data:
        individual_line = rental_data.readlines()
        for line in reversed(individual_line):
            line_split = line.strip().split(',')
            if line_split[0] == game_ID:
                last_rent = line_split[1]
                a = datetime.strptime(last_rent,"%d/%m/%Y")
                difference = today_datetime - a
                #print(game_ID,"  ",difference.days)
                return difference.days #convert to days object
    return -1

