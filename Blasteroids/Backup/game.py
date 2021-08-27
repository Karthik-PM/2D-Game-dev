import pygame 
import time
import keystrokes
import collison_dect
import random
import high_score_detector
import score_board
from pygame import mixer
#initalize pygame
pygame.init()
def position():
	screen.blit(sky_img,(pos_x,pos_y))
def meteroids(asteroids_img,meteroids_x,meteroids_y):
	screen.blit(asteroids_img,(meteroids_x,meteroids_y))
#creating a screen
screen = pygame.display.set_mode((800,450));
pygame.display.set_caption("Blasteriods");
icon_img=pygame.image.load("assets\\icon.png");
pygame.display.set_icon(icon_img);
current_score=0;
new_highscore=[];#for storing all the highscores in a list 
file=open("highscore\\highscore.txt","r");
########high score#########################################################
read=file.read();
highscore=int(read);
# highscore=int(highscore);
###########################################################################
score_board_font=pygame.font.SysFont('comicsansms',28);
highscore_board_font=pygame.font.SysFont('comicsansms',28);
mixer.music.load('sounds\\background.wav');
mixer.music.set_volume(0.1);
mixer.music.play(-1);

##################GAME SETUP##############################################
#spaceship_position
sky_img= pygame.image.load("assets\\space_ship.png").convert_alpha();

#astroids
# asteroids_img =pygame.image.load("assets\\asteroids.png").convert_alpha()
asteroids_img =[pygame.image.load("assets\\sprites\\asteroids.png"),pygame.image.load("assets\\sprites\\asteroids1.png"),pygame.image.load("assets\\sprites\\asteroids2.png"),pygame.image.load("assets\\sprites\\asteroids3.png"),pygame.image.load("assets\\sprites\\asteroids4.png")]

meteroids_x=random.randint(0,750);
meteroids_y=-60;


#spaceship_initial position
pos_x=400
pos_y=380

#loading spaceship into the game

#pic for backround image
backround_image=pygame.image.load("assets\\space_background.png").convert_alpha();

#setting up bullets
bullet_img=pygame.image.load("assets\\laser.png").convert_alpha();
bul_x=pos_x;
bul_y=pos_y;

#gameover symbol:
gameover=pygame.image.load("assets\\game-over.png").convert_alpha();
diff=0;
bullet_diff=0;
###############################################################################

bul_x=[]
bul_x_pos=0;#for taking in the x co-ordinate for the bullet
collison=False;
###########################RUNNING GAME########################################
running = True;
index=0;
while running:
	#game backround color
	screen.blit(backround_image,(0,0));


	#meteroids posn
	for i in pygame.event.get():
		if(i.type==pygame.QUIT):
			running=False;
		diff=keystrokes.keyboard_controls(diff,i);
		bullet_diff=keystrokes.bullet_shoot(i,bullet_diff)
		shoot_pos=0
	meteroids(meteroids_x,meteroids_y)
	if(bullet_diff==-15):
		bul_x=bul_x+[pos_x]
		bullet_sound=mixer.Sound('sounds\\laser.wav')
		bullet_sound.set_volume(0.01);
		bullet_sound.play();

		bul_x= list(dict.fromkeys(bul_x))
		bul_x_pos=bul_x[len(bul_x)-1];
		shoot_pos=bul_x[0];
		if(bul_y <-3):
			bul_y=380;
			bullet_diff=0
			bul_x=[]

		else:
			screen.blit(bullet_img,(shoot_pos+27,bul_y));
	####################COLLISION####################################
		collison=collison_dect.collision_detect(meteroids_x,meteroids_y,bul_x_pos,bul_y);
	# new_highscore=new_highscore+[highscore];
	if current_score==highscore+1:
		highscore_sound=mixer.Sound("sounds\\highsore.wav");
		time.sleep(0.4)
		highscore_sound.play();
		current_score=current_score+1

	if(current_score>=highscore):
		high_score_detector.highscore(current_score);
	
	########OBSTACLE MOVEMENT#######################################	
	met_y_diff=0.25;
	meteroids_y+=met_y_diff;
	# met_x_diff=5;
	# meteroids_x+=met_x_diff
	pos_x +=diff;
	bul_y +=bullet_diff;
	#################################################################
	if (collison==True):
		explosion_sound=mixer.Sound('sounds\\explosion.wav');                     
		explosion_sound.play();
		print(collison)
		
		print("sound")	
		meteroids_x=random.randint(0,400);
		meteroids_y=-60;
		current_score+=1;
	
	if(meteroids_x>=pos_x and (meteroids_y>=pos_y-40)):
		screen.blit(gameover,(250,100));
		gameover_sound=mixer.Sound('sounds\\gameover.wav');
		gameover_sound.play();
		gameover_sound.set_volume(0.01)
		meteroids_y=pos_y-40;
		meteroids_x=pos_x;
		met_y_diff=0;
		met_x_diff=0;
	if(meteroids_y>=380):
		screen.blit(gameover,(250,100));
		gameover_sound=mixer.Sound('sounds\\gameover.wav');
		gameover_sound.set_volume(0.01);
		gameover_sound.play();
		meteroids_y=380;
	if(pos_x>=730):
		pos_x=730;
	if(pos_x<=0):
		pos_x=0;
	


	#rocket_load:
	position()
	#object_load:
	# meteroids(meteroids_x,meteroids_y)
	#score board load:
	score_board.score_board(highscore,current_score,highscore_board_font,score_board_font,screen);
	
	pygame.display.update() 
