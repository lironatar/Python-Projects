from tkinter import *
import random
#Settings

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 150
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR ="#FF0000"
BACKGROUND_COLOR = "#000000"



class Snake:
    def __init__(self): 
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares=[]
        
        headimg= PhotoImage(file="head.png")
        image = canvas.create_image(50, 50, anchor=NE, image=headimg)
        #self.squares.append(image)
        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])
        

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y,x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)
            print(f"x:{x}, y{y}, ")
            
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) *SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) *SPACE_SIZE
    
        self.coordinates = [x,y]
        canvas.create_oval(x,y, x+ SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake,food):
    x,y = snake.coordinates[0]        
    print(f"x = {x} | y= {y}")
    if direction == "up":
        y-=SPACE_SIZE
    elif direction == "down":
        y+=SPACE_SIZE
    elif direction =="left":
        x-=SPACE_SIZE
    elif direction =="right":
        x+=SPACE_SIZE
    
    snake.coordinates.insert(0, (x,y))
    square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)
    
    if x== food.coordinates[0] and y== food.coordinates[1]:
        global score
        score +=1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    window.after(SPEED, next_turn, snake, food)
    if check_collision(snake):
        game_over()
    
def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction
def check_collision(snake):
    x,y= snake.coordinates[0]

    if y == GAME_HEIGHT or y< 0:
        return True
    elif x==GAME_WIDTH or x< 0:
        return True
    
    flag = 0
    for body_part in snake.coordinates[1:]:       
        print("body part:",body_part)
        if body_part[0] == x and y==body_part[1]:
            print("collide")
            print(f"bodypart0{body_part[0]} equal to x{x}, and bodypart1 {body_part[1]} equal to y{y}")
            return True
    return False
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas', 70), text="Game Over", fill="red",tag="gameover" )
    window.destroy()
window = Tk()
window.title("Snake Game")
window.resizable(False, False)
score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas',40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2)-300)
y = int((screen_height/2) - (window_height/2)-50)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('a', lambda event: game_over() )

snake= Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
