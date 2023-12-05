import turtle
import pandas


screen = turtle.Screen()
screen.title("US States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


def state_adder(x,y,answer_state):
    state_turtle = turtle.Turtle()
    state_turtle.hideturtle()
    state_turtle.penup()
    state_turtle.setpos(x,y)
    state_turtle.write(answer_state, align= 'center')


def guess_state():
    if len(correct_guesses) == 0:
        answer = screen.textinput(title="Guess the State", prompt="What's a state name?")
    else:
        answer = screen.textinput(title=f"{len(correct_guesses)}/50 Correct States", prompt="What's a state name?")
    return answer


correct_guesses = []
state_data = pandas.read_csv('50_states.csv')
states = state_data['state'].tolist()
while len(correct_guesses) < 50:
    answer_state = guess_state()
    answer_state = answer_state.title()

    if answer_state == "Exit":
        states_to_learn_list = []
        states_to_learn = {"state": states_to_learn_list}

        for state in states:
            if state not in correct_guesses:
                states_to_learn_list.append(state)

        new = pandas.DataFrame(states_to_learn)
        new.to_csv('states_to_learn.csv')
        break
    if answer_state in states:
        coordinates = state_data[state_data.state == answer_state]
        x = int(coordinates.x.iloc[0])
        y = int(coordinates.y.iloc[0])
        correct_guesses.append(answer_state)
        state_adder(x,y,answer_state)




