"""
Case #4 - Working with file system
Grigorev A., Batenev P., Zhambaeva D.
"""

import rulocal as ru
import os
import os.path

direct = os.getcwd()
name = os.listdir(direct)
file = []


def accept_command():
    """ Asks a command number. """
    command = int(input(ru.CHOOSE+'\n'))
    try:
        command = int(command)
    except:
        print(ru.WRONG)
    if command < 7:
        return command
    else:
        print(ru.WRONG)


def run_command(command):
    """ Runs a command by number. """
    command = int(command)
    if command == 1:
        print(list_dir())
    elif command == 2:
        move_up()
    elif command == 3:
        move_down()
    elif command == 4:
        print(count_files_input())
    elif command == 5:
        print(count_bytes_input())
    elif command == 6:
        print(find_files_input())
    else:
        print(ru.NOT_FOUND)


def list_dir():
    """ Files and dir-s in current dir. """
    return os.listdir(os.getcwd())


def move_up():
    """ Go to parent directory. """
    my_path = 'C:WINDOWSsystem32'
    catalog = os.path.basename(os.path.dirname(my_path))
    return catalog


def move_down():
    """ Go to input directory. """
    needed_dir = input(ru.PATH)
    try:
        dir = os.getcwd()
        new_dir = dir + '\\' + needed_dir
        os.chdir(new_dir)
        return os.getcwd()
    except FileNotFoundError:
        return print(ru.INPUT_ERROR)


def count_files_input():
    """ Addition to count_files. """
    return count_files(input(ru.COUNT_INPUT1))


def count_files(path):

    count = 0
    if not os.path.exists(path):
        return
    files = os.listdir(path)
    print(files)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            count += 1
        else:
            count_files(file_path)


def count_bytes_input():
    """ Addition to count_bytes. """
    return count_bytes(input(ru.COUNT_INPUT2))


def count_bytes(path):
    """ """
    # TODO


def find_files_input():
    """ Addition to count_bytes. """
    target = input(ru.WHAT_FIND)
    path = input(ru.WHERE_FIND)
    return find_files(target, path)


def find_files(target, path):
    lst = []
    for root, dirs, files in os.walk(path):
        for item in files:
            i = os.path.join(root, item)
            if target in i:
                lst.append(i)
    if len(lst) == 0:
        return print(ru.INPUT_ERROR)
    return lst


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
