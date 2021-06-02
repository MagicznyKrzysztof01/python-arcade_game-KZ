import pygame
from pygame.locals import *
import os.path
import random
from tkinter import *
from tkinter.font import Font
"""Programme contains game and informations
about author and game statistics."""

def Game():
    """Function, when is called starts game"""

    """Defining essential variables"""
    running = [True]
    Score = 0
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700

    def loadImage(file, useColorKey = False):
        """Function, when is called downloads image,
        which name is given as the parameter. It adjusts
        pixels to size of the image. If useColorKey is True
        im makes transparent pixels of color, as the color
        in point (0,0)."""
        filepath = os.path.join("obrazy", file)
        image = pygame.image.load(filepath)
        image = image.convert()
        if useColorKey is True:
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image


    def loadSound(name):
        """Function, when is called downloads a
        sound, which name is given as the parameter
         and returns it."""
        filepath = os.path.join("obrazy", name)
        sound = pygame.mixer.Sound(filepath)
        return sound


    class scooby(pygame.sprite.Sprite):
        """Main class, here is defined Scooby,
        which is controlled by the player"""
        def __init__(self):
            """In init Scooby has its image and is
            placed in bottom of the screen it doesn't
            move vertically and across if player doesn't
            click keys."""
            pygame.sprite.Sprite.__init__(self)
            self.image = loadImage("scoobydoo.jpg", True)
            self.rect = self.image.get_rect() #rozmiar rysunku
            self.rect.center = (SCREEN_WIDTH/2, 0.93*SCREEN_HEIGHT)
            self.x_velocity = 0
            self.y_velocity = 0

        def update(self):
            """Update method, when is called it moves Scooby,
            if Scooby cross borders of screen it appears in the
            opposite side."""
            self.rect.move_ip((self.x_velocity, self.y_velocity))

            if self.rect.left < 0:
                self.rect.left = SCREEN_WIDTH-90
            elif self.rect.right > SCREEN_WIDTH:
                self.rect.right = 90


    class good_food(pygame.sprite.Sprite):
        """Class of food which Scooby have to eat
        if he want to collect scores. If food will cross
        the borders of screen game is over."""
        def __init__(self):
            """In init food has its one of 5
            images and is placed on the upstairs
            of the screen and it move vertically
            with constant velocity."""
            list_of_good_food = ["good_food_1.jpg", "good_food_2.jpg", "good_food_3.jpg", "good_food_4.jpg", "good_food_5.jpg", ]
            pygame.sprite.Sprite.__init__(self)
            self.image = loadImage(random.choice(list_of_good_food), True)
            self.rect = self.image.get_rect()
            self.rect.centerx = random.choice([150,250,350,450,550,650,750,850])
            self.rect.centery = 100
            self.y_velocity = 5
            self.x_velocity = 0
        def update(self):
            """Update method, when is called it moves food,
            if food cross bottom border of screen loop breaks
            and game is over."""
            self.rect.move_ip((self.x_velocity, self.y_velocity))

            if self.rect.top > SCREEN_HEIGHT:
                list_of_score.append(Score)
                running.append(False)


    class bad_food(pygame.sprite.Sprite):
        """Class of food which Scooby have to avoid
         if he want to save health points. If food
         will hit Scooby healths points are reduced
         if health points are equal to 0 game is over."""
        def __init__(self):
            """In init food has its one of 5
            images and is placed on the upstairs
            of the screen and it move vertically
            with constant velocity."""
            list_of_bad_food = ["bad_food_1.jpg", "bad_food_2.jpg", "bad_food_3.jpg", "bad_food_4.jpg", "bad_food_5.jpg", ]
            pygame.sprite.Sprite.__init__(self)
            self.image = loadImage(random.choice(list_of_bad_food), True)
            self.rect = self.image.get_rect()
            self.rect.centerx = random.choice([100,200,300,400,500,600,700,800,900])
            self.rect.centery = 100
            self.y_velocity = 5
            self.x_velocity = 0
        def update(self):
            """Update method, when is called it moves food."""
            self.rect.move_ip((self.x_velocity, self.y_velocity))
            if self.rect.top > SCREEN_HEIGHT:
                pass


    class ScoreBoard(pygame.sprite.Sprite):
        """Class of Scoreboard shown on the
        screen and updates if Scooby eats food."""
        def __init__(self):
            """In init Scoreboard has its text
            location font and size."""
            pygame.sprite.Sprite.__init__(self)
            self.score = 0
            self.text = "Strzały: %4d" % self.score
            self.font = pygame.font.SysFont(None,50)
            self.image = self.font.render(self.text,True,(0,0,0))
            self.rect = self.image.get_rect()

        def update(self):
            """In this methods if is called
            numbers of scores are updated plus one."""
            self.score += 1
            self.text = "Strzały: %4d" % self.score
            self.image = self.font.render(self.text,True,(0,0,0))
            self.rect = self.image.get_rect()


    class HealthPoints(pygame.sprite.Sprite):
        """Class of HealthPoints shown on the
        screen and updates if Scooby lose his health points."""
        def __init__(self):
            """In init HealthPoints has its text
            location font and size."""
            pygame.sprite.Sprite.__init__(self)
            self.score = 10
            self.text = "Zdrowie: %4d" % self.score
            self.font = pygame.font.SysFont(None,50)
            self.image = self.font.render(self.text,True,(0,0,0))
            self.rect = self.image.get_rect(x =770, y = 0)

        def update(self):
            """In this methods if is called
            numbers of scores are updated minus one.
            It adds scores to list of scores shown
            in statistics."""
            self.score -= 1
            self.text = "Zdrowie: %4d" % self.score
            self.image = self.font.render(self.text,True,(0,0,0))
            self.rect = self.image.get_rect(x =770, y = 0)
            if self.score == 0:
                list_of_score.append(Score)
    """Initialization of pygame"""
    pygame.init()

    """Making the screen"""
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Scooby, how much can you eat?")

    """Setting background image"""
    background_image = loadImage("white.jpg")
    screen.blit(background_image,(0,0))

    """Setting game sounds"""
    Scooby_good_food_sound = loadSound("good_sound.mp3")
    Scooby_bad_food_sound = loadSound("bad_sound.mp3")

    """Creating  and adding and drawing Sprites of scooby, good food and bad food"""
    scoobySPRITE = pygame.sprite.RenderClear()
    Scooby = scooby()
    scoobySPRITE.add(Scooby)

    good_foodSprites = pygame.sprite.RenderClear()
    good_foodSprites.add(good_food())

    bad_foodSprites = pygame.sprite.RenderClear()

    """Creating adding and drawing Sprites of scoreboard
    and health points."""
    scoreboardSprite = pygame.sprite.RenderClear()
    scoreboardSprite.add(ScoreBoard())
    scoreboardSprite.draw(screen)
    pygame.display.flip()

    HealthPointsSprite = pygame.sprite.RenderClear()
    HealthPointsSprite.add(HealthPoints())
    HealthPointsSprite.draw(screen)
    pygame.display.flip()

    """Creating clock to use it in loop 
    and initializing variables used in loop"""
    clock = pygame.time.Clock()
    add_good_food = 0
    add_bad_food = 0
    Health = 10

    """Main loop where the programme works."""
    while running[-1]:
        """Defining events and keyboards keys and 
        their application in game. Setting constant
        number of frames per second."""
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running.append(False)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running.append(False)
                elif event.key == K_LEFT:
                    Scooby.x_velocity = -10
                elif event.key == K_RIGHT:
                    Scooby.x_velocity = 10
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    Scooby.x_velocity = 0
                elif event.key == K_RIGHT:
                    Scooby.x_velocity = 0
        """Adding objects on screen and optimizing them
        to suitable number of ticks. """
        add_good_food += 3
        if add_good_food >= 175:
            good_foodSprites.add(good_food())
            add_good_food = 0

        add_bad_food+=1
        if add_bad_food >= 150:
            bad_foodSprites.add(bad_food())
            add_bad_food = 0
        """This part of programme works if objects collide with themselves."""
        for hit in pygame.sprite.groupcollide(good_foodSprites,scoobySPRITE,True,False):
            """If good food and scooby collide Score is added plus one,
            sounds for good food plays and Scoreboard is updating clearing 
            and drawing on the screen. Good food disappears. Scooby remains."""
            Score +=1
            Scooby_good_food_sound.play()
            scoreboardSprite.update()
            scoreboardSprite.clear(screen, background_image)
            scoreboardSprite.draw(screen)
            pygame.display.flip()

        for hit in pygame.sprite.groupcollide(bad_foodSprites, scoobySPRITE, True, False):
            """If badfood and scooby collide Health is added minus one,
            sounds for bad food plays and HealthPoints is updating clearing 
            and drawing on the screen. Bad food disappears. Scooby remains.
            If Health is equal to zero, programme stops working on."""
            Health -=1
            Scooby_bad_food_sound.play()
            HealthPointsSprite.update()
            HealthPointsSprite.clear(screen, background_image)
            HealthPointsSprite.draw(screen)
            pygame.display.flip()
            if Health == 0:
                running.append(False)
        """This part of programme keeps both counters."""
        for hit in pygame.sprite.groupcollide(scoreboardSprite, scoobySPRITE, False, False):
            pass
        for hit in pygame.sprite.groupcollide(HealthPointsSprite, scoobySPRITE, False, False):
            pass

        """Sprites are being updated."""
        scoobySPRITE.update()
        good_foodSprites.update()
        bad_foodSprites.update()
        """Sprites are being cleared."""
        scoobySPRITE.clear(screen, background_image)
        good_foodSprites.clear(screen, background_image)
        bad_foodSprites.clear(screen, background_image)
        """Sprites are being drawn on the screen."""
        scoobySPRITE.draw(screen)
        good_foodSprites.draw(screen)
        bad_foodSprites.draw(screen)

        pygame.display.flip()
    """Quiting programme"""
    pygame.quit()
