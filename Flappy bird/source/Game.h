#pragma once
#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>
#include <SFML/Window.hpp>
#include <SFML/Audio.hpp>
#include <SFML/Network.hpp>
using namespace sf;
/*class that works as game*/
class Game 
{
private:
	//variables
    //window
	RenderWindow* window;
	VideoMode videomode;
	Event ev;
	//private functions
	void initVariable();
	void initWindow();
	

	
public:
	//constructors and destructors
	Game();
	virtual ~Game();
	//Accessors
	const bool running() const;
	//Functions
	void update();
	void render();
	const bool running();
};



