from settings import *


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
        self.textures = {
            1: (self.game.stone_wall, pg.Rect(0, 0, WALL_LARG, WALL_LONG)),
            2: (self.game.grass, pg.Rect(0, 0, WALL_LARG, WALL_LONG)),
            3: (self.game.dirt, pg.Rect(0, 0, WALL_LARG, WALL_LONG))
        }

    def get_map(self):
        for ligne, col in enumerate(mini_map):
            for i, value in enumerate(col):
                if value:
                    self.world_map[(i, ligne)] = value

    def draw_map(self):
        # SANS LES TEXTURES DE MURS
        # [pg.draw.rect(self.game.screen, 'red', (pos[0] * WALL_LARG, pos[1] * WALL_LONG, WALL_LARG, WALL_LONG), 2) for
        #  pos in
        #  self.world_map]
        for pos, value in self.world_map.items():
            texture, rect = self.textures[value]
            rect.x, rect.y = pos[0] * WALL_LARG, pos[1] * WALL_LONG
            self.game.screen.blit(texture, rect)
