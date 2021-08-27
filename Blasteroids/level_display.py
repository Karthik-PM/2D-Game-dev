import pygame

def level_display(score_board_font,screen,current_score):
	if(current_score>10 and current_score<20):
		level="2"
	elif(current_score>20):
		level="3"
	else:
		level="1"

	level_disp=score_board_font.render("LEVEL:"+level,True,(255,0,0))
	screen.blit(level_disp,(0,0))
