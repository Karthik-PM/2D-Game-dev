import pygame 
import time
import keystrokes
import collison_dect
import random
import high_score_detector
import score_board
import level_display
import main_menu
from pygame import mixer
from pygame.locals import *
#initalize pygame
pygame.init()
def position(sky_img,pos_x,pos_y):
	screen.blit(sky_img,(pos_x,pos_y))
def meteroids(asteroids_img,meteroids_x,meteroids_y):
	screen.blit(asteroids_img,(meteroids_x,meteroids_y))
def bomb(bomb,bomb_x,bomb_y):
	screen.blit(bomb,(bomb_x,bomb_y))
#creating a screen
screen = pygame.display.set_mode((800,450));

#######################################################################################
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
mixer.music.set_volume(0.025);
mixer.music.play(-1);

##################GAME SETUP##############################################
#spaceship_position
sky_img=[
			pygame.image.load("assets\\space_ship.png"),
			pygame.image.load("assets\\space_ship_level_2.png"),
			pygame.image.load("assets\\spaceship_level_3.png")
		]

#astroids
# asteroids_img =pygame.image.load("assets\\asteroids.png").convert_alpha()

# level 1- Objects
asteroids_img1 =[
					pygame.image.load("assets\\sprites\\level-1\\asteroids.png"),
					pygame.image.load("assets\\sprites\\level-1\\asteroids1.png"),
					pygame.image.load("assets\\sprites\\level-1\\asteroids2.png"),
					pygame.image.load("assets\\sprites\\level-1\\asteroids3.png"),
					pygame.image.load("assets\\sprites\\level-1\\asteroids4.png")
				]

asteroids_img2 =[
					pygame.image.load("assets\\sprites\\level-1\\asteroids.png"),
					pygame.image.load("assets\\sprites\\level-1\\asteroids1.png"),
					pygame.image.load("assets\\sprites\\level-1\\asteroids2.png"),
					pygame.image.load("assets\\sprites\\level-1\\asteroids3.png"),
					pygame.image.load("assets\\sprites\\level-1\\asteroids4.png")
				]

asteroids_img3 =[
					pygame.image.load("assets\\sprites\\level-1\\asteroids.png"),
					pygame.image.load("assets\\sprites\\level-1\\asteroids1.png"),
					pygame.image.load("assets\\sprites\\level-1\\asteroids2.png"),
					pygame.image.load("assets\\sprites\\level-1\\asteroids3.png"),
					pygame.image.load("assets\\sprites\\level-1\\asteroids4.png")
				]
# level 2 objects

asteroids_img21 =[
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_2.png"),
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_21.png"),
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_22.png"),
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_23.png"),
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_24.png")
				]

asteroids_img22 =[
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_2.png"),
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_21.png"),
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_22.png"),
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_23.png"),
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_24.png")
				]



asteroids_img23 =[
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_2.png"),
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_21.png"),
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_22.png"),
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_23.png"),
					pygame.image.load("assets\\sprites\\level-2\\asteroid_level_24.png")
				]

# level3 objects
asteroids_img3 =[
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_3.png"),
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_31.png"),
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_32.png"),
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_33.png"),
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_34.png")
				]

asteroids_img31 =[
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_3.png"),
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_31.png"),
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_32.png"),
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_33.png"),
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_34.png")
				]

asteroids_img32 =[
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_3.png"),
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_31.png"),
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_32.png"),
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_33.png"),
					pygame.image.load("assets\\sprites\\level-3\\asteroid_level_34.png")
				]

bomb=pygame.image.load("assets\\nuclear-bomb.png")
integer=[random.randint(0,5),random.randint(0,10),random.randint(0,10)]
bomb_x=[random.randint(0,75)*integer[0],random.randint(0,75)*integer[1],random.randint(0,75)*integer[2]]
bomb_y=[-70,-2500,-3000]

meteroids_x=[
				random.randint(0,750),
				random.randint(0,750),
				random.randint(0,750),
				random.randint(0,750),
				random.randint(0,750),
				random.randint(0,750),
				random.randint(0,750),
				random.randint(0,750),
				random.randint(0,750),
				random.randint(0,750),
			]

