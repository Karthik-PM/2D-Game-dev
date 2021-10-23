#include <iostream>
#include "Game.h"
#include "Source.h"
using namespace std;
using namespace sf;
int main()
{
  Game game;
  backround_img.loadFromFile("Assets/png/BG.png");
  sf::Sprite backround_display(backround_img);
  if (!font.loadFromFile("pala.ttf"))
  {
	  cout << "couldnt load font to the panel\n";
  }
 //Game Loop
  while(game.running())
  {
		
	 //Update
	  game.update();
	//functions
	  void pollevents();
	  void update();
	  void render();
  }
	
	
    return 0;
}
