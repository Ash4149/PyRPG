#import module
from keyboard import is_pressed as prsd
import pygame
import sys
import tiles_register

#import map
import map.map1, map.map2
import map_register

#import entities
import entities.characteres.Ash as ash_chr
import entities.simple_entities.EntityTest as entity_test_ent


global new_map


#initialization
pygame.init()

#window parameters
fullscreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('PyRPG (beta)')

screen_width, screen_height = 800, 600
screen_windowed = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PyRPG (beta)')

screen = screen_windowed

#Color
White = (255, 255, 255)
Black = (0, 0, 0)

# Launch Map
tile_size = 32
x_map = 0
y_map = 0
map_data = map_register.register_data[y_map][x_map]
number_map = map_register.register_number[y_map][x_map]

#load tiles
tiles = tiles_register.tiles_register

#Characteres
Ash = ash_chr.ash_chr

#Entity
entity_test = entity_test_ent.EntityTest

#Function mooving in loop
def move_loop(chr):
    if prsd('up'):
            chr.move(0, -1, map_data)
    elif prsd('down'):
            chr.move(0, 1, map_data)
    elif prsd('left'):
            chr.move(-1, 0, map_data)
    elif prsd('right'):
            chr.move(1, 0, map_data)

#Check position
def check_position(Character):
    if Character.x == 24:
        return "x+"
    elif Character.y == 18:
        return "y+"
    elif Character.x == 0:
        return "x-"
    elif Character.y == 0:
        return "y-"

#Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            move_loop(Ash)
    
    #Choose the map to load
    if check_position(Ash) == "x+":
        x_map = x_map + 1
        map_data = map_register.register_data[y_map][x_map]
        number_map = map_register.register_number[y_map][x_map]
        Ash.x = 1
    elif check_position(Ash) == "y+":
        y_map = y_map + 1
        map_data = map_register.register_data[y_map][x_map]
        number_map = map_register.register_number[y_map][x_map]
        Ash.y = 1
    elif check_position(Ash) == "x-":
        x_map = x_map - 1
        map_data = map_register.register_data[y_map][x_map]
        number_map = map_register.register_number[y_map][x_map]
        Ash.x = 23
    elif check_position(Ash) == "y-":
        y_map = y_map - 1
        map_data = map_register.register_data[y_map][x_map]
        number_map = map_register.register_number[y_map][x_map]
        Ash.y = 17

    #Fill Background
    screen.fill(Black)
    
    # Print map
    for row in range(len(map_data)):
        for col in range(len(map_data[0])):
            tile_type = map_data[row][col]
            screen.blit(tiles[tile_type], (col * tile_size, row * tile_size))

    # Print character(es)
    Ash.draw(screen)

    #print entities
    if entity_test.active(number_map):
        entity_test.replace()
        entity_test.draw(screen)
    else:
        entity_test.remove()
        entity_test.draw(screen)

    #screen flip
    pygame.display.flip()

pygame.quit()
sys.exit()