meteroids_y=[-60,-200,-300,-1000,-1600,-1700,-2500,-1700,3600];


#spaceship_initial position
pos_x=400
pos_y=380

#loading spaceship into the game

#pic for backround image
backround_image=pygame.image.load("assets\\space_background.png").convert_alpha();
backround_image_level_2=pygame.image.load("assets\\NPtvhs.png").convert_alpha();
backround_image_level_3=pygame.image.load("assets\\space_background_level3.png").convert_alpha();


#setting up bullets
bullet_img=pygame.image.load("assets\\laser.png").convert_alpha();
bul_x=pos_x;
bul_y=pos_y;

#gameover symbol:
gameover=pygame.image.load("assets\\game-over.png").convert_alpha();
blast_img=pygame.image.load("assets\\explosion.png")
diff=0;
bullet_diff=0;
###############################################################################
bul_x=[]
bul_x_pos=0;#for taking in the x co-ordinate for the bullet
collison=False;
###########################RUNNING GAME########################################
index=[0]*10;
iteration=[0]*10
level_up_sound=mixer.Sound('sounds\\level_up.wav')
font_1=pygame.font.SysFont('comicsansms',28);
life=[
		pygame.image.load("assets\\heart.png"),
		pygame.image.load("assets\\heart.png"),
		pygame.image.load("assets\\heart.png")
	]
screen.blit(life[0],(10,10))
n=len(life)
running = True;
unning=True
win=False
win_score=50
while unning:
			menu=pygame.image.load("assets\\menu\\menu.png")
			start=score_board_font.render("START",True,(255,0,0))
			quit=score_board_font.render("QUIT",True,(255,0,0))
			screen.blit(menu,(0,0));
			mx,my=pygame.mouse.get_pos()
			for i in pygame.event.get():

				if(i.type==pygame.QUIT):
					unning = False
					running=False
			
				#print(mx,my)
				if(i.type==MOUSEBUTTONDOWN):
					if(mx<=426 and mx>=351 and my<=179 and my>=155):
						unning=False
					elif(mx<=426 and mx>=351 and my<=229 and my>=208):
						unning = False
						running=False
			if(mx<=440 and mx>=351 and my<=179 and my>=155):
				start=score_board_font.render("START",True,(0,255,0))
			elif(mx<=426 and mx>=351 and my<=229 and my>=208):
				quit=score_board_font.render("QUIT",True,(0,255,0))
			screen.blit(start,(350,147))
			screen.blit(quit,(350,200))
			pygame.display.update()

		
