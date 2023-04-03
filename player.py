from settings import *


class Player:
    def __init__(self, game):
        self.x, self.y = PLAYER_POS
        self.x = self.x * WALL_LARG + WALL_LARG // 2  # conversion en pixels
        self.y = self.y * WALL_LONG + WALL_LONG // 2  # conversion en pixels
        self.game = game
        self.speed = PLAYER_SPEED
        self.animation_time = 0
        self.direction = [0, 0, 0, 0]
        self.image_direction = 'down'
        self.last_direction = 'down'

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_z]:
            self.direction[0] = 1
        else:
            self.direction[0] = 0
        if keys[pg.K_q]:
            self.direction[1] = 1
        else:
            self.direction[1] = 0
        if keys[pg.K_s]:
            self.direction[2] = 1
        else:
            self.direction[2] = 0
        if keys[pg.K_d]:
            self.direction[3] = 1
        else:
            self.direction[3] = 0

        self.image_direction = self.get_image_direction()

        # Déplacement effectif seulement s'il n'y a pas de collision
        if self.direction != [0, 0, 0, 0]:
            self.game.en_mouvement = True
            new_x, new_y = self.x, self.y
            if self.direction[0] == 1:
                new_y -= self.speed
            if self.direction[1] == 1:
                new_x -= self.speed
            if self.direction[2] == 1:
                new_y += self.speed
            if self.direction[3] == 1:
                new_x += self.speed
            # Vérifier si le nouveau déplacement entraîne une collision avec un mur
            colliding = False
            for pos in self.game.carte.world_map:
                if self.game.carte.world_map[pos] == 1:
                    if self.player_coll(pos[0] * WALL_LARG, pos[1] * WALL_LONG, new_x, new_y):
                        colliding = True
                        break

            # Déplacement effectif seulement s'il n'y a pas de collision
            if not colliding:
                self.x, self.y = new_x, new_y

            # Réinitialiser la direction de mouvement
            self.direction = [0, 0, 0, 0]
        else:
            self.game.en_mouvement = False

    def update(self):
        self.move()
        self.animate(self.game.dt)

    def draw_player(self):
        # pg.draw.circle(self.game.screen, 'white', (int(self.x), int(self.y)), int(PLAYER_SIZE / 2))
        if self.game.en_mouvement:
            player_image = self.game.images[self.image_direction][self.game.image_index]
        else:
            if self.image_direction is None:
                self.image_direction = 'down'
            player_image = self.game.images[self.image_direction][0] # J'aimerai mettre ici la denière direction mais c'est toujours None
        player_rect = pg.Rect(int(self.x), int(self.y), 48, 78)
        self.game.screen.blit(player_image, player_rect)

    def get_image_direction(self):
        # Retourne la direction de l'image à afficher en fonction de la direction du joueur
        if self.direction == [1, 0, 0, 0]:
            return "up"
        elif self.direction == [1, 0, 0, 1]:
            return "up-right"
        elif self.direction == [1, 1, 0, 0]:
            return "up-left"
        elif self.direction == [0, 0, 1, 1]:
            return "down-right"
        elif self.direction == [0, 1, 1, 0]:
            return "down-left"
        elif self.direction == [0, 1, 0, 0]:
            return "left"
        elif self.direction == [0, 0, 1, 0]:
            return "down"
        elif self.direction == [0, 0, 0, 1]:
            return "right"

    def animate(self, dt):
        self.animation_time += dt
        if self.game.courir:
            self.game.image_index = int((self.animation_time / ANIMATION_SPEED) % 2)
        else:
            self.game.image_index = int((self.animation_time / ANIMATION_SPEED) % 2)
        print(self.image_direction)
        self.last_direction = self.image_direction

    def player_coll(self, rect_x, rect_y, new_x, new_y):
        # Trouver la distance entre le centre du cercle et les bords du mur
        closest_x = max(rect_x, min(new_x, rect_x + WALL_LARG))
        closest_y = max(rect_y, min(new_y, rect_y + WALL_LONG))
        dist = math.sqrt((closest_x - new_x) ** 2 + (closest_y - new_y) ** 2)
        # pg.draw.line(self.game.screen, 'red', (closest_x, closest_y), (new_x, new_y))

        # Vérifier si la distance est inférieure ou égale au rayon du cercle
        if dist <= PLAYER_SIZE // 2 - PLAYER_SPEED + 5:
            return True
        else:
            return False

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
