# Paramètres du jeu

import pygame as pg

pg.init()
_ = False
mini_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1],
            [1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1],
            [1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 1, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 1, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 1, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 3, 2, 2, 1, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 3, 2, 2, 1, 1, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 1, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

INFO = pg.display.Info()
RES = LARGEUR, HAUTEUR = INFO.current_w, INFO.current_h
FPS = 60
ANIMATION_SPEED = 0.15
WALL_LARG = int(LARGEUR / len(mini_map[0]))
WALL_LONG = int(HAUTEUR / len(mini_map))

PLAYER_POS = 10, 10
PLAYER_SPEED = 5
PLAYER_SIZE = 48

# Personnages du jeu générés à partir de ce lien
# https://itch.io/queue/c/1866035/pixel-art-generators?game_id=1870515
