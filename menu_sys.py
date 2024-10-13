import menu.principal_menu as menu_data
import pygame
import keyboard
import time

#pygame init
pygame.init()

#base menu data agencement
menu_base_text = menu_data.menu_data_text
menu_base = menu_data.menu_data_redirection
text_police = pygame.font.Font(None, 50)

Black = (0, 0, 0)
White = (255, 255, 255)

#menu sprites
background = pygame.image.load(menu_data.background)

#function 
class Menu:
    def __init__(self) -> None:
        self.Is_opened = False
        self.Data_text = menu_base_text
        self.Data = menu_base
        self.Background = background
        self.Police = pygame.font.Font(None, 50)
        self.cooldown = [False, 0, False, 0, False, 0]
        self.pointed_object = 0
        self.In_SubMenu = False
        self.SubMenu_Data = None
        pass

    def open_close(self):
        if not self.cooldown[0]:
            if keyboard.is_pressed('x'):
                if not self.In_SubMenu:
                    self.Is_opened = not self.Is_opened
                    self.cooldown[0] = True

        #cooldown
        if self.cooldown[0] and self.cooldown[1] <= 35:
            self.cooldown[1] = self.cooldown[1] + 1
        
        if self.cooldown[1] == 35:
            self.cooldown[0] = False
            self.cooldown[1] = 0

    def open_close_submenu(self):
        if keyboard.is_pressed('z'):
            self.In_SubMenu = True
            self.SubMenu_Data = menu_data.menu_data_redirection[self.pointed_object]
        
        if keyboard.is_pressed('x'):
            if self.In_SubMenu:
                self.In_SubMenu = False
                self.SubMenu_Data = None
                self.cooldown[0] = True

    def draw(self, screen):
        screen.blit(background, (0, 0))
        index = 0
        for text_case in self.Data_text:
            #set position
            add_x = 10
            if index == 0:
                add_x = 20
            position_X = (index * (round(800 / len(self.Data))) + add_x)
            Position = ((position_X - (len(text_case)) / 2), 50)

            #set color
            color = Black
            if self.pointed_object  == index:
                color = White

            #blit text
            F_Text = self.Police.render(str(text_case), True, color)
            screen.blit(F_Text, Position)
            index = index + 1
    
    def point_sub_menu(self):
        #move
        if  not self.cooldown[2]:
            if keyboard.is_pressed('right'):
                self.pointed_object = self.pointed_object + 1
                self.cooldown[2] = True    
            elif keyboard.is_pressed('left'):
                self.pointed_object = self.pointed_object - 1
                self.cooldown[2] = True

        #debug position
        if self.pointed_object == len(self.Data_text):
            self.pointed_object = 0
        elif self.pointed_object == -1:
            self.pointed_object = len(self.Data_text) - 1
        
        #cooldown
        if self.cooldown[2] and self.cooldown[3] <= 18:
            self.cooldown[3] = self.cooldown[3] + 1
        
        if self.cooldown[3] == 18:
            self.cooldown[2] = False
            self.cooldown[3] = 0