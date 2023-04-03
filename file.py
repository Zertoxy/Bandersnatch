import tkinter as tk

mini_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]


class Game:
    screen_height = 600
    screen_width = 210

    def __init__(self):
        self.key_press = {"q": False, "d": False, "z": False, "s": False}
        self.screen = tk.Tk()
        self.screen.after(1, None)
        self.carte = Map(self)
        self.player = Player(55, 55, self.carte)

    def press(self, event):
        self.key_press[event.keysym] = True
        self.move(event)

    def release(self, event):
        self.key_press[event.keysym] = False

    def move(self, event):
        key = event.keysym
        if key == "z" or self.key_press["z"]:
            self.player.moveZ()
        if key == "d" or self.key_press["d"]:
            self.player.moveD()
        if key == "s" or self.key_press["s"]:
            self.player.moveS()
        if key == "q" or self.key_press["q"]:
            self.player.moveQ()

    def draw(self):
        self.carte.create_map()
        self.carte.drawmap()
        self.player.draw_player()

    def run(self):
        self.screen.title("Bandersnatch")
        self.screen.geometry("{}x{}".format(Game.screen_height, Game.screen_width))
        # self.carte.can.bind("<z>", self.player.moveZ)
        # self.carte.can.bind("<q>", self.player.moveQ)
        # self.carte.can.bind("<s>", self.player.moveS)
        # self.carte.can.bind("<d>", self.player.moveD)
        for key in ["z", "q", "d", "s"]:
            self.carte.can.bind('<KeyPress-%s>' % key, self.press)
            self.carte.can.bind('<KeyRelease-%s>' % key, self.release)
        self.carte.can.focus_set()
        self.draw()
        self.screen.mainloop()


class Map:
    tile_size = 30

    def __init__(self, game):
        self.game = game
        self.world_map = {}
        self.can = tk.Canvas(self.game.screen, highlightthickness=0, bg='grey')
        self.can.pack(fill=tk.BOTH, expand=True)

    def create_map(self):
        for l, col in enumerate(mini_map):
            for i, value in enumerate(col):
                if value:
                    self.world_map[(i, l)] = value

        print(self.world_map)


    def drawmap(self):
        for pos in self.world_map:
            if self.world_map[pos] == 1:
                x, y = pos
                bl = tk.Canvas(self.can, width=Map.tile_size, height=Map.tile_size, bg="black")
                bl.place(x=x * Map.tile_size, y=y * Map.tile_size)
                # self.can.create_rectangle(x * Map.tile_size, y * Map.tile_size, (x + 1) * Map.tile_size,
                #                           (y + 1) * Map.tile_size, fill="black", outline="white")
class Player:
    def __init__(self, posX, posY, cte, image=None, taille=40):
        self.carte = cte
        self.rect = tk.Canvas(self.carte.can, width=taille, height=taille, bg='red')
        self.posX = posX
        self.posY = posY
        self.rect.place(x=self.posX, y=self.posY)
        self.taille = taille
        self.image = image
        self.speed = 5

    def draw_player(self):
        # self.rect.create_oval(self.taille/2 - self.taille/2,
        #                      self.taille/2 - self.taille/2,
        #                      self.taille/2 + self.taille/2,
        #                      self.taille/2 + self.taille/2, fill='red')
        self.rect.place(x=self.posX, y=self.posY)

    def coll(self):
        if self.posX > Game.screen_height - Map.tile_size - self.taille - self.speed:
            self.posX -= self.speed
        if self.posX < 0 + Map.tile_size:
            self.posX += self.speed
        if self.posY > Game.screen_width - Map.tile_size - self.taille - self.speed:
            self.posY -= self.speed
        if self.posY < 0 + Map.tile_size:
            self.posY += self.speed
        print(self.rect.find_overlapping(self.posX,self.posY,self.posX+self.taille,self.posY+self.taille))

    def moveZ(self):
        self.posY -= self.speed
        self.coll()
        self.draw_player()
        print(self.posX, self.posY)

    def moveQ(self):
        self.posX -= self.speed
        self.coll()
        self.draw_player()
        print(self.posX, self.posY)

    def moveS(self):
        self.posY += self.speed
        self.coll()
        self.draw_player()
        print(self.posX, self.posY)

    def moveD(self):
        self.posX += self.speed
        self.coll()
        self.draw_player()
        print(self.posX, self.posY)

if __name__ == "__main__":
    game = Game()
    game.run()
