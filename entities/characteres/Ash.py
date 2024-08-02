import pygame
import entity_class

map_neutral = pygame.image.load('sprites/entities_sprites/ash/neutral.png')
map_up = pygame.image.load('sprites/entities_sprites/ash/up.png')
map_right = pygame.image.load('sprites/entities_sprites/ash/right.png')
map_left = pygame.image.load('sprites/entities_sprites/ash/left.png')
ash_map_sprites = [map_neutral, map_up, map_right, map_left]

ash_sprites = [ash_map_sprites]


ash_chr = entity_class.Character("Ash", 5, 5, ash_sprites, 500, 75, 20, 2, 2, 50, 62.5, 50)