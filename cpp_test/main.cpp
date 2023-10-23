#include <SDL2/SDL.h>
#include <SDL2/SDL_events.h>
#include <SDL2/SDL_shape.h>
#include <SDL2/SDL_video.h>
#include <SDL2/SDL_image.h>
#include <bits/stdc++.h>
#include <GL/gl.h>
#include <cstddef>

const int SCREEN_WIDTH = 480;
const int SCREEN_HEIGHT = 880;


int main(){
	SDL_Window* window = NULL;
	SDL_Event e;
	SDL_GLContext gl_context;
	//initalize SDL
	if(SDL_Init(SDL_INIT_TIMER | SDL_INIT_VIDEO) < 0){
		std::cout << "SDL could not initalize\n";
	}
	
	//initalize OpenGL
	SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 3);
	SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 3);

	//set window	
	window = SDL_CreateWindow("window" , 0 , 0 , SCREEN_HEIGHT , SCREEN_WIDTH , SDL_WINDOW_OPENGL);
	if(window == NULL){
		std :: cout << "Failed to initalize window\n";
	}

    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if(renderer == nullptr){
        std::cout << "failed to initalize renderer";
    }
    // adding textures
    SDL_Texture* texture = nullptr;
	SDL_Texture* astronaut_texture = nullptr;
	SDL_Texture* playerTexture = nullptr;
    SDL_Surface* surface = IMG_Load("/home/karthik/workspace/2D-Game-dev/cpp_test/Space Runner Assets - 27-11-20/runner-asset-sheet-with-transparency.png");
	SDL_Surface* astronaut = IMG_Load("/home/karthik/workspace/2D-Game-dev/cpp_test/Space Runner Assets - 27-11-20/Astronaut/Astronaut_Idle.png");

	if(surface != nullptr){
		std::cout << "image successfully loaded!!\n";
		texture = SDL_CreateTextureFromSurface(renderer, surface);
	}else{
		std::cout << "Failed to load image\n";
	}

	if(astronaut != nullptr){
		std::cout << "astronaut sprite loaded\n";
		astronaut_texture = SDL_CreateTextureFromSurface(renderer, astronaut);
	}
	// backround coords
	SDL_Rect spirteRect;	
	spirteRect.x = 200;
	spirteRect.y = 300;
	spirteRect.w = 80;
	spirteRect.h = 40;

	// player coords

	bool running = true;
	int x_cords = 0;
	int y_cords = 400;
	bool flip_texture = false;
	while(running){
		while(SDL_PollEvent(& e)){
			if(e.type == SDL_QUIT){
				running = false;
			}
			if(e.type == SDL_KEYDOWN){
				if(e.key.keysym.sym == SDLK_RIGHT){
					x_cords += 10;
					astronaut = IMG_Load("/home/karthik/workspace/2D-Game-dev/cpp_test/Space Runner Assets - 27-11-20/Astronaut/Astronaut_Run.png");
					astronaut_texture = SDL_CreateTextureFromSurface(renderer, astronaut);
					flip_texture = false;
					std::cout << "Run\n";

				}else if(e.key.keysym.sym == SDLK_LEFT){
					x_cords -= 10;
					astronaut = IMG_Load("/home/karthik/workspace/2D-Game-dev/cpp_test/Space Runner Assets - 27-11-20/Astronaut/Astronaut_Run.png");	
					astronaut_texture = SDL_CreateTextureFromSurface(renderer, astronaut);
					SDL_RendererFlip flip = SDL_FLIP_HORIZONTAL;
					flip_texture = true;	

				}else if(e.key.keysym.sym == SDLK_UP){
					astronaut = IMG_Load("/home/karthik/workspace/2D-Game-dev/cpp_test/Space Runner Assets - 27-11-20/Astronaut/Astronaut_Jump.png");
					astronaut_texture = SDL_CreateTextureFromSurface(renderer, astronaut);
					x_cords += 10;
					y_cords = x_cords * 10 + 10;
					std::cout << x_cords << " " << y_cords << "\n";
				}

			}else if(e.type == SDL_KEYUP){
				SDL_Surface* astronaut = IMG_Load("/home/karthik/workspace/2D-Game-dev/cpp_test/Space Runner Assets - 27-11-20/Astronaut/Astronaut_Idle.png");
				astronaut_texture = SDL_CreateTextureFromSurface(renderer, astronaut);
				std::cout << "Stop\n";
			}
		}
		Uint32 ticks = SDL_GetTicks();
		Uint32 sprite = (ticks / 100) % 6;	
		SDL_Rect astronaut_srcrect = {sprite*24 , 0, 24, 50};
		SDL_Rect astronaut_decrect = {x_cords, y_cords, 50, 50};
		SDL_RenderClear(renderer);
		SDL_RenderCopy(renderer, texture, &spirteRect, NULL);
		if(flip_texture){
			SDL_RenderCopyEx(renderer, astronaut_texture, &astronaut_srcrect, &astronaut_decrect, 0, NULL, SDL_FLIP_HORIZONTAL);
		}else{
			if(!flip_texture) {
				SDL_RenderCopyEx(renderer, astronaut_texture, &astronaut_srcrect, &astronaut_decrect, 0, NULL, SDL_FLIP_HORIZONTAL);
			}
			SDL_RenderCopy(renderer, astronaut_texture, &astronaut_srcrect, &astronaut_decrect);
		}
		SDL_RenderPresent(renderer);
	}

	SDL_DestroyTexture(texture);
	SDL_DestroyRenderer(renderer);
	SDL_DestroyWindow(window);
	IMG_Quit();
	SDL_Quit();
}