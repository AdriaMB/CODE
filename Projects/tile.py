# More colours in:
# https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007
# How to made the colours:
#https://jakob-bagterp.github.io/colorist-for-python/ansi-escape-codes/standard-16-colors/

"""Normal colours"""
# "\033[ 3(letter)      0...7(colours)  m(ends the sequence)"
#        4(background)

"""Bright colours"""
# "\033[ 9(letter)      0...7(colours)  m(ends the sequence)"
#        10(background)



ANSI_RESET = "\033[0m"
ANSI_YELLOW = "\033[93m"
ANSI_GREEN = "\033[92m"
ANSI_BLUE = "\033[94m"
ANSI_RED = "\033[31m"
ANSI_WHITE = "\033[97m"
ANSI_GRAY = "\033[90m"
ANSI_MAGENTA = "\033[35m"
ANSI_CYAN = "\033[36m"

class Tile:
    def __init__(self, symbol:str, color:str = ANSI_RESET, colored: bool = True):
        self.symbol = f"{color}{symbol}{ANSI_RESET}" if colored else symbol

plains = Tile(".", ANSI_YELLOW)
forest = Tile("&", ANSI_GREEN)
mountain = Tile("A", ANSI_GRAY)
water = Tile("~", ANSI_BLUE)
swamp = Tile("~", ANSI_CYAN)


character = Tile("@", ANSI_RED)



"""
print(plains.symbol)
print(forest.symbol)
print(mountain.symbol)
"""