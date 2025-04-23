import platform
import util
import ascii_art

current_os = platform.system()

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bid in bids:
        if bids[bid] > highest_bid:
            highest_bid = bids[bid]
            winner = bid

    print(f"\nThe winner is {winner} with a bid of ${highest_bid}")
    

print(ascii_art.gavel)

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("Enter your name: ")
    price = float(input("Enter your price: $"))

    bids[name] = price

    other_bids = input("Are there any other bids? [yes/no]: ").lower()

    if other_bids == "yes":
        util.clear_console(current_os)
    else:
        continue_bidding = False
        find_highest_bidder(bids)
