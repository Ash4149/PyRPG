import pygame
import entity_class

tile_size = 32
tiles_move = {0, 2, 3}
#EntityTestSprite = 'sprites/entities_sprites/simple_entities_sprites/entity_test/neutral.png'
EntityTestSprite = pygame.Surface((tile_size, tile_size))
EntityTest = entity_class.SimpleEntity("EntityTest", 8, 6, EntityTestSprite, 0, 8, 6, tiles_move)
EntityTestSprite.fill((255, 0, 0))