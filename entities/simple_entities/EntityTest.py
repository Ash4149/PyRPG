import pygame
import entity_class

tile_size = 32
tiles_move = {0, 2, 3}
EntityTestSprite = pygame.image.load('sprites/entities_sprites/simple_entities_sprites/entity_test/neutral.png')
EntityTest = entity_class.SimpleEntity("EntityTest", 17, 6, 17, 6,[[EntityTestSprite]], 0, tiles_move)