import os
from sys import int_info
from auctionArt import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
bids = {}

def find_highest_bidder(biding_record):
    highest_bid = -1
    winner = ""
    for bidder in biding_record:
        bid_amount = biding_record[bidder]
        if(bid_amount > highest_bid):
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and his bid was {highest_bid}")

biding_finished = False
while not biding_finished:
    name = input("Whats Your Name ?  ")
    price = int(input("Whats Your bid ?  "))
    bids[name] = price
    end = input("Are there any other bidders ")
    if end == "no":
        biding_finished = True
        find_highest_bidder(bids)
    elif end == "yes":
        os.system('cls')