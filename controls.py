import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

x = 0
y = 0
# use a (r, g, b) tuple for color
yellow = (255, 255, 0)
# create the basic window/screen and a title/caption
# default is a black background
screen = pygame.display.set_mode((640, 280))
pygame.display.set_caption("Text adventures with Pygame")
# pick a font you have and set its size
myfont = pygame.font.SysFont(None, 30)

pygame.display.set_caption('Animation')
while 1:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
	key = pygame.key.get_pressed()
	if key[pygame.K_UP]:
		y += 1
		print(y)
	elif key[pygame.K_DOWN]:
		y -= 1
		print(y)
	elif key[pygame.K_RIGHT]:
		x += 1
		print(x)
	elif key[pygame.K_LEFT]:
		x -= 1
		print(x)
	pygame.display.flip()
pygame.quit()