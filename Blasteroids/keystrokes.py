#keyboard controls

import pygame


def keyboard_controls(diff,i):
	if(i.type==pygame.KEYDOWN):
		if(i.key==pygame.K_LEFT):
			diff=-0.5
		if(i.key==pygame.K_RIGHT):
			diff=0.5
	if(i.type==pygame.KEYUP):
		diff=0
	return diff

#bullet shooting
def bullet_shoot(i,bullet_diff):
	if(i.type==pygame.KEYDOWN):
			if(i.key==pygame.K_UP):
				bullet_diff=-15;

	return bullet_diff;







