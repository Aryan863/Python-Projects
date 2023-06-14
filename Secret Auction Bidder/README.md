<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Secret Auction Program</title>
</head>
<body>
  <h1>Secret Auction Program</h1>

  <h2>Description</h2>
  <p>
    This program allows you to run a secret auction by collecting bids from participants and determining the highest bidder.
  </p>

  <h2>Usage</h2>
  <p>
    To use the program, follow these steps:
  </p>
  <ol>
    <li>Run the program.</li>
    <li>Enter your name as a bidder.</li>
    <li>Enter your bid amount.</li>
    <li>If there are other bidders, type "Yes" when prompted to continue. Otherwise, type "No" to end the auction.</li>
    <li>View the winner of the auction and their bid amount.</li>
  </ol>

  <h2>Example</h2>
  <p>
    Here's an example usage of the program:
  </p>
  <pre>
    <code>
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

</code>

</pre>

<h2>Usage</h2>
    <p>To start the program, open a terminal or command prompt and run the following command:</p>
    <pre><code>python main.py</code></pre>

<h2>Contributing</h2>
    <p>Contributions are always welcome! If you have any suggestions or improvements, please create an issue or submit a pull request.</p>

<h2>License</h2>
    <p>This project is licensed under the <a href="LICENSE">MIT License</a>. Feel free to use and modify this code for your own purposes.</p>

<h2>Acknowledgements</h2>
    <p>This program was inspired Secret Auction program. Special thanks to the Python community for providing useful libraries and resources.</p>

<p>Enjoy the program!</p>
</body>
</html>
