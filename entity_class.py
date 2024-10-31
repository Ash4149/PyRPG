import pygame
import random
import time
from keyboard import is_pressed as prsd

tile_size = 32
#window_size = (800, 600)

class Entity:
    def __init__(self, name, x, y ,set_x, set_y, sprites, battle_sprites=None) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.set_x = set_x
        self.set_y = set_y
        self.pixel_x = self.x * tile_size
        self.pixel_y = self.y * tile_size
        self.change_pixel_lapse = 0
        self.map_sprites = sprites[0]
        self.battle_sprites = battle_sprites
        self.is_animated = False
        self.is_running = False
        self.dx = 0
        self.dy = 0
        pass
    
    def ChangeMapPToPP(self):
        self.pixel_x = self.x * tile_size
        self.pixel_y = self.y * tile_size
    
    def remove(self):
        self.pixel_x, self.pixel_y = None, None
        self.x, self.y = None, None
    
    def replace(self):
        self.x, self.y = self.set_x, self.set_y
        self.pixel_x = self.set_x * tile_size
        self.pixel_y = self.set_y * tile_size
    
    def move_chr(self, dx, dy, map_data):
        self.dx = dx
        self.dy = dy
        if map_data[self.y + dy][self.x + dx] in {0, 2, 3}:
            if self.change_pixel_lapse == 0:
                self.x = self.x + dx
                self.y = self.y + dy
                if prsd('shift'):
                    self.is_running = True
                else:
                    self.is_running = False
            self.is_animated = True
    
    def move_animation(self, move_division):
        dpx = (self.dx * tile_size) / move_division
        dpy = (self.dy * tile_size) / move_division
        if self.is_animated == True:
            if self.change_pixel_lapse < move_division:
                if self.is_running:
                    dpx = dpx * 2
                    dpy = dpy * 2
                self.pixel_x = self.pixel_x + dpx
                self.pixel_y = self.pixel_y + dpy
                self.change_pixel_lapse = self.change_pixel_lapse + 1
                if self.is_running:
                    self.change_pixel_lapse = self.change_pixel_lapse + 1
            elif self.change_pixel_lapse >= move_division:
                self.change_pixel_lapse = 0
                self.is_animated = False

    def draw(self, screen):
        screen.blit(self.map_sprites[0], (self.pixel_x, self.pixel_y))


class Character(Entity):
    def __init__(self, name, x, y, set_x, set_y, sprites, battle_sprites, Life) -> None:
        super().__init__(name, x, y, set_x, set_y, sprites, battle_sprites)
        self.sprites = sprites
        self.set_x = set_x
        self.set_y = set_y
        self.Life = Life
        pass

class SimpleEntity(Entity):
    def __init__(self, name, x, y, set_x, set_y, sprites, battle_sprites, map, tiles_move=None) -> None:
        super().__init__(name, x, y, set_x, set_y, sprites, battle_sprites)
        self.map = map
        self.tiles_move = tiles_move
        pass
    
    def in_map(self, Number_map):
        if self.map == Number_map:
            return "+"
        elif self.map != Number_map:
            return "-"
    
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
        if not self.is_animated:
            if map_data[self.y + dy][self.x + dx] in self.tiles_move:
                if (self.x + dx) != 25 or (self.x + dx) != 0:
                    self.x = self.x + dx
                    self.is_animated = True
                if (self.y + dy) != 18 or (self.y + dy) != 0:
                    self.y = self.y + dy
                    self.is_animated = True
    
class HostileEntity(SimpleEntity):
    def __init__(self, name, x, y, set_x, set_y, sprites, battle_sprites, map, Life, tiles_move=None):
        super().__init__(name, x, y, set_x, set_y, sprites, battle_sprites, map, tiles_move)
        self.Life = Life
        pass
