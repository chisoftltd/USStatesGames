import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt=
    "What's another state's name?").title()

    if answer_state == 'Exit':
        with open("missed_states.csv", mode="w") as missed_state:
            for state in all_states:
                if state not in guessed_states:
                    new_missed_state = state + "\n"
                    missed_state.writelines(new_missed_state)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        file_state = data[data["state"] == answer_state]
        t.goto(int(file_state["x"].item()), int(file_state["y"].item()))
        t.write(f"{file_state['state'].item()}")


turtle.mainloop()
