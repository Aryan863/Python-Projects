import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "./US States Game/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.color("black")
writer.penup()

dataset = pd.read_csv("./US States Game/50_states.csv")
states = dataset["state"].to_list()
score = 0
guessed_states = []
missing_state = []

game_is_on = True

while game_is_on:

    answer_state = (screen.textinput(title=f"{score}/50 states correct", prompt="What's another State's name?")).title()
    if answer_state == "Exit":
        # storing unguessed states in csv file
        for state in states:
            if state not in guessed_states:
                missing_state.append(state)

        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("./US States Game/unguessed_states.csv") 
        break


    if answer_state in states:
        guessed_states.append(answer_state)
        state_data = dataset[dataset.state == answer_state]
        score+=1
        writer.goto(int(state_data.x),int(state_data.y))
        writer.write(f"{answer_state}")


