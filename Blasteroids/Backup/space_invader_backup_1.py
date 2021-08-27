import pygame
#initalize pygame
pygame.init()
#creating a screen
screen = pygame.display.set_mode((800,450))
#name and icon
pygame.display.set_caption("Space Invaders")#name
icon_image=pygame.image.load("space.png")
pygame.display.set_icon(icon_image)
#game loop
running = True;
#spaceship_position
sky_img= pygame.image.load("bo (1).png")
#homework
homework_img =pygame.image.load("document.png")
hw_x=0;
hw_y=0;
def hw():
	for i in range(0,10):
		
		screen.blit(homework_img,(hw_x+100*i,hw_y))
#spaceship_initial position
pos_x=400
pos_y=380
#loading spaceship into the game
def position():
	screen.blit(sky_img,(pos_x,pos_y))
#pic for backround image
backround_image=pygame.image.load("Screenshot 2021-06-26 203645.png")
#setting up bullets
#bullet_img=pygame.image.load("")
#####################################
diff=0
while running:

	#game backround color
	screen.blit(backround_image,(0,0))


	#hw posn
	hw()
	for i in pygame.event.get():
		if(i.type==pygame.QUIT):
			running=False
		if(i.type==pygame.KEYUP):
			diff=0
			print("spaceship stops")
		#keyboard controls
		if(i.type==pygame.KEYDOWN):
			if(i.key==pygame.K_LEFT):
				print("spaceship moves left",pos_x)
				diff=-1
			if(i.key==pygame.K_RIGHT):
				print("spaceship moves right",pos_x)
				diff=1
			if(i.key==pygame.K_UP):
				print("Bullet is shot");	
		if(i.type==pygame.KEYUP):
			diff=0
			print("spaceship stops")
			
	pos_x +=diff
	if(pos_x>=730):
		pos_x=730;
	if(pos_x<=0):
		pos_x=0;
	


	#boormey_load
	position()

	pygame.display.update()
