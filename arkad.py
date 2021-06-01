import pygame
import sys
from pygame.locals import *
import os.path
import random
def Game():

    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700


    def loadImage(file, useColorKey = False):
        filepath = os.path.join("obrazy", file)
        image = pygame.image.load(filepath)
        image = image.convert()
        if useColorKey is True:
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image


    def loadSound(name):
        filepath = os.path.join("obrazy", name)
        sound = pygame.mixer.Sound(filepath)
        return sound


    class scooby(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = loadImage("scoobydoo.jpg", True)
            self.rect = self.image.get_rect() #rozmiar rysunku
            self.rect.center = (SCREEN_WIDTH/2, 0.93*SCREEN_HEIGHT)
            self.x_velocity = 0
            self.y_velocity = 0

        def update(self):
            self.rect.move_ip((self.x_velocity, self.y_velocity))

            if self.rect.left < 0:
                self.rect.left = SCREEN_WIDTH-90
            elif self.rect.right > SCREEN_WIDTH:
                self.rect.right = 90


    class good_food(pygame.sprite.Sprite):
        def __init__(self):
            list_of_good_food = ["good_food_1.jpg", "good_food_2.jpg", "good_food_3.jpg", "good_food_4.jpg", "good_food_5.jpg", ]
            pygame.sprite.Sprite.__init__(self)
            self.image = loadImage(random.choice(list_of_good_food), True)
            self.rect = self.image.get_rect()
            self.rect.centerx = random.choice([150,250,350,450,550,650,750,850])
            self.rect.centery = 100
            self.y_velocity = 5
            self.x_velocity = 0
        def update(self):
            self.rect.move_ip((self.x_velocity, self.y_velocity))

            if self.rect.top > SCREEN_HEIGHT:
                sys.exit()


    class bad_food(pygame.sprite.Sprite):
        def __init__(self):
            list_of_bad_food = ["bad_food_1.jpg", "bad_food_2.jpg", "bad_food_3.jpg", "bad_food_4.jpg", "bad_food_5.jpg", ]
            pygame.sprite.Sprite.__init__(self)
            self.image = loadImage(random.choice(list_of_bad_food), True)
            self.rect = self.image.get_rect()
            self.rect.centerx = random.choice([100,200,300,400,500,600,700,800,900])
            self.rect.centery = 100
            self.y_velocity = 5
            self.x_velocity = 0
        def update(self):
            self.rect.move_ip((self.x_velocity, self.y_velocity))

            if self.rect.top > SCREEN_HEIGHT:
                pass


    class ScoreBoard(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.score = 0
            self.text = "Strzały: %4d" % self.score
            self.font = pygame.font.SysFont(None,50)
            self.image = self.font.render(self.text,True,(0,0,0))
            self.rect = self.image.get_rect()

        def update(self):
            self.score += 1
            self.text = "Strzały: %4d" % self.score
            self.image = self.font.render(self.text,True,(0,0,0))
            self.rect = self.image.get_rect()


    class HealthPoints(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.score = 10
            self.text = "Zdrowie: %4d" % self.score
            self.font = pygame.font.SysFont(None,50)
            self.image = self.font.render(self.text,True,(0,0,0))
            self.rect = self.image.get_rect(x =770, y = 0)

        def update(self):
            self.score -= 1
            self.text = "Zdrowie: %4d" % self.score
            self.image = self.font.render(self.text,True,(0,0,0))
            self.rect = self.image.get_rect(x =770, y = 0)
            if self.score == 0:
                sys.exit()


    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Scooby, how much can you eat?")


    background_image = loadImage("white.jpg")
    screen.blit(background_image,(0,0))


    Scooby_good_food_sound = loadSound("good_sound.mp3")
    Scooby_bad_food_sound = loadSound("bad_sound.mp3")

    scoobySPRITE = pygame.sprite.RenderClear()
    Scooby = scooby()
    scoobySPRITE.add(Scooby)

    good_foodSprites = pygame.sprite.RenderClear()
    good_foodSprites.add(good_food())

    bad_foodSprites = pygame.sprite.RenderClear()

    scoreboardSprite = pygame.sprite.RenderClear()
    scoreboardSprite.add(ScoreBoard())
    scoreboardSprite.draw(screen)
    pygame.display.flip()

    HealthPointsSprite = pygame.sprite.RenderClear()
    HealthPointsSprite.add(HealthPoints())
    HealthPointsSprite.draw(screen)
    pygame.display.flip()

    clock = pygame.time.Clock()
    add_good_food = 0
    add_bad_food = 0
    score = 0
    health = 10
    while True:
        clock.tick(60)
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
        add_good_food += 3
        if add_good_food >= 175:
            good_foodSprites.add(good_food())
            add_good_food = 0

        add_bad_food+=1
        if add_bad_food >= 150:
            bad_foodSprites.add(bad_food())
            add_bad_food = 0

        for hit in pygame.sprite.groupcollide(good_foodSprites,scoobySPRITE,True,False):
            score +=1
            Scooby_good_food_sound.play()
            scoreboardSprite.update()
            scoreboardSprite.clear(screen, background_image)
            scoreboardSprite.draw(screen)
            pygame.display.flip()

        for hit in pygame.sprite.groupcollide(bad_foodSprites, scoobySPRITE, True, False):
            health+=1
            Scooby_bad_food_sound.play()
            HealthPointsSprite.update()
            HealthPointsSprite.clear(screen, background_image)
            HealthPointsSprite.draw(screen)
            pygame.display.flip()

        for hit in pygame.sprite.groupcollide(scoreboardSprite, scoobySPRITE, False, False):
            pass
        for hit in pygame.sprite.groupcollide(HealthPointsSprite, scoobySPRITE, False, False):
            pass


        scoobySPRITE.update()
        good_foodSprites.update()
        bad_foodSprites.update()

        scoobySPRITE.clear(screen, background_image)
        good_foodSprites.clear(screen, background_image)
        bad_foodSprites.clear(screen, background_image)

        scoobySPRITE.draw(screen)
        good_foodSprites.draw(screen)
        bad_foodSprites.draw(screen)

        pygame.display.flip()
Game()