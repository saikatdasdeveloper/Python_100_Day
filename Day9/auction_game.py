import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
logo = '''
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

bids= {}
continue_bid =  False
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not continue_bid:
   name = input("Enter your Name: \n") 
   price = input("What is your Bid Price? \n $")
   bids[name] = int(price)
   should_bid = input("Is there any Bidder left? Type Yes or No \n -->")
   if should_bid.lower() == "no":
      continue_bid = True
      find_highest_bidder(bids)
   elif should_bid.lower() == "yes":
      continue_bid = False
      cls()
    