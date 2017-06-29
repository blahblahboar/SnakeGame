
import pygame
import random
from copy import deepcopy
import math
from pygame.locals import *
import time


pygame.init()
pygame.mixer.init()
global width, height
redsquare = pygame.image.load("redsquare.png")
snake = pygame.image.load("snake.png")
width, height = 1000,1000
pygame.display.init()
screen = pygame.display.set_mode((width,height))
white = (255,255,255)
screen.fill(white)
pygame.display.flip()



def pause_game():
	paused = True
	font = pygame.font.Font(None, 24)
	while paused:
		text = font.render("Game Paused", True, (0,0,255))
		screen.blit(text, (100,250))
		for event in pygame.event.get():
				 
				 if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
					 paused = False
				 continue

def game_over():
	game_over= True
	font = pygame.font.Font(None, 24)
	while game_over:
		text = font.render("Game Over: Press any Key to Restart", True, (0,0,255))
		screen.blit(text, (340,450))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				game_over = False
				
while 1:
	game_over()
	game_running = True
	directions_vector = [False, False, False, False]
	snake_length = 1
	head_position = [random.randint(0,19), random.randint(0,19)]
	snakes = []
	extra = True
	snakes.append(head_position)
	pos = [random.randint(0,19), random.randint(0,19)]
	snakes_copy = []
	counter = 0
	last_direction = None
	key_pressed = 0
	font = pygame.font.Font(None, 24)
	lastsave = time.time()
	while game_running:
		counter  += 1
		screen.fill(white)
		text1 = font.render("Length:"+str(snake_length), True, (255,0,0))
		screen.blit(text1, (0, 0))
		for i in range(len(snakes)):
			screen.blit(snake, (snakes[i][0]*50, snakes[i][1]*50))

		if extra == True:
			screen.blit(redsquare, (pos[0]*50, pos[1]*50))
			
		snakes_past_position = deepcopy(snakes)
		
		if time.time()- lastsave > (0.15-0.003*snake_length):
			lastsave= time.time()
			if key_pressed == 1:
				directions_vector = [False, False, False, False]
				directions_vector[last_direction] = True
				if directions_vector[0] == True:
					
					snakes[0][1] -= 1
				elif directions_vector[1] == True:
					
					snakes[0][0] -= 1
				elif directions_vector[2] == True:
					
					snakes[0][1] += 1
				elif directions_vector[3] == True:
					
					snakes[0][0] += 1
			if snakes[0] in snakes[1:]:
				game_running = False
				
				
				
			snakes = [snakes[0]] + snakes_past_position[:-1]
				
		if snakes[0][1] < 0 or snakes[0][0] < 0:
			game_running = False
		if snakes[0][0] >19 or snakes[0][1] >19:
			game_running = False
		
		
		
		
		
		
	##	snakerect = pygame.Rect(snake.get_rect())
	##	snakerect.top = snakes[0][1]
	##	snakerect.left = snakes[0][0]
	##	redrect = pygame.Rect(redsquare.get_rect())
	##	redrect.top = pos[1]
	##	redrect.left = pos[0]
		

		if snakes[0] == pos:
			snake_length += 1
			copy = []
			in_snake = False
			while in_snake == False:    
				pos = [random.randint(0,19), random.randint(0,19)]
				if pos not in snakes:
					in_snake = True
			if directions_vector[0] == True:
				copy.append([snakes[0][0], snakes[0][1] - 1])
			elif directions_vector[1] == True:
				copy.append([snakes[0][0]-1, snakes[0][1]])
			elif directions_vector[2] == True:
				copy.append([snakes[0][0], snakes[0][1]+1])
			elif directions_vector[3] == True:
				copy.append([snakes[0][0]+1, snakes[0][1]])
			snakes = copy + snakes
			
			
		
		for event in pygame.event.get():
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pause_game()
					key_pressed = 1
					last_direction = 0
				elif event.key == pygame.K_w:
					key_pressed = 1
					last_direction = 0	
				elif event.key == pygame.K_a:
					key_pressed = 1
					last_direction = 1
				elif event.key == pygame.K_s:
					key_pressed = 1
					last_direction = 2
				elif event.key == pygame.K_d:
					key_pressed = 1
					last_direction = 3
					
	##        if event.type == pygame.KEYUP:
	##            
	##            if event.key == pygame.K_w:
	##                last_direction = 0
	##            elif event.key == pygame.K_a:
	##                directions_vector[1] = False
	##            elif event.key == pygame.K_s:
	##                directions_vector[2] = False
	##            elif event.key == pygame.K_d:
	##                directions_vector[3] = False
		pygame.display.flip()
			
	

	
