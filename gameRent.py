"""
This module provides functions used to rent games.
The datetime library is used to get the current date.
The provided subscriptionManager module is used to check if customer has active sub.
The database.py module is used to check if a game exists and is available.
"""

import database as d
import subscriptionManager as sm
from datetime import date

'''
Description:
    The check_customer_subscriptions() function checks the type of subscription the 
    customer has (Basic or Premium). It then ensures that the customer has not 
    reached their subscription limit but looping the Rental.txt to find any instance where 
    they have rented a game with no return date (ie. not returned the game yet)
Parameters:
    1. game_ID - entered by the user, the game to be rented.
    2. customer_ID - entered by the user, the customer wanting to rent
Returns:
    Returns bool - true if the customer can rent a game (ie. not reached limit), otherwise false
'''
def check_customer_subscriptions(customer_ID, game_ID):
    with open('Subscription_Info.txt','r') as sub_info:
        #basic or premium subscription
        for line in sub_info.readlines():
            line_split = line.strip().split(',')
            if line_split[0] == customer_ID:
                customer_sub_type = line_split[1]
                #print(customer_sub_type)
                break

    if customer_sub_type == "Basic":
        max_rentals = 2
    elif customer_sub_type == "Premium":
        max_rentals = 7

    #check against limit
    customer_max_rentals = 0
    with open('Rental.txt','r') as rental_data:
        individual_line = rental_data.readlines()
        for line in individual_line:
            line_split = line.strip().split(',')
            if line_split[-1]==customer_ID and line_split[2]=="":
                customer_max_rentals+=1

    if customer_max_rentals >= max_rentals:
        print("Customer " + customer_ID + " cannot rent " + game_ID + " as rental limit reached")
        return False
    else:
        return True


'''
Description:
    The rent_game() function actually performs the rent functionality. It first checks they have 
    an active subscription, and then check if the game is available, and then if yes, it creates a new 
    line in the Rental.txt file. 
Parameters:
    1. game_ID - entered by the user, the game to be rented.
    2. customer_ID - entered by the user, the customer wanting to rent
Returns/Output:
    Writes to the Rental.txt file if the customer can rent, otherwise returns an error saying 
    they have an inactive subscription or the game is not available.
'''
def rent_game(customer_ID, game_ID):
    #get subscription - acitve or not
    subscriptions = sm.load_subscriptions('Subscription_Info.txt')
    subscriptionStatus = sm.check_subscription(customer_ID, subscriptions)
    #print("Customer has " + str(subscriptionStatus) + " subscription")

    #Add rent date
    if subscriptionStatus:
        if check_customer_subscriptions(customer_ID,game_ID):
            if d.availability(game_ID):
                rental_date = date.today().strftime("%d/%m/%Y")
                with open('Rental.txt','a') as rental:
                    rental.write("\n" + game_ID + "," + rental_date + "," + "," + customer_ID)
                    print("Customer " + customer_ID + " Rented Game " + game_ID)
    else:
        print("Customer " + customer_ID + " has Inactive Subscription")


def test_rent():
    check_customer_subscriptions("yhvn", "gbm03")
    #Invalid as customer has reached rental limit - will print this
    check_customer_subscriptions("qjqu","smsh14")
    #valid as customer has not reached rental limit - will print nothing

    rent_game("yhvn", "gbm03")
    #Invalid as customer has reached rental limit - will print this
    rent_game("cfrm", "smsh14")
    #Invalid as customer has inactive subscription - will print this
    rent_game("qjqu", "asas19")
    #Invalid as game unavailable - will not print this (this error is dealt with in menu)

if __name__ == "__main__":
    test_rent()