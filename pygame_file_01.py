import pygame

width = 500
height = 500

screen = pygame.display.set_mode((width, height))

running = False
while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False
  
  pygame.display.update()
