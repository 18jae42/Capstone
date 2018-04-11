# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import os 
import turtle 
import random
import math

# Create Classes
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y,speed):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 1
		self.ticks = 0
		
	def go_forward(self):
		self.fd(10)
	
	def go_backward(self):
		self.fd(-10)
		
	def turn_left(self):
		self.lt(30)
		
	def turn_right(self):
		self.rt(30)
		
	def tick(self):
		self.ticks += 1
		if self.ticks == 30:
			game.timer -= 1
			lbl_time.update("Time Left: {} seconds".format(game.timer))
			self.ticks = 0
			
class Border(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup() 
		self.hideturtle()
		self.speed(0)
		self.color("black")
		self.pensize(5)
	
	def draw_border(self):
		self.penup()
		self.goto(-350,-350)
		self.pendown()
		self.goto(-350,350)
		self.goto(350,350)
		self.goto(350,-350)
		self.goto(-350,-350)
		
class Black(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)

	def place_random(self):
		self.goto(random.randint(-350, 350), random.randint(-350,350))
		

class Color(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y) 
        
	def place_random(self):
		self.goto(random.randint(-350, 350), random.randint(-350,350))    
    
        
class Boxes(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        

    


# Initial Game setup
game = spgl.Game(800, 800, "grey", "Collect the Rainbow",0)
game.lives = 3 
game.timer = 120 

# Create Sprites
player = Player("triangle", "yellow", 200, -200, 1)
border = Border()
box = Boxes("square", "white", 100, 0)
black = Black("circle", "black", 1500, 1500)
color1 = Color("circle", "red", 1500, 1500)
color2 = Color("circle", "orange", 1500, 1500)
color3 = Color("circle", "yellow", 1500, 1500)
color4 = Color("circle", "green", 1500, 1500)
color5 = Color("circle", "blue", 1500, 1500)
color6 = Color("circle", "navy", 1500, 1500)
color7 = Color("circle", "purple", 1500, 1500)


border.draw_border()

# Create Functions


def place_circle():
	computer_choice = random.randint(1,2)
	if computer_choice == 1:
		black.place_random()
	elif computer_choice == 2:
		color_choice = random.randint(1,7)
		if color_choice == 1:
			color1.place_random()
		elif color_choice == 2:
			color2.place_random()
		elif color_choice == 3:
			color3.place_random()
		elif color_choice == 4:
			color4.place_random()
		elif color_choice == 5:
			color5.place_random()
		elif color_choice == 6:
			color6.place_random()
		elif color_choice == 7:
			color7.place_random()

# Create Labels
lbl_lives = spgl.Label("Lives left: 3", "red", -350, 360)

lbl_lives.font_name = "Georgia" # Default is Arial
lbl_lives.font_size = 20 # Default is 12

lbl_time = spgl.Label("Time Left", "Blue", 230, 360)
lbl_time.update("Time Left: {} seconds".format(game.timer))

# Create Buttons

# Set Keyboard Bindings
turtle.listen()
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.go_forward, "Up")
turtle.onkey(player.go_backward, "Down")
turtle.onkey(player.turn_right, "Right")

rainbow = 0 

while True:
    # Call the game tick method
	game.tick()
	#start the game time
	if game.is_collision(player, box):
		box.destroy()
		place_circle()
		print("COLLISION")

	if game.is_collision(player, black):
		black.destroy()
		game.lives -= 1	
		lbl_lives.update("Lifes Left: {}".format(game.lives))
    	
	if game.is_collision(player, color1):
		rainbow += 1
		color1.destroy()
	
	if rainbow == 7:
		print("You win!")
	
	if game.lives <= 0:
		quit()
		
	if game.timer == 0:
		quit()
    	
    
    	
    			
