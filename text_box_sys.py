import pygame, keyboard

class TextBox:
    def __init__(self, text, police=pygame.font.Font(None, 25)):
        self.text = text
        self.police = police
        self.box_number = 0
        self.cooldown = [True, 0]
        self.is_actived = True
        pass
    
    def blit(self, screen):
        #rect
        pygame.draw.rect(screen, (0, 0, 0), (25, 425, 750, 150))
        pygame.draw.rect(screen, (255,255,255), (25, 425, 750, 150), 5)

        #text
        screen.blit(self.police.render(self.text[self.box_number], True, (255, 255, 255)), (50, 450))
    
    def change(self):
        if not self.cooldown[0]:
            if keyboard.is_pressed('z') and self.box_number!=len(self.text):
                self.box_number = self.box_number + 1
                self.cooldown[0]=True
            if self.box_number==len(self.text):
                self.is_actived =False
        
        #cooldown
        if self.cooldown[0]:
            self.cooldown[1]=self.cooldown[1]+1
        if self.cooldown[1]==25:
            self.cooldown[0]=False
            self.cooldown[1]=0