<!DOCTYPE html>
<html>
<head>

</head>
<body>
  <h1>Caesar Cipher Program</h1>
  <img src="caesarCipher.png" alt="Caesar Cypher ">

  <h2>Description</h2>
  <p>
    This program implements the Caesar cipher encryption technique. It allows you to encode and decode messages by shifting the letters in the message by a specified number of positions.
  </p>

  <h2>Usage</h2>
  <p>
    To use the program, follow these steps:
  </p>
  <ol>
    <li>Run the program.</li>
    <li>Enter your choice: "Encode" to encrypt a message or "Decode" to decrypt a message.</li>
    <li>Enter the message you want to encrypt or decrypt.</li>
    <li>Enter the shift number, which determines the amount of shifting applied to each letter.</li>
    <li>View the result.</li>
    <li>If you want to run the program again, type "yes" when prompted; otherwise, type "no" to exit.</li>
  </ol>

  <h2>Example</h2>
  <p>
    Here's an example usage of the program:
  </p>
  <pre>
    <code>
from caesar_cipher_art import logo
import os

end = False
while not end :
os.system('cls') # To clear the terminal after each use(optional)
print(logo)
choice=input("Type 'Encode' to encrypt , Type 'Decode' to decrypt- ").lower()
message=input("Type your message- ").lower()
shift=int(input("Type the shift number- "))
#Prevents the user from entering the shift value greater than the number of alphabets
shift=shift%26

    if choice == "encode":
        new_message=""
        for i in range(len(message)):
            #checks if the letter is an alphabet. if Yes than encode it or else directly add it into the new string
            if message[i].isalpha():
                # % and addition is used to keep the encoded letters between 97 - 122(a-z)
                #ord() - used to get ASCII values of a particular character
                letter = (ord(message[i])+shift)%122

                #if shifted letters ascii value exceed 122, 97 is added to get it back in between the range of 97-122
                if letter==0:
                    letter+=97
                elif letter<97:
                    letter+=96

                #chr() - used to convert ascii values back to the corresponding characters
                new_message+=chr(letter)
            else:
                new_message+=message[i]

        print(f"Here's the result- {new_message}")

    elif choice == "decode":
        new_message=""
        for i in range(len(message)):
            if message[i].isalpha():
                letter = (ord(message[i])-shift)%122
                if letter==0:
                    letter+=97
                elif letter<97:
                    letter+=96

                new_message+=chr(letter)
            else :
                new_message+=message[i]

        print(f"Here's the result- {new_message}")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        end = True
        print("Goodbye")

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
    <p>This game was inspired by the Caesar Cipher encryption technique. Special thanks to the Python community for providing useful libraries and resources.</p>

<p>Enjoy the game!</p>
</body>
</html>
