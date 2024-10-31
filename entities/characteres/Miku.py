import pygame
import entity_class

#set png
MikuMapSprite = pygame.image.load('sprites/entities_sprites/miku/neutral.png')
MikuBattleSprites = pygame.image.load('sprites/entities_sprites/miku/battle_sprites.png')

miku_map_sprites = [MikuMapSprite]
miku_battle_sprites = [MikuBattleSprites]


trashmiku_chr = entity_class.Character("TrashMiku", 5, 5, 5, 5, [miku_map_sprites], miku_battle_sprites, 500)