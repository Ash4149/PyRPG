import pygame
import random
import time

tile_size = 32
#window_size = (800, 600)

class Entity:
    def __init__(self, name, x, y, sprites) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.map_sprites = sprites[0]
        pass
    
    def move(self, dx, dy, map_data):
        if map_data[self.y + dy][self.x + dx] in {0, 2, 3}:
            self.x = self.x + dx
            self.y = self.y + dy
    
    def sleep(self, duration):
        self.sleep_until = pygame.time.get_ticks() + (duration * 1000)

    def draw(self, screen, direction=False):
        if direction != False:
            index = 0
            if direction == "up":
                index = 1
            elif direction == "right":
                index = 2
            elif direction == "left":
                index = 3
            
            screen.blit(self.map_sprites[index], (self.x * tile_size, self.y * tile_size))
        
        elif direction == False:
            screen.blit(self.map_sprites[0], (self.x * tile_size, self.y * tile_size))


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
    def __init__(self, name, x, y, sprites, map, set_x, set_y, tiles_move=None) -> None:
        super().__init__(name, x, y, sprites)
        self.map = map
        self.set_x = set_x
        self.set_y = set_y
        self.tiles_move = tiles_move
        pass
    
    def in_map(self, Number_map):
        if self.map == Number_map:
            return "+"
        elif self.map != Number_map:
            return "-"
    
    def remove(self):
        self.x, self.y = -5, -5
    
    def replace(self):
        self.x = self.set_x
        self.y = self.set_y
    
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
            self.x = self.x + dx
            self.y = self.y + dy
            

#chr data
chr_base_sprite = pygame.Surface((tile_size, tile_size))
chr_base_sprite.fill((255, 0, 0))
