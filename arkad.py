import pygame, sys
class Game(object):
    def __init__(self):
        # Config
        self.tps_max = 100.0

        #Initialization
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 700))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        while True:
            #Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            #Rendering
            self.screen.fill((0,0,0))
            self.draw()
            pygame.display.flip()
    def tick(self):
        keys = pygame.key.get_pressed()
    def draw(self):
        pygame.draw.rect(self.screen, (0, 150, 255), pygame.Rect(20,20,100,100))
if __name__ == "__main__":
    Game()