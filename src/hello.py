import pygame
import sys
from pygame.locals import *

W = 240
H = 320

pygame.init()
DISPLAYSURF = pygame.display.set_mode((W, H))
pygame.display.set_caption('Hello World!')

while True:  # main game loop
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                pygame.quit()
                sys.exit()
            case pygame.MOUSEBUTTONDOWN:
                match event.button:
                    case 3:
                        print(event)
    pygame.display.update()
