#import module
from keyboard import is_pressed as prsd
import pygame
import sys
import tiles_register
import map_register
import entities.entities_register
import menu_sys
import character_register
import battle_sys

#initialization
pygame.init()
debug_mode = True
In_battle = False
battle_data = None

#window parameters
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PyRPG (in progress)')
icon = pygame.image.load('icon/windows_icon.png')
pygame.display.set_icon(icon)

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
Equiped_chr = character_register.characteres_equip_list

#Entity
entity_test = entities.entities_register.SimpleEntities_register["EntityTest"]

#move character
def move_loop(Character):
    if Character.is_animated == False:
        if prsd('up'):
            Character.move_chr(0, -1, map_data)
        elif prsd('down'):
            Character.move_chr(0, 1, map_data)
        elif prsd('left'):
            Character.move_chr(-1, 0, map_data)
        elif prsd('right'):
            Character.move_chr(1, 0, map_data)

#Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_F4:
            running = False

    #character map function
    if not In_battle:
        if menu.Is_opened == False:
            move_loop(Equiped_chr[0])
            if Equiped_chr[0].x == 24:
                x_map = x_map + 1
                if len(map_register.register_data[y_map]) == x_map:
                    x_map = 0
                map_data = map_register.register_data[y_map][x_map]
                number_map = map_register.register_number[y_map][x_map]
                Equiped_chr[0].x = 1
                Equiped_chr[0].is_animated = False
                Equiped_chr[0].ChangeMapPToPP()
            elif Equiped_chr[0].y == 18:
                y_map = y_map + 1
                if len(map_register.register_data) == y_map:
                    y_map = 0
                map_data = map_register.register_data[y_map][x_map]
                number_map = map_register.register_number[y_map][x_map]
                Equiped_chr[0].y = 1
                Equiped_chr[0].is_animated = False
                Equiped_chr[0].ChangeMapPToPP()
            elif Equiped_chr[0].x == 0:
                x_map = x_map - 1
                if -1 == x_map:
                    x_map = len(map_register.register_data[y_map]) - 1
                map_data = map_register.register_data[y_map][x_map]
                number_map = map_register.register_number[y_map][x_map]
                Equiped_chr[0].x = 23
                Equiped_chr[0].is_animated = False
                Equiped_chr[0].ChangeMapPToPP()
            elif Equiped_chr[0].y == 0:
                y_map = y_map - 1
                if -1 == y_map:
                    y_map = len(map_register.register_data) - 1
                map_data = map_register.register_data[y_map][x_map]
                number_map = map_register.register_number[y_map][x_map]
                Equiped_chr[0].y = 17
                Equiped_chr[0].is_animated = False
                Equiped_chr[0].ChangeMapPToPP()

    #change screen
    if prsd('alt') and prsd('enter'):
        pygame.display.toggle_fullscreen()

    #menu
    if not In_battle:
        if not Equiped_chr[0].is_animated:
            menu.open_close()
        if menu.Is_opened:
            menu.point_object()
            menu.open_close_submenu()

    #Fill Background
    screen.fill(Black)

    #blit
    if not In_battle:
        #blit menu
        if menu.Is_opened == True:
            menu.draw(screen)

        # Blit map
        if menu.Is_opened == False:
            for row in range(len(map_data)):
                for col in range(len(map_data[0])):
                    tile_type = map_data[row][col]
                    screen.blit(tiles[tile_type], (col * tile_size, row * tile_size))

            # Blit character(es)
            Equiped_chr[0].move_animation(12)
            Equiped_chr[0].draw(screen)

            # Blit entities
            if entity_test.active(number_map):
                entity_test.replace()
                entity_test.ChangeMapPToPP()
                entity_test.draw(screen)
                if entity_test.x == Equiped_chr[0].x and entity_test.y == Equiped_chr[0].y:
                    In_battle = True
                    battle_data = battle_sys.Battle(Equiped_chr, [entity_test])
                    battle_data.create_current_life()
            else:
                entity_test.remove()
    
    elif In_battle:
        battle_data.draw(screen)
        battle_data.turn()

    #debug test

    #screen flip
    pygame.display.flip()

pygame.quit()
sys.exit()