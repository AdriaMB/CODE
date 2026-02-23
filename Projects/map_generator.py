from tile import Tile, plains, forest, mountain, water, swamp, character
from random import randint

class Map:
    def __init__(self, width: int, height: int) -> none:
        self.width = width
        self.height = height

        # we are defining that Map has a uninitialized method map_data of type list[list[str]]
        self.map_data : list[list[Tile]]

        # we will store the position of the player character aswell
        self.player_x = int(width / 2)
        self.player_y = int(height / 2)
        self.player_switch_tile = None





    # The keyword self is not really necessary in the defintion of the class
    def generate_map(self)->None:
        self.map_data = [[ plains for i in range(self.width)] for j in range(self.height)]
        self.generate_patch(forest, 7, 10, 10)
        self.generate_patch(mountain, 3, 11, 10)
        self.generate_patch(water, 2, 5, 10)
        self.generate_patch(swamp, 2, 5, 10)

        self.player_switch_tile = self.map_data[self.player_x][self.player_y]
        self.map_data[self.player_x][self.player_y] = character



    def generate_patch(
        self,
        tile: Tile,
        num_patches: int,
        min_size: int,
        max_size: int,
        irregular: bool = True
    )-> None:

        if min_size > max_size:
            aux = min_size
            min_size = max_size
            max_size = aux

        for _ in range(num_patches):
            width = randint(min_size, max_size)
            height = randint(min_size, max_size)
            start_x = randint(1, self.width-1-width)
            start_y = randint(1, self.height-1-height)

            # if the tile is a forest, we are going to introduce some imperfections...
            if irregular and tile == forest:
                init_start_x = randint(2, self.width - max_size)


            for i in range(height):
                for j in range(width):
                    # if the tile is water, we are going to introduce different imperfections
                    if tile == water and irregular: 
                        start_x = randint(1, self.width-width)
                        start_y = randint(1, self.height-height)
                    elif tile == forest and irregular:
                        width = randint(int(0.7*max_size), max_size)
                        start_x = init_start_x
                    self.map_data[start_y+i][start_x+j] = tile


    def display_map(self)->None:

        #Print the canvas of the map
        frame = "x" + self.width * "=" + "x\n"
        for line in self.map_data:
            row_tiles = [tile.symbol for tile in line]
            frame += "|" + "".join(row_tiles) + "|\n"
        frame += "x" + self.width * "=" + "x\n"

        print(frame)
        


    def move_character(self, x: int = 0, y:int = 0)-> None:

        #Draw the previous tile
        self.map_data[self.player_x][self.player_y] = self.player_switch_tile 

        #Update the position of the player
        self.player_x = self.player_x + x
        self.player_y = self.player_y + y

        #Store the new switch tile and move the character tile to that position
        self.player_switch_tile = self.map_data[self.player_x][self.player_y]
        self.map_data[self.player_x][self.player_y] = character