import curses
import sys

scr = curses.initscr()


class SNEK:
    def __init__(self,screen):
        self.screen = screen
        curses.noecho()
        curses.curs_set(0) # set cursor to be invisible 
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        scr.addstr("The program is starting")
        w = curses.newwin(30,30,0,0)
        w.keypad(1)
        w.timeout(0)


    def shutdown(self):
        curses.curs_set(1)
        curses.echo()
        curses.endwin()
        sys.exit(0)

    def run(self):
        while True:
            input = chr(self.screen.getch())

            if input == 'x':
                self.shutdown()

def main_wrapper(main_screen):
    snek = SNEK(main_screen) 
    snek.run()

def main():
    curses.wrapper(main_wrapper)

if __name__ == '__main__':
    main()
