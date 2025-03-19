import keyboard.mouse
import pygame, sys
import keyboard
import time

pygame.init()

#screen 
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('test for pyrpg')

#color
Black = (0, 0, 0)
White = (255, 255, 255)

#police
Police = pygame.font.Font(None, 50)

#class button
class Button:
    def __init__(self, Size, Position, Text, BorderSize = 5):
        self.Size = Size
        self.Position = Position
        self.Text = Text
        self.Cooldown = False
        self.BorderSize = BorderSize
        self.timer = False
        self.clicked_nb = 0
        self.can_click = True
        self.timer_act = 0
        self.timer_comp = 0
        self.end = False
        pass

    def draw(self, screen):
        #draw case
        pygame.draw.rect(screen, Black, (self.Position[0], self.Position[1], self.Size[0], self.Size[1]), self.BorderSize, 0)
        pygame.draw.rect(screen, (125, 125, 125), ((self.Position[0] + self.BorderSize), (self.Position[1] + self.BorderSize), (self.Size[0] - 2 * self.BorderSize), (self.Size[1] - 2 * self.BorderSize)))

        #draw text
        f_text = Police.render(str(self.clicked_nb), True, Black)
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
                        if not self.timer:
                            self.timer = True
                            self.timer_act = time.perf_counter()
                        return True
        if self.timer and not self.end:
            self.timer_comp = time.perf_counter()
            if (self.timer_comp - self.timer_act) >= 5:
                self.can_click = False
                self.end = True
        
        if self.Cooldown and not keyboard.mouse.is_pressed("left"):
            self.Cooldown = False

#test data
button_test = Button((150, 100), (175, 200), 'Testeuh')

#program loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #button event
    if button_test.is_clicked():
        print('Ok')

    #fill
    screen.fill((35, 45, 125))

    #draw button
    button_test.draw(screen)
    t_text = Police.render(f"Timer: {round((button_test.timer_comp - button_test.timer_act))} /5", True, Black)
    screen.blit(t_text, (200, 50))

    if button_test.end:
        score = f"Score: {(button_test.clicked_nb / 5)}CPS"
        score_text = Police.render(score, True, Black)
        screen.blit(score_text, (200, 425))

    #flip
    pygame.display.flip()

pygame.quit()
sys.exit()