import pygame
import sys

pygame.init()
screen = pygame.Rect(0, 0, 240, 320)
disp = pygame.display.set_mode((screen.width, screen.height))
pygame.display.set_caption('Hello World!')

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BG = (0x22, 0x22, 0x22)
DG = (0x11, 0x11, 0x11)


class bar:
    # background color
    back = DG
    # height, pixels
    H = 16

    def render(self):
        pygame.draw.rect(disp, self.back, self.rect)


class top(bar):
    rect = pygame.Rect(0, 0, screen.width, bar.H)


class status(bar):
    rect = pygame.Rect(0, screen.bottom - bar.H, screen.width, bar.H)


def render():
    disp.fill(BG)
    top().render()
    status().render()
    pygame.draw.polygon(disp, GREEN, (
        (146, top.rect.bottom + top.H),
        (screen.width - top.H, 106),
        (screen.width / 5 * 4, 277),
        (56, 277), (0 + top.H, 106)
    ))


render()
while True:  # game event loop
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                pygame.quit()
                sys.exit()
            case pygame.MOUSEBUTTONDOWN:
                match event.button:
                    case 3:
                        print(event)
    # render()
    pygame.display.update()
