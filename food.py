import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280,280),random.randint(-280,280))




