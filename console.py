#!/usr/bin/python3
""" Console  """

class HBNBCommand(cmd.Cmd):
    """Quit command"""
    def do_quit(self, arg):
        return True
    
    """End the command line"""
    def do_EOF(self, arg):
        return True
    
    """ Prints the help documentation """
    def help_EOF(self):
        print("Exit the program\n")

    """ emptyline method of """
    def emptyline(self):
        pass

    """ the help documentation for quit """
    def help_quit(self):
        print("Quit the program\n")
