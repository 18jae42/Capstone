# Import SPGL
import spgl
import os 
import turtle 
import random
import math
import time

# Create Classes
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y,speed):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 1
		self.ticks = 0
		
	def go_forward(self):
		self.fd(10)
		if self.xcor() > 340:
			self.setx(340)
		if self.xcor() < -340:
			self.setx(-340)
		if self.ycor() > 340:
			self.sety(340)
		if self.ycor() < -340:
			self.sety(-340)
	
	def go_backward(self):
		self.fd(-10)
		if self.xcor() > 340:
			self.setx(340)
		if self.xcor() < -340:
			self.setx(-340)
		if self.ycor() > 340:
			self.sety(340)
		if self.ycor() < -340:
			self.sety(-340)
			
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
		self.goto(random.randint(-340, 340), random.randint(-340,340))
	def play_sound(self, filename):
		os.system("afplay {}&".format(filename))

		

class Color(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y) 
        
	def place_random(self):
		self.goto(random.randint(-340, 340), random.randint(-340,340))
	def play_sound(self, filename):
		os.system("afplay {}&".format(filename))  
	 
    
        
class Boxes(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
    def play_sound(self, filename):
    	os.system("afplay {}&".format(filename))
    

    


# Initial Game setup
game = spgl.Game(800, 800, "grey", "Collect the Rainbow",10)
game.set_background("rainbow.gif")
game.lives = 3 
game.timer = 120 
game.play_sound("back.mp3 -v 0.1", 169)


# Create Sprites
player = Player("triangle", "white", random.randint(-350, 350), random.randint(-350,350), 1)
player.shapesize(0.5, 1, 0)
border = Border()
black1 = Black("circle", "black", 1500, 1500)
black2 = Black("circle", "black", 1500, 1500)
black3 = Black("circle", "black", 1500, 1500)
black4 = Black("circle", "black", 1500, 1500)
black5 = Black("circle", "black", 1500, 1500)

color1 = Color("circle", "red", 1500, 1500)
color2 = Color("circle", "orange", 1500, 1500)
color3 = Color("circle", "yellow", 1500, 1500)
color4 = Color("circle", "green", 1500, 1500)
color5 = Color("circle", "blue", 1500, 1500)
color6 = Color("circle", "navy", 1500, 1500)
color7 = Color("circle", "purple", 1500, 1500)


colors = [color1, color2, color3, color4, color5, color6, color7]
game.current_color = 0
remaining_colors = [color1, color2, color3, color4, color5, color6, color7]



blacks = [black1, black2, black3, black4, black5]

border.draw_border()

# Create Functions


def place_circle():
	computer_choice = random.randint(1,4)
	if computer_choice == 1:
		black = random.choice(blacks)
		black.place_random()
	else:
		if len(remaining_colors) > 0:
			next_color = random.choice(remaining_colors)
			remaining_colors.remove(next_color)
			next_color.place_random()		

def place_color():
	next_color = random.choice(remaining_colors1)
	remaining_colors1.remove(next_color)
	next_color.place_random()
	

# Create Labels
lbl_lives = spgl.Label("Lives left: 3", "red", -350, 360)

lbl_lives.set_font_name("Georgia") 
lbl_lives.set_font_size(20) 

lbl_time = spgl.Label("Time Left", "Blue", 170, 360)
lbl_time.update("Time Left: {} seconds".format(game.timer))

lbl_time.set_font_name("Georgia") 
lbl_time.set_font_size(20) 

# Create Buttons

# Set Keyboard Bindings
turtle.listen()
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.go_forward, "Up")
turtle.onkey(player.go_backward, "Down")
turtle.onkey(player.turn_right, "Right")

#blacks = []
#for count in range(100):
	#blacks.append(Black("circle", "black", 1500, 1500))

boxes = []
coordinates = [(-300, -25), (-250, 25), (-250, 25), (-250, 25), (-200, -25),(-150,25),(-100,-25),(-50,25),(0,-25),(0,-25),(0,-25),(0,-25),(50,25),(100,-25),(150,25),(150,25),(150,25),(200,-25),(250,25),(250,25),(300,-25),(300,-25)]
for coordinate in coordinates:
	boxes.append(Boxes("box.gif", "white", coordinate[0], coordinate[1]))



while True:
    # Call the game tick method
	game.tick()
	#start the game time
	for box in boxes:
		if game.is_collision(player, box):
			box.destroy()
			place_circle()
			print("COLLISION")
			box.play_sound("box.wav") 
			
			
	for black in blacks:			
		if game.is_collision(player, black):
			blacks.remove(black)
			black.destroy()
			game.lives -= 1	
			lbl_lives.update("Lives Left: {}".format(game.lives))
			black.play_sound("black.mp3")

	for color in colors:
		if game.is_collision(player, color):
			if color == colors[game.current_color]:
				color.destroy()
				color.play_sound("color.mp3")
				game.current_color += 1
			else:
				game.lives -= 1
				lbl_lives.update("Lives Left: {}".format(game.lives))
				color.destroy()
				color.play_sound("black.mp3")
				#something has gone wrong
		if remaining_colors == []:
			remaining_colors = [color1, color2, color3, color4, color5, color6, color7]

	
	if game.current_color == 7:
		for color in colors:
			color.destroy()
		for black in blacks:
			black.destroy()
		for box in boxes:
			box.destroy()
		player.goto(-1000, -1000)
		border.clear()
		os.system("killall afplay")
		game.play_sound("win.wav")
		lbl_lives.update("")
		lbl_time.update("")
		game.set_background("success.gif")
		game.tick()
		time.sleep(5)
		exit()
				
		
	if game.lives <= 0:
		for color in colors:
			color.destroy()
		for black in blacks:
			black.destroy()
		for box in boxes:
			box.destroy()
		player.goto(-1000, -1000)
		border.clear()
		os.system("killall afplay")
		game.play_sound("lose.wav")
		lbl_lives.update("")
		lbl_time.update("")
		game.set_background("failure.gif")
		game.tick()
		time.sleep(5)
		exit()
		 
	
	if game.timer < 30 and len(remaining_colors) == 0:
		place_circle()	
		
	if game.timer == 0:
		for color in colors:
			color.destroy()
		for black in blacks:
			black.destroy()
		for box in boxes:
			box.destroy ()
		player.goto(-1000, -1000)
		border.clear()
		os.system("killall afplay")
		game.play_sound("lose.wav")
		lbl_lives.update("")
		lbl_time.update("")
		game.set_background("failure.gif")
		game.tick()
		time.sleep(5)
		exit()
		
    
    	
    			
