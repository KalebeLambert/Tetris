from settings import *
import math
from tetromino import Tetromino

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprites_group = pygame.sprite.Group()
        self.tetromino = Tetromino(self)

    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pygame.draw.rect(self.app.screen, 'black',
                (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        self.tetromino.update()
        self.sprites_group.update()

    def draw(self):
        self.draw_grid()
        self.sprites_group.draw(self.app.screen)

