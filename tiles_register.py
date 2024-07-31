import pygame

#Load tiles images
grass_tile = pygame.image.load('sprites/tiles_sprites/grass.png')
water_tile = pygame.image.load('sprites/tiles_sprites/water.png')
wood_bridge_tile = pygame.image.load('sprites/tiles_sprites/wood_bridge.png')
sand_tile = pygame.image.load('sprites/tiles_sprites/sand.png')

tiles_register = {
    0: grass_tile,
    1: water_tile,
    2: wood_bridge_tile,
    3: sand_tile,
}