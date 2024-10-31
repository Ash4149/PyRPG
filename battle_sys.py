import pygame
import custom_lib

Black = (0, 0, 0)

class Battle:
    def __init__(self, Equip_A = None, Equip_B = None):
        self.Equip_A = Equip_A
        self.Equip_B = Equip_B
        self.Background = pygame.image.load('sprites/battle_background/White_Space_Battle.png')
        self.Police = pygame.font.Font(None, 40)
        self.EntityTurnIndex = 0
        self.IsEquiqAturn = True
        self.blit_first_button = True
        self.attack_button = custom_lib.Button((700, 75), (25, 500), 'Attack')
        self.cooldown = [False, 0]
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
        index = 0
        for chr in self.Equip_A:
            screen.blit(chr.battle_sprites[0], (((200 * index) + 50), 400))
            life_text = self.Police.render(f'{self.Life_Equip_A[index]}/{chr.Life}', True, Black)
            screen.blit(life_text, (((200 * index) + 50), 550))
            index = index + 1
        
        index = 0
        for entity in self.Equip_B:
            screen.blit(entity.battle_sprites[0], (((index * 50) + 250), 150))
            life_text = self.Police.render(f'{self.Life_Equip_B[index]}/{entity.Life}', True, Black)
            screen.blit(life_text, (((index * 50) + 250), 300))
        
        if self.blit_first_button:
            self.attack_button.draw(screen)
    
    def turn(self):
        #choose who
        if self.IsEquiqAturn:
            EntityTurn = self.Equip_A[self.EntityTurnIndex]
        elif not self.IsEquiqAturn:
            EntityTurn = self.Equip_B[self.EntityTurnIndex]
        
        #use button
        if self.attack_button.is_clicked:
            print('Attacked')
            self.cooldown[0] = True
            self.EntityTurnIndex = self.EntityTurnIndex + 1
            if self.IsEquiqAturn and self.EntityTurnIndex > (len(self.Equip_A) - 1):
                self.EntityTurnIndex = 0
                self.IsEquiqAturn = False
            elif not self.IsEquiqAturn and self.EntityTurnIndex > (len(self.Equip_B) - 1):
                self.EntityTurnIndex = 0
                self.IsEquiqAturn = True
        
        #cooldown
        if self.cooldown[0]:
            self.cooldown[1] = self.cooldown[1] + 1
        if self.cooldown[1] >= 50:
            self.cooldown[0] = False
            self.cooldown[1] = 0