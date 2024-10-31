import pygame
import entity_class

tile_size = 32
tiles_move = {0, 2, 3}
EntityTestSprite = pygame.image.load('sprites/entities_sprites/simple_entities_sprites/entity_test/neutral.png')
EntityTestBattleSprite = pygame.image.load('sprites/entities_sprites/simple_entities_sprites/entity_test/Battle.png')
EntityTest = entity_class.HostileEntity("EntityTest", 14, 6, 14, 6, [[EntityTestSprite]], [EntityTestBattleSprite], 0, 50)