#include "Game.h"

void Game::initVariable()
{
	this->window = nullptr;
}
void Game::initWindow()
{
	this->videomode.height = 512;
	this->videomode.width = 288;
	this->window= new RenderWindow(this->videomode, "Flappy Bird");
}

Game::Game()
{
	this->initVariable();
	this->initWindow();
}

Game::~Game()
{
	delete this->window;
}

const bool Game::running() const
{
	return this->window->isOpen();
}

void Game::pollevents()
{
	//event polling
	while (this->window->pollEvent(this->ev))
	{
		switch (this->ev.type)
		{
		case sf::Event::Closed:
			this->window->close();
			break;
		case sf::Event::KeyPressed:
			if (this->ev.key.code == sf::Keyboard::Escape)
				this->window.close();
			break;
		}
	}
}

void Game::render()
{
	this->window->clear();
	//draw game

	this->window->display();
}


