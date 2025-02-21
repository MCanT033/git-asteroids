import pygame
from constants import *


def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
		
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		screen.fill((0,0,0))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		dt = clock.tick(60)/1000
	

print("Starting Asteroids!")
print("Screen width: 1280")
print("Screen height: 720")

main()

