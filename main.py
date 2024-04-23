import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

score = 0
guessed_states = []

data = pd.read_csv("50_states.csv")
state_list = data.state.values

while len(guessed_states) < 50:
    state_guess = screen.textinput(title=f"{score}/50 States Guessed", prompt="Enter state name: ").title()

    if state_guess == "Exit":
        missing_states = data[~data.state.isin(guessed_states)]
        missing_states_list = missing_states.state.values

        for state in missing_states_list:
            state_df = missing_states[missing_states.state == state]

            writer.goto(x=int(state_df.x.iloc[0]), y=int(state_df.y.iloc[0]))
            writer.color("red")
            writer.write(f"{state}", align="center", font=("Arial", 7, "bold"))

        missing_states.state.to_csv("missed_states.csv")

        break

    if state_guess in state_list and state_guess not in guessed_states:
        score += 1
        guessed_states.append(state_guess)

        state_df = data[data.state == state_guess]

        writer.goto(x=int(state_df.x.iloc[0]), y=int(state_df.y.iloc[0]))
        writer.write(f"{state_guess}", align="center", font=("Arial", 7, "normal"))

screen.exitonclick()
