from settings import *
from tetris import Tetris
import sys


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Tetris')
        pygame.display.set_icon(ProgramIcon)
        self.screen = pygame.display.set_mode(FIELD_RES)
        self.Clock = pygame.time.Clock()
        self.tetris = Tetris(self)

    def update(self):
        self.tetris.update()
        self.Clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        self.tetris.draw()
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
    
if __name__ == '__main__':
    app = App()
    app.run()