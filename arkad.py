import pygame, sys
from pygame.locals import *
import os.path
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
def loadImage(file, useColorKey=False):

    filepath = os.path.join("obrazy",file)
    image = pygame.image.load(filepath)
    image = image.convert()
    if useColorKey is True:
        colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey,RLEACCEL)
    return image

class scooby(pygame.sprite.Sprite):
    def __init__(self):
        # Inicjalizuj klasę bazową Sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = loadImage("scoobydoo.jpg",True)
        self.rect = self.image.get_rect() #rozmiar rysunku
        self.rect.center = (SCREEN_WIDTH/2,0.93*SCREEN_HEIGHT) #gdzie wstawić?
        self.x_velocity = 0
        self.y_velocity = 0

    def update(self):
        self.rect.move_ip((self.x_velocity, self.y_velocity))  # move in-place

        if self.rect.left < 0:
            self.rect.left = SCREEN_WIDTH-90
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = 90

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Scooby, how much can you eat?")


background_image = loadImage("background.jpg")
screen.blit(background_image,(0,0))

scoobySPRITE = pygame.sprite.RenderClear()
Scooby = scooby()
scoobySPRITE.add(Scooby)

clock = pygame.time.Clock()
while True:
    clock.tick(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
            elif event.key == K_LEFT:
                Scooby.x_velocity = -10
            elif event.key == K_RIGHT:
                Scooby.x_velocity = 10
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                Scooby.x_velocity = 0
            elif event.key == K_RIGHT:
                Scooby.x_velocity = 0

    scoobySPRITE.update()

    scoobySPRITE.clear(screen, background_image)

    scoobySPRITE.draw(screen)

    pygame.display.flip()