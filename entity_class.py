import pygame
import random
import time
from keyboard import is_pressed as prsd

tile_size = 32
#window_size = (800, 600)

class Entity:
    def __init__(self, name, x, y, sprites, battle_sprites=None) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.pixel_x = self.x * tile_size
        self.pixel_y = self.y * tile_size
        self.change_pixel_lapse = 0
        self.map_sprites = sprites[0]
        self.battle_sprites = battle_sprites
        self.is_animated = False
        self.dx = 0
        self.dy = 0
        pass
    
    def ChangeMapPToPP(self):
        self.pixel_x = self.x * tile_size
        self.pixel_y = self.y * tile_size
    
    def move(self, dx, dy, map_data):
        self.dx = dx
        self.dy = dy
        if map_data[self.y + dy][self.x + dx] in {0, 2, 3}:
            if self.change_pixel_lapse == 0:
                self.x = self.x + dx
                self.y = self.y + dy
            self.is_animated = True
    
    def move_animation(self, move_division):
        dpx = (self.dx * tile_size) / move_division
        dpy = (self.dy * tile_size) / move_division
        if self.change_pixel_lapse < move_division:
            if self.is_animated == True:
                self.pixel_x = self.pixel_x + dpx
                self.pixel_y = self.pixel_y + dpy
                self.change_pixel_lapse = self.change_pixel_lapse + 1
        elif self.change_pixel_lapse >= move_division:
            self.change_pixel_lapse = 0
            self.is_animated = False


    def draw(self, screen, direction=False):
        if direction != False:
            index = 0
            if direction == "up":
                index = 1
            elif direction == "right":
                index = 2
            elif direction == "left":
                index = 3
            
            screen.blit(self.map_sprites[index], (self.pixel_x, self.pixel_y))
        
        elif direction == False:
            screen.blit(self.map_sprites[0], (self.pixel_x, self.pixel_y))


class Character(Entity):
    def __init__(self, name, x, y, sprites, Life, Atk, Def, Luck, Level, Exp, More_Exp, Last_Exp) -> None:
        super().__init__(name, x, y, sprites)
        self.Atk = Atk
        self.Def = Def
        self.Level = Level
        self.Exp = Exp
        self.Luck = Luck
        self.More_Exp = More_Exp
        self.Last_Exp = Last_Exp
        self.Life = round(Life * (self.Def / 90))
        pass

    def Attack(self, enemy, More):
        Damage = self.Atk * More
        if round(random.randint(1, 10 - self.Luck)) == 1:
            enemy.Life = enemy.Life - round(random.randint(Damage + 50, Damage + 75))
        else:
            enemy.Life = enemy.Life - round(random.randint(Damage, Damage + 40))


class SimpleEntity(Entity):
    def __init__(self, name, x, y, sprites, map, tiles_move=None) -> None:
        super().__init__(name, x, y, sprites)
        self.map = map
        self.set_x = x
        self.set_y = y
        self.tiles_move = tiles_move
        pass
    
    def in_map(self, Number_map):
        if self.map == Number_map:
            return "+"
        elif self.map != Number_map:
            return "-"
    
    def remove(self):
        self.pixel_x, self.pixel_y = -5, -5
    
    def replace(self):
        self.pixel_x = self.set_x * tile_size
        self.pixel_x = self.set_y * tile_size
    
    def active(self, Current_number_map):
        if self.map == Current_number_map:
            return True
    
    def RandomMove(self, map_data):
        dy = 0
        dx = 0
        axe = random.choice(["x", "y"])
        if axe == "x":
            dx = random.choice([-1, 1])
        elif axe == "x":
            dy = random.choice([-1, 1])
        if map_data[self.y + dy][self.x + dx] in self.tiles_move:
            if (self.x + dx) != 25 or 0:
                self.x = self.x + dx
            if (self.y + dy) != 18 or 0:
                self.y = self.y + dy