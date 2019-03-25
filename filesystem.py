"""
Case #4 - Working with file system
Grigorev A., Batenev P., Zhambaeva D.
"""

import rulocal as ru
import os


def accept_command():
    """ Asks a command number. """
    # Эксепшоны прописать.
    command = input(ru.CHOOSE+'\n')
    return command


def run_command(command):
    """ Runs a command by number. """
    # TODO


def list_dir():
    """ Files and dir-s in current dir. """
    return os.listdir(os.getcwd())


def move_up():
    """ Go to parent directory. """
    # TODO


def move_down():
    """ Go to input directory. """
    # TODO


def count_files(path):
    """ """
    # TODO


def count_bytes(path):
    """ """
    # TODO


def find_files(target, path):
    """ """
    # TODO


def main():
    """ Main function. """
    while True:
        print(os.getcwd())
        print(ru.MENU)
        command = accept_command()
        if command == 7:
            break
        run_command(command)

    print(ru.BYE)


if __name__ == '__main__':
    main()
