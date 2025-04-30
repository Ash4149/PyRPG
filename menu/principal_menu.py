import pygame
pygame.init()

#data
background = [pygame.image.load('sprites/menu/background/background.png'), pygame.image.load('sprites/menu/background/backups_background.png')]
buttons_data = [['Start', 'Config', 'Quit'],['Load', 'New','Delete','Copy']]
button_sprites = pygame.image.load('sprites/menu/gui/buttons.png')
