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
		
	def go_forward(self):
		self.fd(10)
	
	def go_backward(self):
		self.fd(-10)
		
	def turn_left(self):
		self.lt(30)
		
	def turn_right(self):
		self.rt(30)
		
	
	
class Black(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)

	def place_random(self):
		self.goto(random.randint(-400, 400), random.randint(-400,400))
		

class Color(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y) 
        
	def place_random(self):
		self.goto(random.randint(-400, 400), random.randint(-400,400))    
    
        
class Boxes(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        

    


# Initial Game setup
game = spgl.Game(800, 800, "grey", "Collect the Rainbow",0)
game.lives = 3 
game.time = 120 

# Create Sprites
player = Player("triangle", "yellow", 200, -200, 1)
box = Boxes("square", "white", 100, 0)
black = Black("circle", "black", 0, 0)
color1 = Color("circle", "red", 0, 0)
color2 = Color("circle", "orange", 0, 0)
color3 = Color("circle", "yellow", 0, 0)
color4 = Color("circle", "green", 0, 0)
color5 = Color("circle", "blue", 0, 0)
color6 = Color("circle", "navy", 0, 0)
color7 = Color("circle", "purple", 0, 0)

# Create Functions
def isCollision(object1,object2):
	a = object1.xcor() - object2.xcor()
	b = object1.ycor()- object2.ycor()
	d = math.sqrt((a**2)+(b**2))
	if d < 10:
		return True 
	else:
		return False

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

# Create Buttons

# Set Keyboard Bindings
turtle.listen()
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.go_forward, "Up")
turtle.onkey(player.go_backward, "Down")
turtle.onkey(player.turn_right, "Right")


while True:
    # Call the game tick method
    game.tick()
    if game.is_collision(player, box):
    	box.destroy()
    	place_circle()
    	print("COLLISION")
    
    #if game.is_collision(player, color):
    	#if color
    	
    
    	
    			
