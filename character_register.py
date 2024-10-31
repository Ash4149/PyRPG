#import
import pygame
import entities.characteres.Ash as Ash
import entities.characteres.Miku as TrashMiku

#modulation
Ash_chr = Ash.ash_chr
TrashMiku_chr = TrashMiku.trashmiku_chr

characteres_list = [Ash_chr, TrashMiku_chr]    #all characteres
characteres_equip_list = [Ash_chr, TrashMiku_chr]    #characteres in the equip (the first will be the map chr sprite and they fight in this order)