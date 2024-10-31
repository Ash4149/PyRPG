#import
import keyboard.mouse
import pygame, keyboard

#color
Black = (0, 0, 0)
Gray = ()

#class button
class Button:
    def __init__(self, Size, Position, Text, BorderSize=2, ButtonBorderColor=(0, 0, 0), ButtonBackgroundColor=(125, 125, 125), TextColor=(0, 0, 0), Police=pygame.font.Font(None, 50)):
        self.Size = Size
        self.Position = Position
        self.Text = Text
        self.BorderSize = BorderSize
        self.ButtonBorderColor = ButtonBorderColor
        self.ButtonBackgroundColor = ButtonBackgroundColor
        self.TextColor = TextColor
        self.Police = Police
        self.Cooldown = False
        pass

    def draw(self, screen):
        #draw case
        pygame.draw.rect(screen, self.ButtonBorderColor, (self.Position[0], self.Position[1], self.Size[0], self.Size[1]), 5, 0)
        pygame.draw.rect(screen, self.ButtonBackgroundColor, ((self.Position[0] + self.BorderSize), (self.Position[1] + self.BorderSize), (self.Size[0] - 2 * self.BorderSize), (self.Size[1] - 2 * self.BorderSize)))

        #draw text
        f_text = self.Police.render(self.Text, True, self.TextColor)
        text_size = (f_text.get_width(), f_text.get_height())
        screen.blit(f_text, (((self.Position[0] + (self.Size[0] / 2)) - (text_size[0] / 2)), ((self.Position[1] + (self.Size[1] / 2))) - (text_size[1] / 2)))

    def is_clicked(self):
        mouse_position = pygame.mouse.get_pos()
        if not self.Cooldown and self.can_click:
            if mouse_position[0] > self.Position[0] and mouse_position[1] > self.Position[1]:
                if mouse_position[0] < (self.Position[0] + self.Size[0]) and mouse_position[1] < (self.Position[1] + self.Size[1]):
                    if keyboard.mouse.is_pressed('left'):
                        self.Cooldown = True
                        self.clicked_nb = self.clicked_nb + 1
                        return True
        
        if self.Cooldown and not keyboard.mouse.is_pressed("left"):
            self.Cooldown = False