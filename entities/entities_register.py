#import characteres from characteres folder
import entities.characteres
import entities.characteres.Ash

#import simple entities from simple_entities folder 
import entities.simple_entities
import entities.simple_entities.EntityTest


Characteres_register = {
    "Ash": entities.characteres.Ash.ash_chr
}

SimpleEntities_register = {
    "EntityTest": entities.simple_entities.EntityTest.EntityTest
}