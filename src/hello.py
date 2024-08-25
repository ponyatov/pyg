import pygame
import sys
import os

# full screen startup
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
info = pygame.display.Info()
screen = pygame.Rect(0, 0, info.current_w / 3, info.current_h / 3)
#
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


class Cat:
    def __init__(self, img='img/cat.png'):
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()
        self.rect.centerx = screen.centerx
        self.rect.centery = screen.centery
        self.dx = 3
        self.dy = 2

    def move(self):
        if self.rect.right >= screen.right:
            self.dx -= self.dx
        if self.rect.bottom >= screen.bottom:
            self.dy -= self.dy
        if self.rect.left <= screen.left:
            self.dx -= self.dx
        if self.rect.top <= screen.top:
            self.dy -= self.dy
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

    def render(self):
        self.move()
        disp.blit(self.img, (self.rect.x, self.rect.y))


cat = Cat()


def render():
    disp.fill(BG)
    top().render()
    status().render()
    pygame.draw.polygon(disp, GREEN, (
        (top.rect.centerx, top.rect.bottom + top.H),
        (screen.width - top.H, 106),
        (screen.width / 5 * 4, screen.height / 2),
        (56, 277),
        (0 + top.H, 106)
    ))
    cat.render()


FPS = 60
fps = pygame.time.Clock()

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
    render()
    pygame.display.update()
    fps.tick(FPS)
