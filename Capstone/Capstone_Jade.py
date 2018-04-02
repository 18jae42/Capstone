# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import os 
import turtle 
import random

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

class Color(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)     
        
class Boxes(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
    
        
# Create Functions

# Initial Game setup
game = spgl.Game(800, 800, "black", "Collect the Rainbow",0)
game.lives = 3 
game.time = 120 

# Create Sprites
player = Player("triangle", "yellow", 200, -200, 1)



	
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
    
