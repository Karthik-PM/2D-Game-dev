#detects if currentscore is greater than highscore and overwrites it if current score is >= highscore.
def highscore(current_score):
	f=open("highscore\\highscore.txt","r");
	highscore=f.read();
	highscore=int(highscore);
	if(current_score>highscore):
		f=open("highscore\\highscore.txt","w");
		f.write(str(current_score));
		f.close();
