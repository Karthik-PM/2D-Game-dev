import pygame 
import keystrokes
import collison_dect
import random
import high_score_detector
from pygame import mixer
#initalize pygame
pygame.init()
#creating a screen
screen = pygame.display.set_mode((800,450));
pygame.display.set_caption("Blasteriods");
icon_img=pygame.image.load("assets\\icon.png");
pygame.display.set_icon(icon_img);
################score board################################################
current_score=0;
########high score#########################################################
file=open("highscore\\highscore.txt","r");
read=file.read();
highscore=int(read);
# highscore=int(highscore);
###########################################################################
score_board_font=pygame.font.SysFont('comicsansms',28);
highscore_board_font=pygame.font.SysFont('comicsansms',28);
def score_board():
	highscore_board=highscore_board_font.render("HIGH SCORE:"+str(highscore),True,(255,0,0))
	score_board=score_board_font.render("SCORE:"+str(current_score),True,(255,0,0));
	screen.blit(highscore_board,(570,50));
	screen.blit(score_board,(630,0));


mixer.music.load('sounds\\background.wav');
mixer.music.set_volume(0.1);
mixer.music.play(-1);

##################GAME SETUP##############################################
#spaceship_position
sky_img= pygame.image.load("assets\\space_ship.png").convert_alpha()

#astroids
asteroids_img =pygame.image.load("assets\\asteroids.png").convert_alpha()
meteroids_x=100;
meteroids_y=-60;

def meteroids(meteroids_x,meteroids_y):
	screen.blit(asteroids_img,(meteroids_x,meteroids_y))

#spaceship_initial position
pos_x=400
pos_y=380

#loading spaceship into the game
def position():
	screen.blit(sky_img,(pos_x,pos_y))
#pic for backround image
backround_image=pygame.image.load("assets\\space_background.png").convert_alpha()

#setting up bullets
bullet_img=pygame.image.load("assets\\laser.png").convert_alpha()
bul_x=pos_x;
bul_y=pos_y;

#gameover symbol:
gameover=pygame.image.load("assets\\game-over.png").convert_alpha()
diff=0;
bullet_diff=0;
###############################################################################

bul_x=[]
bul_x_pos=0;#for taking in the x co-ordinate for the bullet
collison=False;
###########################RUNNING GAME########################################
running = True;

while running:
	#game backround color
	screen.blit(backround_image,(0,0));


	#meteroids posn
	meteroids(meteroids_x,meteroids_y)
	for i in pygame.event.get():
		if(i.type==pygame.QUIT):
			running=False;
		diff=keystrokes.keyboard_controls(diff,i);
		bullet_diff=keystrokes.bullet_shoot(i,bullet_diff)
		shoot_pos=0
	if(bullet_diff==-15):
		bul_x=bul_x+[pos_x]
		bullet_sound=mixer.Sound('sounds\\laser.wav')
		bullet_sound.set_volume(0.01);

		bullet_sound.play();
		bul_x= list(dict.fromkeys(bul_x))
		bul_x_pos=bul_x[len(bul_x)-1];
		shoot_pos=bul_x[0];
		if(bul_y <0):
			bul_y=380;
			bullet_diff=0
			bul_x=[]

		else:
			screen.blit(bullet_img,(shoot_pos+27,bul_y));
		collison=collison_dect.collision_detect(meteroids_x,meteroids_y,bul_x_pos,bul_y)
	####################COLLISION####################################
	if (collison==True):
		meteroids_x=random.randint(0,400);
		meteroids_y=-60;
		current_score+=1;
		if(current_score>=highscore):
			highscore_sound=mixer.Sound("sounds\\highsore.wav");
			highscore_sound.play();
			high_score_detector.highscore(current_score);
	########OBSTACLE MOVEMENT#######################################	
	met_y_diff=0.25;
	meteroids_y+=met_y_diff;
	
			
	# met_x_diff=5;
	# meteroids_x+=met_x_diff
	pos_x +=diff;
	bul_y +=bullet_diff;
	#################################################################
	
	if(meteroids_x>=pos_x and (meteroids_y>=pos_y-40)):
		screen.blit(gameover,(250,100));
		gameover_sound=mixer.Sound('sounds\\gameover.wav');
		gameover_sound.play();
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
	meteroids(meteroids_x,meteroids_y)
	#score board load:
	score_board()
	
	pygame.display.update() 
