from turtle  import Turtle
start_position = [(0,0),(-20,0),(-40,0)]
moving_distance = 20
up = 90
down = 270
left = 180
right = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in start_position:
            self.add_segment(position)
            

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(moving_distance)
    
    def add_segment(self,position):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)
        
            
    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)
        
    
    def down(self):
        if self.head.heading()!=up:
            self.head.setheading(down)

    
    
    def left(self):
        if self.head.heading()!=right:
            self.head.setheading(left)
        
        
    
    def right(self):
        if self.head.heading()!=left:
            self.head.setheading(right)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())