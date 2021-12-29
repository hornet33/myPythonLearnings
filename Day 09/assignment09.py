# Python program to simulate a secret auction

# Able to import utilities module from helpers package since PYTHONPATH env var is set to "myPythonLearnings" folder
from helpers import utilities


def get_highest_bidder(bid_dictionary):
    max_bid = 0
    max_bidder = ""
    for bidder in bid_dictionary:
        current_user_bid = bid_dictionary[bidder]
        if current_user_bid > max_bid:
            max_bid = current_user_bid
            max_bidder = bidder
    print(f"The highest bidder is {max_bidder} with a bid of ${max_bid}.")


user_bids = {}
more_bidders = 'yes'
while more_bidders == 'yes':
    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid: $"))
    user_bids[name] = bid  # Add the user and his/her bid to the dictionary
    more_bidders = input("Are there more bidders? Type 'yes' or 'no': ").lower()
    utilities.screen_clear()
get_highest_bidder(user_bids)