def statistics():
    """Function, when is called it creates another
    GUI window with statistics from the game, which
    contains number of tries and number of score."""
    top = Toplevel()
    top.title('Statystyki')
    top.geometry('400x500+550+200')
    Try_Label = Label(top, text = "Statystyki", font = bigFont)
    Try_Label.pack()
    Try_Label.place(height=100, width=400)
    for i in range(len(list_of_score)):
        try_Label = Label(top, text="Próba: %4d" %(i+1), font=smallFont)
        try_Label.pack()
        try_Label.place(y =75 + 25*i, height=25, width=200)
        points_Label = Label(top, text="Punkty: %4d" %list_of_score[i], font=smallFont)
        points_Label.pack()
        points_Label.place(y =75 + 25*i,x=200, height=25, width=200)
def author():
    """Function, when is called it creates another
    GUI window with information about the author
    and short rules of the game."""
    top = Toplevel()
    top.title('O Autorze')
    top.geometry('400x500+550+200')
    Try_Label = Label(top, text="O mnie", font=bigFont)
    Try_Label.pack()
    Try_Label.place(height=100, width=400)
    with open("author.txt", encoding='utf-8') as f:
        file_content = f.read()
        Author_Label = Label(top, text = file_content, font= smallFont)
        Author_Label.pack()
        Author_Label.place(y =100, height = 400, width = 400)

