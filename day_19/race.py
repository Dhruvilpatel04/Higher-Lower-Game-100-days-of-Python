from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500, height= 400)

user_bet = screen.textinput(title="make ur bet !!!" , prompt=" which turtle will win the race ? choose a color:")
colors = ["red","orange","yellow","blue","purple","green"]
y_positions = [-70,-40,-10,10,40,70]
turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x= -230 , y = y_positions[turtle_index])
    turtles.append(new_turtle)


if user_bet:
    game_on = True
    
while game_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print("you win")
                game_on = False
            else: 
                print("you lose")
                game_on = False
          
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)
        
screen.exitonclick()