import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1200, 700))
box = pygame.Rect(10,10,50,50)
x=10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sys.exit()

    if pygame.key.get_pressed()[pygame.K_d]:
        box.x +=1
    if pygame.key.get_pressed()[pygame.K_a]:
        box.x -=1
    if pygame.key.get_pressed()[pygame.K_w]:
        box.y -=1
    if pygame.key.get_pressed()[pygame.K_s]:
        box.y +=1




    #Drawing
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,150, 255), box)
    pygame.display.flip()
