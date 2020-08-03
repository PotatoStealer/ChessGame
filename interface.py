import curses

class ConsoleInterface:

    def __init__(self):
        pass

    def set_board(self, inputstr):
        """
        Takes board info as an input string and prints it to the console
        """
        print(inputstr)

    def set_msg(self, inputstr):
        """
        Takes an inputstr and prints it to the console
        """
        print(inputstr)

    def get_player_input(self, msgstr):
        """
        Prints a msgstr and prompt player fpr input and retrive as a string
        """
        value = input(msgstr)
        return value

class TextInterface:
    def __init__(self):
        stdscr = curses.initscr()
        self.win1 = curses.newwin(10, 20, 0, 0)
        self.win2 = curses.newwin(12, 20, 12, 0)
        self.win3 = curses.newwin(2, 100, 10, 0)

    def set_board(self, inputstr):
        """
        Takes board info as an input string and prints it to the console using text interface
        """
        self.win1.addstr(0, 0, inputstr)
        self.win1.refresh()

    def set_msg(self, inputstr):
        """
        Takes an inputstr and prints it to the console using text interface
        """
        self.win3.addstr(0, 0, inputstr)
        self.win3.refresh()
        
    def get_player_input(self, msgstr):
        """
        Prints a msgstr and prompt player fpr input and retrive as a string
        """
        self.win2.addstr(0, 0, msgstr)
        self.win2.refresh()
        value = self.win2.getstr().decode('utf-8')
        self.win2.erase()
        self.win3.erase()
        return value
    
