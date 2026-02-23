#   Link: https://www.youtube.com/watch?v=Lezk01D4ToE
import os
import curses # library for making a fast, reactive input


from map_generator import Map

def run() -> None:
    while True:
        os.system("clear")

        map.display_map()
        player_order = input("> ")

        if player_order == "a":
            map.move_character(-1, 0)
        elif player_order == "d":
            map.move_character(1, 0)
        elif player_order == "s":
            map.move_character(0, -1)
        elif player_order == "w":
            map.move_character(0, 1)


        
if __name__ == "__main__":

    # curses library
    stdscr = curses.initscr()
    #curses.noecho()         # turn off automatic echoing of keys to the screen, in order to be able to read keys and only display them under certain circumstances. 
    #curses.cbreak()         # react to keys instantly, without requiring the Enter key to be pressed
    #stdscr.keypad(True)     # special keys, such as the cursor keys or navigation keys such as Page Up and Home

    map_w, map_h = 30, 20
    map = Map(map_w, map_h)
    map.generate_map()


    os.system("clear")
    run()


    # For termination
    #curses.nocbreak()
    #stdscr.keypad(False)
    #curses.echo()