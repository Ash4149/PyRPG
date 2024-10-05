#import module
from keyboard import is_pressed as prsd
import pygame
import sys
import tiles_register
import map_register
import entities.entities_register
import menu_sys

#initialization
pygame.init()

#window parameters
fullscreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('PyRPG (in progress)')

screen_width, screen_height = 800, 600
screen_windowed = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PyRPG (in progress)')

screen = screen_windowed

#Color
White = (255, 255, 255)
Black = (0, 0, 0)

#load menu
menu = menu_sys.Menu()

# Launch Map
tile_size = 32
x_map = 0
y_map = 0
map_data = map_register.register_data[y_map][x_map]
number_map = map_register.register_number[y_map][x_map]

#load tiles
tiles = tiles_register.tiles_register

#Characteres
Ash = entities.entities_register.Characteres_register["Ash"]

#Entity
entity_test = entities.entities_register.SimpleEntities_register["EntityTest"]

#move character
def move_loop(Character):
    if Character.is_animated == False:
        if prsd('up'):
            Character.move(0, -1, map_data)
        elif prsd('down'):
            Character.move(0, 1, map_data)
        elif prsd('left'):
            Character.move(-1, 0, map_data)
        elif prsd('right'):
            Character.move(1, 0, map_data)

#Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #character map function
    if menu.Is_opened == False:
        move_loop(Ash)
        if Ash.x == 24:
            x_map = x_map + 1
            map_data = map_register.register_data[y_map][x_map]
            number_map = map_register.register_number[y_map][x_map]
            Ash.x = 1
            Ash.ChangeMapPToPP()
        elif Ash.y == 18:
            y_map = y_map + 1
            map_data = map_register.register_data[y_map][x_map]
            number_map = map_register.register_number[y_map][x_map]
            Ash.y = 1
            Ash.ChangeMapPToPP()
        elif Ash.x == 0:
            x_map = x_map - 1
            map_data = map_register.register_data[y_map][x_map]
            number_map = map_register.register_number[y_map][x_map]
            Ash.x = 23
            Ash.ChangeMapPToPP()
        elif Ash.y == 0:
            y_map = y_map - 1
            map_data = map_register.register_data[y_map][x_map]
            number_map = map_register.register_number[y_map][x_map]
            Ash.y = 17
            Ash.ChangeMapPToPP()

    if Ash.x == entity_test.x and Ash.y == entity_test.y:
        print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')

    #call menu
    menu.open_close()

    #Fill Background
    screen.fill(Black)
    
    # Blit Menu
    if menu.Is_opened == True:
        menu.draw(screen)

    # Blit map
    if menu.Is_opened == False:
        for row in range(len(map_data)):
            for col in range(len(map_data[0])):
                tile_type = map_data[row][col]
                screen.blit(tiles[tile_type], (col * tile_size, row * tile_size))

        # Blit character(es)
        Ash.move_animation(10)
        Ash.draw(screen)

        # Blit entities
        if entity_test.active(number_map):
            entity_test.replace()
            entity_test.draw(screen)
        else:
            entity_test.remove()
    
        entity_test.ChangeMapPToPP()

    #screen flip
    pygame.display.flip()

pygame.quit()
sys.exit()