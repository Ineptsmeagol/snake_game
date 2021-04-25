from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
POSITIONS = [(0, 0), (-20, 0), (-30, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create a 3 segment snake to start the game"""
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        my_snake = Turtle("square")
        my_snake.color('white')
        my_snake.penup()
        my_snake.goto(position)
        self.segments.append(my_snake)

    def extend(self):
        """Extend the snake by one segment"""
        self.add_segment(self.segments[-1].position())

    def snake_forward(self):
        """Move then snake forward"""
        pass
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        self.segments[0].forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        """Move snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Move snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Move snake to the left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Move the snake to the right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
