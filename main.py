from turtle import Turtle, Screen
import pandas

#Screen
screen = Screen()
screen.title('U.S states game')
image = 'blank_states_img.gif'
screen.addshape(image)

#Background image
background = Turtle()
background.shape(image)

#CSV
data = pandas.read_csv('50_states.csv')
states = data['state'].tolist()
x_coor = data['x'].tolist()
y_coor = data['y'].tolist()

#Logic
write_states = Turtle()
write_states.color('black')
write_states.hideturtle()
write_states.penup()

#GAME
states_count = 0
is_game_on = True
while is_game_on:
    answer = screen.textinput(f'{states_count}/50', 'Name of a state:').capitalize()
    if answer == 'Exit':
        is_game_on = False

    answer_index = None
    answer_coords = None
    for state in states:
        if state == answer:
            answer_index = int(states.index(state))
            answer_coords = (x_coor[answer_index], y_coor[answer_index])
            states_count += 1
            write_states.goto(answer_coords)
            write_states.write(arg=f'{state}', font=('Arial', 11, 'normal'), align='center')
            states.remove(state)

missing_states = []
for state in states:            
    missing_states.append(state)
missing_dict = {
    'States': missing_states
}
    
data = pandas.DataFrame(missing_dict).to_csv('missing_states.csv')