while running:
	#game backround color
	collison=[	
			collison_dect.collision_detect(meteroids_x[0],meteroids_y[0],bul_x_pos,bul_y),
			collison_dect.collision_detect(meteroids_x[1],meteroids_y[1],bul_x_pos,bul_y),
			collison_dect.collision_detect(meteroids_x[2],meteroids_y[2],bul_x_pos,bul_y),
			collison_dect.collision_detect(meteroids_x[3],meteroids_y[3],bul_x_pos,bul_y),
			collison_dect.collision_detect(meteroids_x[4],meteroids_y[4],bul_x_pos,bul_y),
			collison_dect.collision_detect(meteroids_x[5],meteroids_y[5],bul_x_pos,bul_y),
			collison_dect.collision_detect(meteroids_x[6],meteroids_y[6],bul_x_pos,bul_y),
			collison_dect.collision_detect(meteroids_x[7],meteroids_y[7],bul_x_pos,bul_y),
			collison_dect.collision_detect(meteroids_x[8],meteroids_y[8],bul_x_pos,bul_y),
		]
	bomb_collision=[
						collison_dect.collision_detect(bomb_x[0],bomb_y[0],bul_x_pos,bul_y),
						collison_dect.collision_detect(bomb_x[1],bomb_y[1],bul_x_pos,bul_y),
						collison_dect.collision_detect(bomb_x[2],bomb_y[2],bul_x_pos,bul_y)
						
					]
	if (collison[1]==True):	
		explosion_sound=mixer.Sound('sounds\\explosion.wav');                     
		#explosion_sound.play();
		#print(collison)
		#print("sound")	
		meteroids_x[1]=random.randint(0,400);
		meteroids_y[1]=-200;
		current_score+=1;

	if (collison[2]==True):	
		explosion_sound=mixer.Sound('sounds\\explosion.wav');                     
		#explosion_sound.play();
		#print(collison)
		#print("sound")	
		meteroids_x[2]=random.randint(0,400);
		meteroids_y[2]=-300;
		current_score+=1;

	if (collison[3]==True):	
		explosion_sound=mixer.Sound('sounds\\explosion.wav');                     
		#explosion_sound.play();
		#print(collison)
		#print("sound")	
		meteroids_x[3]=random.randint(0,400);
		meteroids_y[3]=-1000;
		current_score+=1;

	if (collison[4]==True):	
		explosion_sound=mixer.Sound('sounds\\explosion.wav');                     
		#explosion_sound.play();
		#print(collison)
		#print("sound")	
		meteroids_x[4]=random.randint(0,400);
		meteroids_y[4]=-1600;
		current_score+=1;

	if (collison[5]==True):	
		explosion_sound=mixer.Sound('sounds\\explosion.wav');                     
		#explosion_sound.play();
		#print(collison)
		#print("sound")	
		meteroids_x[5]=random.randint(0,400);
		meteroids_y[5]=-1700;
		current_score+=1;
	if (collison[6]==True):	
		explosion_sound=mixer.Sound('sounds\\explosion.wav');                     
		#explosion_sound.play();
		#print(collison)
		#print("sound")	
		meteroids_x[6]=random.randint(0,400);
		meteroids_y[6]=-1700;
		current_score+=1;

	if (collison[7]==True):	
		explosion_sound=mixer.Sound('sounds\\explosion.wav');                     
		#explosion_sound.play();
		#print(collison)
		#print("sound")	
		meteroids_x[7]=random.randint(0,400);
		meteroids_y[7]=-1700;
		current_score+=1;

	if (collison[8]==True):	
		explosion_sound=mixer.Sound('sounds\\explosion.wav');                     
		#explosion_sound.play();
		#print(collison)
		#print("sound")	
		meteroids_x[8]=random.randint(0,400);
		meteroids_y[8]=-1700;
		current_score+=1;
	flag1=False
	if (bomb_collision[0]==True):	
		explosion_sound=mixer.Sound('sounds\\explosion.wav');
		time.sleep(0.4)                       
		explosion_sound.play();
		#print(collison)
		#print("sound")	
		bomb_x[0]=random.randint(0,400);
		bomb_y[0]=-250;
		n=n-1
		

	if (bomb_collision[1]==True):	
		explosion_sound=mixer.Sound('sounds\\explosion.wav');
		time.sleep(0.4)                       
		explosion_sound.play();
		#print(collison)
		#print("sound")	
		bomb_x[1]=random.randint(0,400);
		bomb_y[1]=-300;
		n=n-1
		

	if (bomb_collision[2]==True):	
		explosion_sound=mixer.Sound('sounds\\explosion.wav');
		time.sleep(0.4)                     
		explosion_sound.play();
		#print(collison)
		#print("sound")	
		bomb_x[2]=random.randint(0,400);
		bomb_y[2]=-170;
		n=n-1

		

	if(current_score>10 and current_score<=20):
		screen.blit(backround_image_level_2,(0,0));
		position(sky_img[1],pos_x,pos_y)
		

		if(current_score==11):
			time.sleep(0.4)
			level_up_sound.play()
			current_score+=1
		meteroids(asteroids_img1[index[0]],meteroids_x[0],meteroids_y[0])
		meteroids(asteroids_img2[index[1]],meteroids_x[1],meteroids_y[1])
		meteroids(asteroids_img3[index[2]],meteroids_x[2],meteroids_y[2])
		meteroids(asteroids_img21[index[3]],meteroids_x[3],meteroids_y[3])
		meteroids(asteroids_img22[index[4]],meteroids_x[4],meteroids_y[4])
		meteroids(asteroids_img23[index[5]],meteroids_x[5],meteroids_y[5])
		screen.blit(bomb,(bomb_x[0],bomb_y[0]))
		screen.blit(bomb,(bomb_x[1],bomb_y[1]))

	elif(current_score>20):
		screen.blit(backround_image_level_3,(0,0))
		position(sky_img[2],pos_x,pos_y)
		# meteroids(asteroids_img1[index[0]],meteroids_x[0],meteroids_y[0])
		if(current_score==21):
			time.sleep(1)
			level_up_sound.play()
			current_score+=1
		meteroids(asteroids_img2[index[1]],meteroids_x[1],meteroids_y[1])
		meteroids(asteroids_img21[index[3]],meteroids_x[3],meteroids_y[3])
		meteroids(asteroids_img22[index[4]],meteroids_x[4],meteroids_y[4])
		meteroids(asteroids_img23[index[5]],meteroids_x[5],meteroids_y[5])
		meteroids(asteroids_img3[index[6]],meteroids_x[6],meteroids_y[6])
		meteroids(asteroids_img31[index[7]],meteroids_x[7],meteroids_y[7])
		meteroids(asteroids_img32[index[8]],meteroids_x[8],meteroids_y[8])
		screen.blit(bomb,(bomb_x[0],bomb_y[0]))
		screen.blit(bomb,(bomb_x[1],bomb_y[1]))
		screen.blit(bomb,(bomb_x[2],bomb_y[2]))

	else:
		screen.blit(backround_image,(0,0));
		position(sky_img[0],pos_x,pos_y)
		screen.blit(bomb,(bomb_x[0],bomb_y[0]))
		meteroids(asteroids_img1[index[0]],meteroids_x[0],meteroids_y[0])
		meteroids(asteroids_img2[index[1]],meteroids_x[1],meteroids_y[1])
	flag=True

	if(n==0):
		flag=False
	#print(n)
	if(flag==True):
		for i in range(0,n):
			screen.blit(life[i],(0+40*i,50))
	elif(flag==False):
		display=score_board_font.render("GAME OVER",True,(255,0,0))
		screen.blit(display,(0,50))
		break


	#meteroids posn
	for i in pygame.event.get():
		if(i.type==pygame.QUIT):
			running=False;
		diff=keystrokes.keyboard_controls(diff,i);
		bullet_diff=keystrokes.bullet_shoot(i,bullet_diff)
		shoot_pos=0
		
		if (i.type==pygame.KEYDOWN):
			if(i.key==pygame.K_f):
				screen = pygame.display.set_mode((800,450),pygame.FULLSCREEN);
	
	if(bullet_diff==-15):
		bul_x=bul_x+[pos_x]
		bullet_sound=mixer.Sound('sounds\\laser.wav')
		bullet_sound.set_volume(0.1);
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


		
	# new_highscore=new_highscore+[highscore];
	if (current_score==highscore+1):
		highscore_sound=mixer.Sound("sounds\\highsore.wav");
		time.sleep(0.4)
		highscore_sound.play();
		current_score=current_score+1

	if(current_score>=highscore):
		high_score_detector.highscore(current_score);
	
	########OBSTACLE MOVEMENT#######################################	
	met_y_diff=0.25;
	meteroids_y[0]+=met_y_diff;
	meteroids_y[1]+=met_y_diff;
	meteroids_y[2]+=met_y_diff;
	meteroids_y[3]+=met_y_diff;
	meteroids_y[4]+=met_y_diff;
	meteroids_y[5]+=met_y_diff;
	meteroids_y[6]+=met_y_diff;
	meteroids_y[7]+=met_y_diff;
	meteroids_y[8]+=met_y_diff;
	
	bomb_y_diff=0.25
	bomb_y[0]+=bomb_y_diff
	bomb_y[1]+=bomb_y_diff
	bomb_y[2]+=bomb_y_diff
	# screen.blit(bomb,(bomb_x[0],bomb_y[0]))
	# screen.blit(bomb,(bomb_x[1],bomb_y[1]))
	# screen.blit(bomb,(bomb_x[2],bomb_y[2]))


	# met_x_diff=5;
	# meteroids_x+=met_x_diff
	pos_x +=diff;
	bul_y +=bullet_diff;
	#################################################################
	
	
	



	if (collison[0]==True):
		
		# screen.blit(blast_img, (meteroids_x,meteroids_y))
		explosion_sound=mixer.Sound('sounds\\explosion.wav');                     
		#explosion_sound.play();
		#print(collison)
		
		#print("sound")	
		meteroids_x[0]=random.randint(0,400);
		meteroids_y[0]=-60;
		current_score+=1;

		
	

	if(meteroids_y[0]>=380):
		meteroids_x[0]=random.randint(0,750)
		meteroids_y[0]=-60;

	if(meteroids_y[1]>=380):
		meteroids_y[1]=-75

	if(meteroids_y[2]>=380):
		meteroids_x[2]=random.randint(0,750)
		meteroids_y[2]=-60;

	if(meteroids_y[3]>=380):
		meteroids_x[3]=random.randint(0,750)
		meteroids_y[3]=-75

	if(meteroids_y[4]>=380):
		meteroids_x[4]=random.randint(0,750)
		meteroids_y[4]=-75

	if(meteroids_y[5]>=380):
		meteroids_x[5]=random.randint(0,750)
		meteroids_y[5]=-60;

	if(meteroids_y[6]>=380):
		meteroids_x[6]=random.randint(0,750)
		meteroids_y[6]=-60;

	if(meteroids_y[7]>=380):
		meteroids_x[7]=random.randint(0,750)
		meteroids_y[7]=-60;

	if(meteroids_y[8]>=380):
		meteroids_x[8]=random.randint(0,750)
		meteroids_y[8]=-60;
			
	if(bomb_y[0]>=380):
		bomb_x[0]=random.randint(0,750)
		bomb_y[0]=-30;
	if(bomb_y[1]>=380):
		bomb_x[1]=random.randint(0,750)
		bomb_y[1]=-340;

	if(bomb_y[2]>=380):
		bomb_x[2]=random.randint(0,750)
		bomb_y[2]=-500;


	if(pos_x>=730):
		pos_x=730;
	if(pos_x<=0):
		pos_x=0;
	


	
	if(iteration[0]%256==0):
		index[0]+=1

	if(iteration[1]%256==0):

		index[1]+=1
	if(iteration[2]%256==0):

		index[2]+=1
	if(iteration[3]%256==0):

		index[3]+=1
	if(iteration[4]%256==0):


		index[4]+=1
	if(iteration[5]%256==0):

		index[5]+=1
	if(iteration[6]%256==0):

		index[6]+=1
	if(iteration[7]%256==0):

		index[7]+=1
	if(iteration[8]%256==0):

		index[8]+=1
	

	if(index[0]>len(asteroids_img1)-1):

		index[0]=0
	if(index[1]>len(asteroids_img1)-1):

		index[1]=0
	if(index[2]>len(asteroids_img1)-1):

		index[2]=0
	if(index[3]>len(asteroids_img1)-1):

		index[3]=0
	if(index[4]>len(asteroids_img1)-1):

		index[4]=0
	if(index[5]>len(asteroids_img1)-1):

		index[5]=0
	if(index[6]>len(asteroids_img1)-1):

		index[6]=0
	if(index[7]>len(asteroids_img1)-1):

		index[7]=0
	if(index[8]>len(asteroids_img1)-1):

		index[8]=0
	
	iteration[0]+=1
	iteration[1]+=1
	iteration[2]+=1
	iteration[3]+=1
	iteration[4]+=1
	iteration[5]+=1
	iteration[6]+=1
	iteration[7]+=1
	iteration[8]+=1

	if(current_score==50):
		running=False
	#score board load:
	score_board.score_board(highscore,current_score,highscore_board_font,score_board_font,screen);
	level_display.level_display(score_board_font,screen, current_score)
	pygame.display.update() 
if(current_score==50):
	unning=True
	main_menu.menu2(unning, screen, score_board_font, running);
if(n==0):
	unning=True
	main_menu.menu1(unning, screen, score_board_font, running)
	running=main_menu.state(running)
	
		
	

	

	
