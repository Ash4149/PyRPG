import pygame
import keyboard

Black = (0, 0, 0)
white = (255, 255, 255)

class Battle:
    def __init__(self, Equip_A = None, Equip_B = None):
        self.Equip_A = Equip_A
        self.Equip_B = Equip_B
        self.Background = pygame.image.load('sprites/battle_background/White_Space_Battle.png')
        self.Police = pygame.font.Font(None, 40)
        self.EntityTurnIndex = 0
        self.IsEquiqAturn = True
        self.blit_witch_button = 0
        self.first_button = ['Fight', 'Run']
        self.fight_button = ['Attack', 'Skill', 'Heal', 'Special']
        self.pointed_button = 0
        self.cooldown = [False, 0, False, 0]
        pass
    
    def create_current_life(self):
        self.Life_Equip_A = []
        self.Life_Equip_B = []
        index = 0
        for chr in self.Equip_A:
            self.Life_Equip_A.insert(index, chr.Life)
            index = index + 1
        
        index = 0
        for entity in self.Equip_B:
            self.Life_Equip_B.insert(index, entity.Life)
            index = index + 1

    def draw(self, screen):
        screen.blit(self.Background, (0, 0))

        #life and chr
        index = 0
        for chr in self.Equip_A:
            screen.blit(chr.battle_sprites[0], (((200 * index) + 50), 350))
            life_text = self.Police.render(f'{self.Life_Equip_A[index]}/{chr.Life}', True, Black)
            screen.blit(life_text, (((200 * index) + 50), 500))
            index = index + 1

        index = 0
        for entity in self.Equip_B:
            screen.blit(entity.battle_sprites[0], (((index * 50) + 250), 150))
            life_text = self.Police.render(f'{self.Life_Equip_B[index]}/{entity.Life}', True, Black)
            screen.blit(life_text, (((index * 50) + 250), 300))
        
        #blit first button
        if self.blit_witch_button == 0:
            button_index = 0
            for first_button in self.first_button:
                pygame.draw.rect(screen, (50, 50, 50), ((35 + (button_index * 375)), 530, 357, 50))
                pygame.draw.rect(screen, Black, ((35 + (button_index * 375)), 530, 357, 50), 5, 5)
                button_text_color = Black
                if self.pointed_button == button_index:
                    button_text_color = white
                first_button_text = self.Police.render(self.first_button[button_index], True, button_text_color)
                screen.blit(first_button_text, ((225 - ((len(self.fight_button[button_index]* 15)) / 2) + (button_index * 365)), 540))
                button_index = button_index + 1
        
        #blit fight button
        if self.blit_witch_button == 1:
            button_index = 0
            for fight_button in self.fight_button:
                pygame.draw.rect(screen, (50, 50, 50), ((37 + (button_index * 183)), 530, 179, 50))
                pygame.draw.rect(screen, Black, ((37 + (button_index * 183)), 530, 179, 50), 5, 5)
                button_text_color = Black
                if self.pointed_button == button_index:
                    button_text_color = white
                fight_button_text = self.Police.render(self.fight_button[button_index], True, button_text_color)
                screen.blit(fight_button_text, (((button_index * 179 + 149) - ((len(self.fight_button[0]* 20)) / 2)), 540))
                button_index = button_index + 1


    def move_in_button(self):
        #choose in witch button
        if self.blit_witch_button == 0:
            in_witch_button = self.first_button
        elif self.blit_witch_button == 1:
            in_witch_button = self.fight_button

        #move in button
        if not self.cooldown[0]:
            if keyboard.is_pressed('left'):
                self.pointed_button = self.pointed_button - 1
                if self.pointed_button == -1:
                    self.pointed_button = len(in_witch_button) - 1
                self.cooldown[0] = True
            elif keyboard.is_pressed('right'):
                self.pointed_button = self.pointed_button + 1
                if self.pointed_button == len(in_witch_button):
                    self.pointed_button = 0
                self.cooldown[0] = True
        
        #cooldown
        if self.cooldown[0] and self.cooldown[1] <= 35:
            self.cooldown[1] = self.cooldown[1] + 1
        
        if self.cooldown[1] == 25:
            self.cooldown[0] = False
            self.cooldown[1] = 0

        if self.cooldown[0]:
            if not keyboard.is_pressed('left') and not keyboard.is_pressed('right'):
                self.cooldown[0] = False
                self.cooldown[1] = 0

    def use_button(self):
        if not self.cooldown[2]:
            if keyboard.is_pressed('z'):
                if self.pointed_button == 0:
                    if self.blit_witch_button == 0:
                        self.blit_witch_button = 1
                        self.cooldown[2] = True
                    elif self.blit_witch_button == 1:
                        self.Life_Equip_B[0] = self.Life_Equip_B[0] - self.Equip_A[self.EntityTurnIndex].Atk
                        self.EntityTurnIndex = self.EntityTurnIndex + 1
                        if self.IsEquiqAturn:
                            if len(self.Equip_A) + 1 == self.EntityTurnIndex:
                                self.EntityTurnIndex
                                self.IsEquiqAturn = False
                        
                        self.blit_witch_button = 0
                        self.cooldown[2] =True
                
                elif self.pointed_button == 1:
                    if self.blit_witch_button == 0:
                        Return_obj = True

            elif keyboard.is_pressed('x'):
                if self.blit_witch_button == 1:
                    self.blit_witch_button = 0
                    self.pointed_button = 0
        
        #cooldown
        if self.cooldown[2] and self.cooldown[3] <= 35:
            self.cooldown[3] = self.cooldown[3] + 1
    
        if self.cooldown[3] == 25:
            self.cooldown[2] = False
            self.cooldown[3] = 0

        if self.cooldown[2]:
            if not keyboard.is_pressed('z') or not keyboard.is_pressed('x'):
                self.cooldown[2] = False
                self.cooldown[3] = 0