import pygame 
from pygame.locals import *
def state(running):
	return running
def menu1(unning,screen,score_board_font,running):
	while unning:
			menu=pygame.image.load("assets\\menu\\endmenu.png")
			exit=score_board_font.render("EXIT ",True,(255,0,0))
			screen.blit(menu,(0,0));
			mx,my=pygame.mouse.get_pos()
			for i in pygame.event.get():

				if(i.type==pygame.QUIT):
					unning = False
					running=False
			
				#print(mx,my)
				if(i.type==MOUSEBUTTONDOWN):
					if(mx<=524 and mx>=247 and my<=191 and my>=147):
						unning=False
			if(mx<=524 and mx>=247 and my<=191 and my>=147):
				exit=score_board_font.render("EXIT",True,(0,255,0))
			screen.blit(exit,(350,147))
			pygame.display.update()

def menu2(unning,screen,score_board_font,running):
	while unning:
			menu=pygame.image.load("assets\\menu\\endmenu1.png")
			exit=score_board_font.render("EXIT ",True,(255,0,0))
			screen.blit(menu,(0,0));
			mx,my=pygame.mouse.get_pos()
			for i in pygame.event.get():

				if(i.type==pygame.QUIT):
					unning = False
					running=False
			
				#print(mx,my)
				if(i.type==MOUSEBUTTONDOWN):
					if(mx<=524 and mx>=247 and my<=191 and my>=147):
						unning=False
			if(mx<=524 and mx>=247 and my<=191 and my>=147):
				exit=score_board_font.render("EXIT",True,(0,255,0))
			screen.blit(exit,(350,147))
			pygame.display.update()
						
