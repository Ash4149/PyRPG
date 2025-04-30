#import module
from keyboard import is_pressed as prsd
import pygame
import sys
import tiles_register
import map_register
import entities.entities_register
import submenu_sys
import menu_sys
import character_register
import battle_sys
import text_box_sys
import event_sys

#initialization
pygame.init()
debug_mode = True
In_battle= False
battle_data= None
current_stats= {}
textbox= text_box_sys.TextBox(["Oh hello", "Welcome to PyRPG's in dev map!", "/!\ there might be some bug /!\ "])
EventPackagesAsset={
    "Pos": [event_sys.EventPos(0, ((14, 6)), 0)]
}
EventPackages = {
    0: {"actived":True,"activation_accessibility":True,"package":[['textbox', ["Hi, i'm a friendly monster"]],]}
}

#chr init
pre_position_chr =None

#window parameters
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PyRPG - Inf_dev')
icon = pygame.image.load('icon/windows_icon.png')
pygame.display.set_icon(icon)

#Color
White = (255, 255, 255)
Black = (0, 0, 0)

#load menu
submenu = submenu_sys.Submenu()
menu = menu_sys.Menu()

# Launch Map
tile_size = 32
x_map = 0
y_map = 0
map_data = map_register.register_data[y_map][x_map]

#load tiles
tiles = tiles_register.tiles_register

#Characteres
Equiped_chr = character_register.characteres_equip_list

#move character
def move_loop(Character):
    if Character.is_animated == False:
        if prsd('up'):
            Character.move_chr(0, -1, map_data, map_data.entity)
        elif prsd('down'):
            Character.move_chr(0, 1, map_data, map_data.entity)
        elif prsd('left'):
            Character.move_chr(-1, 0, map_data, map_data.entity)
        elif prsd('right'):
            Character.move_chr(1, 0, map_data, map_data.entity)

#test
''''''

#Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_F4:
            running = False
        if event.type == pygame.FULLSCREEN:
            pygame.display.toggle_fullscreen()

    #change screen type
    if prsd('alt') and prsd('enter'):
        pygame.display.toggle_fullscreen()
    
    if menu.is_activate:
        menu.move_button()
        if not menu.cooldown[2]:
            if prsd('z'):
                if menu.current_menu==0:
                    if menu.pointed_button==0:
                        menu.current_menu=1
                    elif menu.pointed_button==2:
                        RUNNING_COND=False
                elif menu.current_menu==1:
                    if menu.pointed_button==0:
                        current_stats = menu_sys.open_save('saves/save1.json')
                        menu.is_activate=False
                    if menu.pointed_button==1:
                        menu_sys.new_save('saves/save1.json')
                menu.cooldown[2]=True
            elif prsd('x'):
                if menu.current_menu==1:
                    menu.current_menu=0
                menu.cooldown[2]=True


    if not menu.is_activate:
        #character map function
        if not textbox.is_actived:
            if not In_battle:
                if not submenu.Is_opened:
                    move_loop(Equiped_chr[0])
                    if Equiped_chr[0].x == 24:
                        x_map = x_map + 1
                        if len(map_register.register_data[y_map]) == x_map:
                            x_map = 0
                        map_data = map_register.register_data[y_map][x_map]
                        Equiped_chr[0].x = 1
                        Equiped_chr[0].is_animated = False
                        Equiped_chr[0].ChangeMapPToPP()
                    elif Equiped_chr[0].y == 18:
                        y_map = y_map + 1
                        if len(map_register.register_data) == y_map:
                            y_map = 0
                        map_data = map_register.register_data[y_map][x_map]
                        Equiped_chr[0].y = 1
                        Equiped_chr[0].is_animated = False
                        Equiped_chr[0].ChangeMapPToPP()
                    elif Equiped_chr[0].x == 0:
                        x_map = x_map - 1
                        if -1 == x_map:
                            x_map = len(map_register.register_data[y_map]) - 1
                        map_data = map_register.register_data[y_map][x_map]
                        Equiped_chr[0].x = 23
                        Equiped_chr[0].is_animated = False
                        Equiped_chr[0].ChangeMapPToPP()
                    elif Equiped_chr[0].y == 0:
                        y_map = y_map - 1
                        if -1 == y_map:
                            y_map = len(map_register.register_data) - 1
                        map_data = map_register.register_data[y_map][x_map]
                        Equiped_chr[0].y = 17
                        Equiped_chr[0].is_animated = False
                        Equiped_chr[0].ChangeMapPToPP()
                    
                    #event pos
                    for event_pos in EventPackagesAsset['Pos']:
                        if EventPackages[event_pos.code]["actived"] and event_pos.verify(Equiped_chr[0], map_data.number_map):
                            for sg_event in EventPackages[event_pos.code]["package"]:
                                if sg_event[0]=='textbox':
                                    textbox=text_box_sys.TextBox(sg_event[1])
                            EventPackages[event_pos.code]["actived"]=False
                        else:
                            if EventPackages[event_pos.code]["activation_accessibility"] and not event_pos.verify(Equiped_chr[0], map_data.number_map):
                                EventPackages[event_pos.code]["actived"]=True
                        
                    

            #battle event
            if In_battle:
                battle_data.move_in_button()
                battle_data.use_button()
            
            #menu
            if not In_battle:
                if not Equiped_chr[0].is_animated:
                    submenu.open_close()
                if submenu.Is_opened:
                    submenu.point_object()
                    submenu.open_close_submenu()  
        
            #battle sys
            '''
            if not In_battle:
                if entity.x == Equiped_chr[0].x and entity.y == Equiped_chr[0].y:
                    pre_position_chr = [Equiped_chr[0].x, Equiped_chr[0].y]
                    In_battle = True
                    battle_data = battle_sys.Battle(Equiped_chr, [entity])
                    battle_data.create_current_life()'
            '''
        elif textbox.is_actived:
            textbox.change()

    #Fill Background
    screen.fill(Black)

    #blit
    if menu.is_activate:
        menu.draw(screen)
    
    if not menu.is_activate:
        if not In_battle:
            #blit menu
            if submenu.Is_opened == True:
                submenu.draw(screen)

            # Blit map
            if submenu.Is_opened == False:
                for row in range(len(map_data.map_data)):
                    for col in range(len(map_data.map_data[0])):
                        tile_type = map_data.map_data[row][col]
                        screen.blit(tiles[tile_type], (col * tile_size, row * tile_size))

                # Blit character(es)
                Equiped_chr[0].move_animation(12)
                Equiped_chr[0].draw(screen)

                # Blit entities
                #if entity_test.active(number_map):
                if hasattr(map_data, 'entity'):
                    for entity in map_data.entity:
                        entity.ChangeMapPToPP()
                        entity.draw(screen)
                
                if textbox.is_actived:
                    textbox.blit(screen)
                        
        
        elif In_battle:
            battle_data.draw(screen)

    #debug test

    #screen flip
    pygame.display.flip()

pygame.quit()
sys.exit()