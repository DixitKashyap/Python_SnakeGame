from turtle import Turtle

# Staring postion of Snake Object
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
# Snake every iteration moving distance
MOVE_DISTANCE  = 20

# Snake Direction
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0 

class Snake:

    def __init__(self) -> None:
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0]
        
# Creating the Snake Object
    def create_snake(self):
        for position  in STARTING_POSITION:
         self.add_segment(position=position)  


# Moving the Snake Object
    def move(self) :
        for seg in range(len(self.segments)-1,0,-1):
            print(seg,seg-1)
            newx =self.segments[seg-1].xcor()
            newy =self.segments[seg-1].ycor()
            self.segments[seg].goto(newx,newy)

        self.segments[0].forward(MOVE_DISTANCE)


    def add_segment(self,position):
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())        

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
    def up(self):
        if(self.segments[0].heading() != DOWN):
            self.segments[0].setheading(UP)    


    def down(self):
        if(self.segments[0].heading()!=UP):
            self.segments[0].setheading(DOWN)

    def left(self):
        if(self.segments[0].heading()!=RIGHT):
            self.segments[0].setheading(LEFT)

    def right(self):
        if(self.segments[0].heading()!=LEFT):
            self.segments[0].setheading(RIGHT)