def quit():
    """This function, when is called, closes programme"""
    root.destroy()

"""Here is main part of GUI part of programme, it 
consists of title, label and the size of window."""
root = Tk()
my_title = 'Gra'
root.title(my_title)
root.geometry('400x500+550+200')

"""In this part two fonts for the text are defined"""
smallFont = Font(
    family = "Helvetica",
    size = 15,
    weight = "bold",
    slant = "roman",
    underline =0,
    overstrike = 0)
bigFont = Font(
    family = "Helvetica",
    size = 35,
    weight = "bold",
    slant = "roman",
    underline =0,
    overstrike = 0)

"""Here is list of scores achieved in the game
and 4 buttons, every with suitable functions,
defined above."""
list_of_score = []
PlayButton = Button(root, text='Graj',font = bigFont, command=Game)
StatisticsButton = Button(root, text='Statystyki',font = bigFont, command=statistics)
AuthorButton = Button(root, text='O autorze',font = bigFont, command=author)
ExitButton = Button(root, text='Wyjdź',font = bigFont, command=quit)

"""Button are packed and placed on the screen."""
PlayButton.pack()
StatisticsButton.pack()
AuthorButton.pack()
ExitButton.pack()

PlayButton.place(height=125, width=400)
StatisticsButton.place(y = 125, height=125, width=400)
AuthorButton.place(y = 250, height=125, width=400)
ExitButton.place(y = 375,height=125, width=400)
"""Programme starts working."""
root.mainloop()