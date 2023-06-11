from caesar_cipher_art import logo
import os

end = False
while not end :
    os.system('cls')   # To clear the terminal after each use(optional)
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
    


