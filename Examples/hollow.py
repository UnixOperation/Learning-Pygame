import pygame
from pygame.locals import *
import random

pygame.init()
pygame.font.init()

width = 500; height = 500; screen = pygame.display.set_mode((width, height));
PlayerX = width/2; PlayerY = height/2; PlayerColor = (255,0,0); PlayerSize = 32; 
GoalX = 0; GoalY = 0; GoalColor = (0,0,255); GoalSize = 32;
running = True; maxChoice = 100; Score = 0; ScoreGoal = 100;

text_ = "Your Goal is to get " + str(ScoreGoal) + " to win!"
green = (0,255,0)
font = pygame.font.Font(None, 32)
text = font.render(text_, True, green)


class Menorna():
    def Goal(): # Moves the 'Goal' block around when the code is called
        global GoalX, GoalY
        for y in range(0, height, GoalSize):
            for x in range(0, width, GoalSize):
                choice = random.randint(0, maxChoice)
                if choice == 7:
                    GoalX = x
                    GoalY = y
                    return
                else:
                    continue
    
    def Player(): # Spawns in the 'Player' for the first time
        global PlayerX, PlayerY
        for y in range(0, height, PlayerSize):
            for x in range(0, width, PlayerSize):
                choice = random.randint(0, maxChoice)
                if choice == 7:
                    PlayerX = x
                    PlayerY = y
                    return
                else:
                    continue

Menorna.Goal()
Menorna.Player()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                PlayerY -= PlayerSize
            elif event.key == pygame.K_DOWN:
                PlayerY += PlayerSize
            elif event.key == pygame.K_LEFT:
                PlayerX -= PlayerSize
            elif event.key == pygame.K_RIGHT:
                PlayerX += PlayerSize

    if PlayerX > width - (PlayerSize / 2):
        PlayerX -= PlayerSize
    elif PlayerX < 0 - (PlayerSize / 2):
        PlayerX += PlayerSize
    elif PlayerY > height - (PlayerSize / 2):
        PlayerY -= PlayerSize
    elif PlayerY < 0 - (PlayerSize / 2):
        PlayerY += PlayerSize

    elif PlayerY == GoalY and PlayerX == GoalX:
        Menorna.Goal()
        Score = Score + 1
    
    elif Score >= ScoreGoal:
        text2_ = "Well Done, You won!, you can keep playing"
        font2 = pygame.font.Font(None, 25)
        text2 = font.render(text2_, True, green)
        screen.blit(text2, (25, 400))

    screen.blit(text, (100, 100))
    caption = "|  Hollow  |  Score: " + str(Score)
    pygame.display.set_caption(caption)
    pygame.draw.rect(screen, PlayerColor, (PlayerX, PlayerY, PlayerSize, PlayerSize))
    pygame.draw.rect(screen, GoalColor, (GoalX, GoalY, GoalSize, GoalSize))

    pygame.display.update()
    screen.fill((0,0,0))
