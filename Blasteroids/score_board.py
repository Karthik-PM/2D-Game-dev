import pygame;


def score_board(highscore,current_score,highscore_board_font,score_board_font,screen):
	if(highscore>=current_score):
		highscore_board=highscore_board_font.render("HIGHSCORE:"+str(highscore),True,(255,0,0))
	else:
		highscore_board=highscore_board_font.render("HIGHSCORE:"+"PASS",True,(255,0,0))

	score_board=score_board_font.render("SCORE:"+str(current_score),True,(255,0,0));
	screen.blit(highscore_board,(530,0));
	screen.blit(score_board,(630,40));
