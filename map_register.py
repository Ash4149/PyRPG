#import map file
import map.map1
import map.map2

#map_data
data1 = map.map1.map_data
data2 = map.map2.map_data

register_data = [
    [data1, data2]
]

#number of map
nbs1 = map.map1.number_map
nbs2 = map.map2.number_map

register_number = [
    [nbs1, nbs2]
]

#Check the position
'''
def check_position(Character):
    if Character.x == 24:
        return "x+"
    elif Character.y == 17:
        return "y+"
    elif Character.x == 0:
        return "x-"
    elif Character.y == 0:
        return "y-"

def change_map(Character, Register, Number_register, X, Y, Chr_X, Chr_Y):
    if check_position(Character) == "x+":
        X = X + 1
        new_map = Register[Y][X]
        new_number_map = Number_register[Y][X]
        chr_x = 1
        chr_y = Chr_Y
        return new_map, new_number_map, chr_x, chr_y
    elif check_position(Character) == "y+":
        new_map = Register[Y + 1][X]
        new_number_map = Number_register[Y + 1][X]
        chr_x = Chr_X
        chr_y = 1
        return new_map, new_number_map, chr_x, chr_y
    elif check_position(Character) == "x-":
        new_map = Register[Y][X - 1]
        new_number_map = Number_register[Y][X - 1]
        chr_x = 23
        chr_y = Chr_Y
        return new_map, new_number_map, chr_x, chr_y
    elif check_position(Character) == "y-":
        new_map = Register[Y - 1][X]
        new_number_map = Number_register[Y - 1][X]
        chr_y = 1
        chr_x = Chr_X
        return new_map, new_number_map, chr_x, chr_y
    else:
        return Register[Y][X], Number_register[Y][X], Chr_X, Chr_Y
'''