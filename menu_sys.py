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
        self.pointed_submenu = 0
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
            self.SubMenu_Data = menu_data.menu_data_redirection[self.pointed_submenu]
        
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
            text_color = Black
            if self.pointed_submenu == index:
                text_color = White

            #blit text
            F_Text = self.Police.render(str(text_case), True, text_color)
            screen.blit(F_Text, Position)
            index = index + 1
        
        #blit submenu data
        if self.In_SubMenu:
            i_index = 0
            blit_list = self.SubMenu_Data.copy()
            for item in blit_list:
                Position_i = (55, (i_index * 50) + 85)
                item_text_color = Black
                if self.pointed_object == i_index:
                    item_text_color = White
                i_nb = self.SubMenu_Data.count(item)
                remove_item_much_loop = i_nb - 1
                while remove_item_much_loop:
                    blit_list.remove(item)
                    remove_item_much_loop = remove_item_much_loop - 1
                I_text = self.Police.render(f"{str(item.name)} X{i_nb}", True, item_text_color)
                screen.blit(I_text, Position_i)
                if self.pointed_object == i_index:
                    D_text = self.Police.render(str(self.SubMenu_Data[i_index].description), True, Black)
                if self.pointed_object == i_index:
                    screen.blit(D_text, (800 - (len(self.SubMenu_Data[i_index].description) * 19) - 50, 450))
                i_index = i_index + 1

    def point_object(self):
        if not self.In_SubMenu:
            if  not self.cooldown[2]:
                if keyboard.is_pressed('right'):
                    self.pointed_submenu = self.pointed_submenu + 1
                    self.cooldown[2] = True
                    if self.pointed_submenu == len(self.Data_text):
                        self.pointed_submenu = 0

                elif keyboard.is_pressed('left'):
                    self.pointed_submenu = self.pointed_submenu - 1
                    self.cooldown[2] = True
                    if self.pointed_submenu == -1:
                        self.pointed_submenu = len(self.Data_text) - 1

        elif self.In_SubMenu:
            len_list_compacted = list(set(self.SubMenu_Data))
            if  not self.cooldown[2]:
                if keyboard.is_pressed('down'):
                    self.pointed_object = self.pointed_object + 1
                    self.cooldown[2] = True
                    if self.pointed_object == len(len_list_compacted):
                        self.pointed_object = 0
                elif keyboard.is_pressed('up'):
                    self.pointed_object = self.pointed_object - 1
                    self.cooldown[2] = True
                    if self.pointed_object == -1:
                        self.pointed_object= len(len_list_compacted) - 1
        
        #cooldown
        if self.cooldown[2] and self.cooldown[3] <= 18:
            self.cooldown[3] = self.cooldown[3] + 1
        
        if self.cooldown[3] == 18:
            self.cooldown[2] = False
            self.cooldown[3] = 0