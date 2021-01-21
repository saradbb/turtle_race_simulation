from turtle import Turtle, Screen
import random
# A Turtle racing stimulation.

screen = Screen()
screen.setup(width = 500,height = 400)
user_choice = screen.textinput(title = "Make your bet", prompt = "Which color turtle will win the race")
print(user_choice)
initial_y_position = -100
X_POSITION = -250
X_FINISH_LINE = 200
current_y = -100
turtles = []
colors = ['green','black','blue','pink','yellow','orange','maroon']
finish = 0
winner = ''

def setup_racing_turtles():
    """
    Create new turtles, assign them colors and coordinates and get them ready for the race
    """
    global  current_y
    for i in range(0, 7):
        temp_turtle = Turtle()
        temp_turtle.shape('turtle')
        temp_turtle.color(colors[i])
        current_y += 30
        temp_turtle.penup()
        temp_turtle.goto(X_POSITION, current_y)
        temp_turtle.pendown()
        turtles.append(temp_turtle)

def draw_finish_line():
    # Draw the red line where the race ends
    line_drawer = Turtle()
    line_drawer.penup()
    line_drawer.goto(X_FINISH_LINE, current_y + 10)
    line_drawer.color('red')
    line_drawer.pendown()
    line_drawer.goto(X_FINISH_LINE, initial_y_position - 10)
    line_drawer.hideturtle()

def play():
    """
    The game runs until a turtle crosses the finish line. The turtle can make any move between 0-2 steps at a time
    :return:
    """
    global finish
    global X_FINISH_LINE
    global winner
    while finish == 0:
        for turtle in turtles:
            turtle.forward(random.randint(0, 3))
            if turtle.xcor() >= X_FINISH_LINE:
                finish = 1
                winner = turtle.color()


def result():
    global winner,user_choice
    if winner == user_choice:
        print(f"Congratulations, your selected winner {winner} won the race.")
    else:
        print(f"Oh no! {user_choice} lost! {winner[0]} won the race.")


setup_racing_turtles()
draw_finish_line()
play()
result()











screen.exitonclick()
