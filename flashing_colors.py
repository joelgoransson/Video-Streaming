import random
import pygame
pygame.init()

screen = pygame.display.set_mode([1280,720])

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((random.randrange(255), random.randrange(255), random.randrange(255)))

	
	pygame.display.flip()

pygame.quit()