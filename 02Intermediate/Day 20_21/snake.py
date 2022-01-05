import turtle

BLOCK_WIDTH = 20
BLOCK_SPACE = 2
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.start_snake()
        self.head = self.snake_body[0]

    def start_snake(self):
        set_x = 0
        # Create the first snake body - this is the state when the game begins
        for _ in range(3):
            new_block = turtle.Turtle()
            new_block.shape("square")
            new_block.color("white")
            new_block.penup()
            new_block.setx(set_x)
            set_x = new_block.xcor() - BLOCK_SPACE + BLOCK_WIDTH  # Set 'x' for the next snake block
            self.snake_body.append(new_block)  # Add block to the snake body

    def move(self):
        for block_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[block_num - 1].xcor()
            new_y = self.snake_body[block_num - 1].ycor()
            self.snake_body[block_num].goto(new_x, new_y)
        self.head.forward(BLOCK_SPACE + BLOCK_WIDTH)

    def turn_right(self):
        curr_dir = self.head.heading()
        if curr_dir in [RIGHT, LEFT]:  # Moving east or west
            return
        self.head.setheading(RIGHT)  # Set East

    def turn_down(self):
        curr_dir = self.head.heading()
        if curr_dir in [UP, DOWN]:  # Moving north or south
            return
        self.head.setheading(DOWN)  # Set South

    def turn_left(self):
        curr_dir = self.head.heading()
        if curr_dir in [RIGHT, LEFT]:  # Moving east or west
            return
        self.head.setheading(LEFT)  # Set West

    def turn_up(self):
        curr_dir = self.head.heading()
        if curr_dir in [UP, DOWN]:  # Moving north or south
            return
        self.head.setheading(UP)  # Set North

