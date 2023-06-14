from art import logo
import os

auction_entries=[]
def addEntry(name,bid):
    new_entry={}
    new_entry["name"]=name
    new_entry["bid"]=bid
    auction_entries.append(new_entry)

    # auction_entries.append({       **This can also work**
    #     "name":name,
    #     "bid":bid,
    # })

def highestBid():
    max_bid=0
    for entry in auction_entries:
        if entry["bid"]>max_bid:
            max_bid=entry["bid"]
            max_name=entry["name"]
    
    print(f"The winner is {max_name} with a bid of ${max_bid}")


end=False
while not end:
    os.system("cls")
    print(logo)
    print("Welcome to the secrect auction program")
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: "))
    addEntry(name,bid)
    cont=input("Are there any other bidders?. Type 'Yes' or 'No'").lower()

    if cont=="no":
        end=True

os.system("cls")
highestBid()



