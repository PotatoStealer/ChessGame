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
    
