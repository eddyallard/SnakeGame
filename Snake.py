import pygame
import random
#COLORS
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255,255,255)

class Board:
    #where we store all the square of the board
    board=[]
    #creates a table with x_length number of squares on x axis and y_length number of squares on y axis
    def __init__(self, x_length, y_length, size):
        self.size = size
        for x_loc in range(x_length):
            for y_loc in range(y_length):
                self.board.append((x_loc, y_loc))
                self.draw(black, x_loc, y_loc)
    def get(self):
        return self.board
    def draw(self, color, x, y):
        x_loc = x*self.size
        y_loc = (y*self.size)+header
        pygame.draw.rect(display, color, (x_loc, y_loc, self.size, self.size))

class Player:

    snake = []
    color = green
    def __init__(self, board):
        self.currentDirection=(1,0)
        self.board = board
        self.snake.append((1,boardy/2-1))
        self.snake.append((2,boardy/2-1))
        self.snake.append((3,boardy/2-1))

    def draw(self, grew):
        if grew is False:
            self.removeFirst()
        for square in self.snake:
            self.board.draw(self.color, square[0], square[1])
    
    def move(self):
        if self.currentDirection == (1,0):
            self.snake.append((self.snake[-1][0]+1,self.snake[-1][1])) #right
        elif self.currentDirection == (-1, 0):
            self.snake.append((self.snake[-1][0]-1,self.snake[-1][1])) #left
        elif self.currentDirection ==(0, 1):
            self.snake.append((self.snake[-1][0],self.snake[-1][1]+1)) #down
        elif self.currentDirection ==(0, -1):
            self.snake.append((self.snake[-1][0],self.snake[-1][1]-1)) #up
    
    def removeFirst(self):
        self.board.draw(black, self.snake[0][0],self.snake[0][1])
        self.snake.pop(0)
    
    def get(self):
        return(self.snake[-1][0], self.snake[-1][1])

    def touches(self):
        for square in self.snake[:-1]:
            if(self.get() == square):
                return True
        return False

class Point:
    color = red
    def __init__(self, board):
        self.x = boardx/2 -1
        self.y = boardy/2 -1
        self.board = board
        self.draw()

    def draw(self):
        self.board.draw(self.color, self.x, self.y) 

    def new(self):
        newX = random.randrange(boardx-1)
        newY = random.randrange(boardy-1)
        while(snake.snake.__contains__((newX, newY))):
            newX = random.randrange(boardx-1)
            newY = random.randrange(boardy-1)
        self.x = newX
        self.y = newY
        self.draw()
    
    def get(self):
        return(self.x,self.y)

def directionHandler(key, snake):
    if key[pygame.K_w]:
        if snake.currentDirection != (0,1):
            snake.currentDirection = (0,-1)
    elif key[pygame.K_s]:
        if snake.currentDirection != (0,-1):
            snake.currentDirection = (0,1)
    elif key[pygame.K_a]:
        if snake.currentDirection != (1,0):
            snake.currentDirection = (-1,0)
    elif key[pygame.K_d]:
        if snake.currentDirection != (-1,0):
            snake.currentDirection = (1,0)
header = 30
boardx = 50
boardy = 30
boardSize = 20
(width, height) = (boardx*boardSize, boardy*boardSize)
display = pygame.display.set_mode((width, height+header))
display.fill(white)
pygame.display.flip()

#Score counter


panel = Board(boardx, boardy, boardSize)
snake = Player(panel)
treat = Point(panel)
clock = pygame.time.Clock()
#Main game loop
running = True
grew = False
while running:
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            directionHandler(pygame.key.get_pressed(), snake)
    if snake.get()[0] < 0 or snake.get()[1] < 0 or snake.get()[0] >= boardx or snake.get()[1] >= boardy or snake.touches():
        break
    snake.move()
    if snake.get() == treat.get():
        grew = True
        treat.new()
    else:
        grew = False
    snake.draw(grew)
    pygame.display.update()
