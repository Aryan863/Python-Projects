PLACEHOLDER = "[name]"

with open("./Mail Merge/Input/Names/invited_names.txt", mode="r") as names_file:
    invited_names = names_file.readlines()
    for i in range(0, len(invited_names)):
        invited_names[i] = invited_names[i].strip("\n")

with open ("./Mail Merge/Input/Letters/starting_letter.txt", mode="r") as letter_file:
    example_letter = letter_file.read()
 
for name in invited_names:
    with open(f"./Mail Merge/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        new_letter = example_letter.replace(PLACEHOLDER, name)
        file.write(new_letter)




