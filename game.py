from settings import *
from carte import Map
from player import Player
import sys


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()
        self.image_index = 0
        self.en_mouvement = False
        self.courir = False
        self.dt = 0
        self.animation_speed = ANIMATION_SPEED  # Changer cette valeur pour ajuster la vitesse d'animation

    def load_assets(self):
        # Charger les images
        self.stone_wall = pg.image.load("textures/stonewall.png").convert()
        self.stone_wall = pg.transform.scale(self.stone_wall, (int(WALL_LARG), int(WALL_LONG)))
        self.dirt = pg.image.load("textures/dirt.png").convert()
        self.dirt = pg.transform.scale(self.dirt, (int(WALL_LARG), int(WALL_LONG)))
        self.grass = pg.image.load("textures/grass.png").convert()
        self.grass = pg.transform.scale(self.grass, (int(WALL_LARG), int(WALL_LONG)))
        self.images = {
            "up": [pg.image.load(f"sprites/Haut/tile00{i}.png").convert_alpha() for i in range(0, 5)],
            "down": [pg.image.load(f"sprites/Bas/tile00{i}.png").convert_alpha() for i in range(0, 5)],
            "left": [pg.image.load(f"sprites/Gauche/tile00{i}.png").convert_alpha() for i in range(0, 5)],
            "right": [pg.image.load(f"sprites/Droite/tile00{i}.png").convert_alpha() for i in range(0, 5)],
            "up-left": [pg.image.load(f"sprites/Haut-Gauche/tile00{i}.png").convert_alpha() for i in range(0, 5)],
            "up-right": [pg.image.load(f"sprites/Haut-droite/tile00{i}.png").convert_alpha() for i in range(0, 5)],
            "down-right": [pg.image.load(f"sprites/Bas-Droite/tile00{i}.png").convert_alpha() for i in range(0, 5)],
            "down-left": [pg.image.load(f"sprites/Bas-Gauche/tile00{i}.png").convert_alpha() for i in range(0, 5)],

        }

    def update(self):
        self.player.update()
        pg.display.flip()
        self.clock.tick(FPS)
        self.dt = self.clock.tick(FPS) / 1000  # calcul du temps écoulé en secondes
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def new_game(self):
        self.load_assets()
        self.carte = Map(self)
        self.player = Player(self)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.carte.draw_map()
        self.player.draw_player()
        pg.display.update()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_LSHIFT:
                self.player.speed = PLAYER_SPEED * 2
                self.courir = True
            else:
                self.player.speed = PLAYER_SPEED
                self.courir = False
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
