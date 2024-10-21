#import simple entities from simple_entities folder 
import entities.simple_entities.EntityTest

#register
SimpleEntities_register = {
    "EntityTest": entities.simple_entities.EntityTest.EntityTest,
    
}

#on map register
entities_localisation_register = [
    [SimpleEntities_register["EntityTest"]],    #Nb 0
    [],    #Nb 1
    [],    #Nb 2
]