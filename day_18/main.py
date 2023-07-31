import turtle as t
from turtle import Screen
import random

Timmy = t.Turtle()
 
colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","Orange","Yellow","Pink"]
Timmy.speed("fastest")

def spiralgraph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        Timmy.color(random.choice(colors))
        Timmy.circle(100)
        Timmy.setheading(Timmy.heading() + size_of_gap)
    
spiralgraph(60)

    


screen = Screen()
screen.exitonclick()


