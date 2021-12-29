import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")


data = pandas.read_csv("50_states.csv")
print(data)
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
file_state = data[data["state"] == answer_state]
print(file_state["x"], " ", file_state["y"])

turtle.goto(int(file_state["x"]), int(file_state["y"]))
turtle.write(f"{file_state['state']}")
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

