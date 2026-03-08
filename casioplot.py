#ymksw 2026
import pygame
from time import sleep

# pygame setup
pygame.init()
screen = pygame.display.set_mode((384, 192))


def clear_screen():
    screen.fill("white")

def show_screen():
    pygame.display.flip()
    sleep(0.01)

def set_pixel(x,y,col=(0,0,0)):
    screen.set_at((x,y),col)


pygame.font.init()
my_font = pygame.font.SysFont('JetBrainsMonoNLNerdFontMono', 20)

def draw_string(x,y,string,color=(0,0,0),size="medium"):
    text_surface = my_font.render(string, False, color)
    screen.blit(text_surface, (x,y))

def getkey():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        return 14
    if keys[pygame.K_DOWN]:
        return 34
    if keys[pygame.K_LEFT]:
        return 23
    if keys[pygame.K_RIGHT]:
        return 25
    if keys[pygame.K_SPACE]: #OK
        return 24
    if keys[pygame.K_RETURN]: #tools
        return 36
    if True in keys:
        return 96
    return 0
