import time
import  turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self,position):
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def on_key_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def on_key_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def on_key_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def on_key_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
