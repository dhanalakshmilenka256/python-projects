from turtle import Turtle,Screen
screen=Screen()

'''def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
#HIgher order function is a function that work with another functions
def turn_right():
    new_heading=tim.heading()-10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.home()
screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")
#screen.onkey(turn_right,"d")#takes function with no arguments
screen.exitonclick()'''
import random
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="which turtle will win the race?Enter a color:")#textinput-
colors=["red","orange","green","blue","purple","yellow"]
y_pos=[-70,-40,-10,20,50,80]
all_turtles=[]
for turtle in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle])#goto-defines x value and y value
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_Color=turtle.pencolor()#set pencolor and fillcolor
            if winning_Color==user_bet:
                print(f"you've won! The {winning_Color} turtle is the winner")
            else:
                print(f"you've lost! The {winning_Color} turtle is the winner")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()