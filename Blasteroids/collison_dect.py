#collison detection
def collision_detect(meteroids_x,meteroids_y,bul_x_pos,bul_y):
	if(bul_x_pos>=meteroids_x-24 and bul_x_pos<=meteroids_x+24):
		if(bul_y<=meteroids_y):
			return True;
			
	else:
		return False;