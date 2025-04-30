#import
import menu.principal_menu
import pygame
import keyboard
import time
import json

pygame.init()

#data
class Menu:
    def __init__(self, background=menu.principal_menu.background, button_sprites=menu.principal_menu.button_sprites, buttons_data=menu.principal_menu.buttons_data, buttons_position=(225,300),Police=pygame.font.Font(None, 50)):
        self.background = background
        self.button_sprite = button_sprites
        self.buttons_data = buttons_data
        self.buttons_position = buttons_position
        self.Police = Police
        self.current_menu = 0
        self.pointed_button = 0
        self.cooldown = [False, 0, False, 0]
        self.is_activate = True
        pass

    def draw(self, screen):
        if self.current_menu != 3:
            #blit background
            screen.blit(self.background[0], (0, 0))

            #blit buttons
            index = 0
            for button in self.buttons_data[self.current_menu]:
                screen.blit(self.button_sprite, ((400-self.button_sprite.get_width()/2), (self.buttons_position[1]+index*65)))
                index=index+1

            index=0
            for text in self.buttons_data[self.current_menu]:
                color=(0, 0, 0)
                if index==self.pointed_button:
                    color=(255, 255, 255)
                drawn_text = self.Police.render(text, True, color)
                screen.blit(drawn_text, ((425-self.button_sprite.get_width()/2), (self.buttons_position[1]+index*65+15)))
                index=index+1
        
        #blit save backups
        if self.current_menu == 3:
            #background
            screen.blit(self.background[1], (0, 0))

            #backup case
            screen.blit

            #blit backup descriptions
            file_number = self.pointed_button + 1
            with open('saves/save{file_number}.json', "r") as f:
                backup_data = json.load(f)
    
    def move_button(self):
        if not self.cooldown[0]:
            if keyboard.is_pressed('down'):
                self.pointed_button=self.pointed_button+1
                self.cooldown[0] = True
                if self.pointed_button == len(self.buttons_data[self.current_menu]):
                    self.pointed_button=0
            elif keyboard.is_pressed('up'):
                self.pointed_button=self.pointed_button-1
                self.cooldown[0] = True
                if self.pointed_button == -1:
                    self.pointed_button=len(self.buttons_data[self.current_menu])-1
        
        #cooldown
        if self.cooldown[0]:
            self.cooldown[1]=self.cooldown[1]+1
        if self.cooldown[1]==25:
            self.cooldown[0]=False
            self.cooldown[1]=0
        
        #cooldown
        if self.cooldown[2]:
            self.cooldown[3]=self.cooldown[3]+1
        if self.cooldown[3]==25:
            self.cooldown[2]=False
            self.cooldown[3]=0
    
def new_save(filename):
    stats = {
        'name': '?',
        'time played': 0,
        'personnage proprieties': {
            'personnage1': {
                'exp':0,
                'lv':0,
                'equipement': {},
                'life': 50
            }
        },
        'position': [[5, 5], 0],
        'event_stat': [['evenement', 'On or Off']],
        'inventory': ['objet'],
    }
    with open(filename, 'w') as f:
        json.dump(stats, f)
        
def open_save(filename=None):
    with open(filename, "r") as f:
        return json.load(f)