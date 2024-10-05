import menu.principal_menu as menu_data
import pygame
import keyboard

#pygame init
pygame.init()

#data agencement
menu_base = menu_data.menu_data
text_police = pygame.font.Font(None, 74)

Black = (0, 0, 0)

#menu sprites
background = pygame.image.load(menu_data.background)

#function 
class Menu:
    def __init__(self) -> None:
        self.Is_opened = False
        self.Data = menu_base
        self.Background = background
        self.Police = pygame.font.Font(None, 50)
        self.cooldown = [False, 0]
        pass

    def open_close(self):
        if keyboard.is_pressed('x'):
            if not self.cooldown[0]:
                self.Is_opened = not self.Is_opened
                self.cooldown[0] = True
        
        if self.cooldown[0] and self.cooldown[1] <= 30:
            self.cooldown[1] = self.cooldown[1] + 1
        
        if self.cooldown[1] == 30:
            self.cooldown[0] = False
            self.cooldown[1] = 0

    def draw(self, screen):
        screen.blit(background, (0, 0))
        index = 0
        for text_case in self.Data:
            Position = ((800 / (len(self.Data)) * (index)), 50)
            F_Text = self.Police.render(str(text_case), True, Black)
            screen.blit(F_Text, Position)