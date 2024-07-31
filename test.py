#Change map and number's map
'''
def change_map(Character, MapRegister, NumberRegister, X, Y, chr_x, chr_y):
    if check_position(Character) == "x+":
        X = X + 1
        new_map_data = MapRegister[Y][X]
        new_number_map = NumberRegister[Y][X]
        Character_x = 1
        Character_y = chr_y
        return new_map_data, new_number_map, Character_x, Character_y
    elif check_position(Character) == "y+":
        Y = Y + 1
        new_map_data = MapRegister[Y][X]
        new_number_map = NumberRegister[Y][X]
        Character_y = 1
        Character_x = chr_x
        return new_map_data, new_number_map, Character_x, Character_y
    elif check_position(Character) == "x-":
        X = X - 1
        new_map_data = MapRegister[Y][X]
        new_number_map = NumberRegister[Y][X]
        Character_x = 23
        Character_y = chr_y
        return new_map_data, new_number_map, Character_x, Character_y
    elif check_position(Character) == "y-":
        Y = Y - 1
        new_map_data = MapRegister[Y][X]
        new_number_map = NumberRegister[Y][X]
        Character_y = 16
        Character_x = chr_x
        return new_map_data, new_number_map, Character_x, Character_y
    else:
        new_map_data = MapRegister[Y][X]
        new_number_map = NumberRegister[Y][X]
        Character_x = chr_x
        Character_y = chr_y
        return new_map_data, new_number_map, Character_x, Character_y
'''
