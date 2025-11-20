# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}
new_bidders = True
while new_bidders:
    bidders_name = input("What's you name?: ")
    bidders_bid = int(input("How much do you want to bid? $"))
    bids[bidders_name] = bidders_bid
    more_bidders = input("Are there any more bidders? Type 'yes' or 'no'.\n").lower()
    print("\n" * 100)
    if more_bidders not in {"yes", "no"}:
        print("Invalid input!")
        more_bidders = input("Are there any more bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "no":
        new_bidders = False

highest_bidder = ""
highest_bid = 0
for current_bidder, current_bid in bids.items():
    if current_bid > highest_bid:
        highest_bid = current_bid
        highest_bidder = current_bidder
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

