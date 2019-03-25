"""
Case #4 - Working with file system
Grigorev A., Batenev P., Zhambaeva D.
"""

import rulocal as ru
import os
import os.path

def accept_command():
    """ Asks a command number. """
    # Эксепшоны прописать.
    command = int(input(ru.CHOOSE+'\n'))
    if command < 7:
        print('Команда введена  корректно, продолжаем работать')

    else:
        print('Команда введена не корректно, проверьте ввод команды и попробуйте еще раз:')
        command = int(input(ru.CHOOSE + '\n'))
    return command


def run_command(command):
    """ Runs a command by number. """
    # TODO


def list_dir():
    """ Files and dir-s in current dir. """
    return os.listdir(os.getcwd())


def move_up():
    """ Go to parent directory. """
    my_path = 'C:WINDOWSsystem32'
    catalog = os.path.basename(os.path.dirname(my_path))
    return catalog


def move_down(current_dir):
    """ Go to input directory. """
    try:
        dir = os.getcwd()
        new_dir = dir + '\\' + current_dir
        os.chdir(new_dir)
        return os.getcwd()
    except FileNotFoundError:
        return print(ru.INPUT_ERROR)


def count_files(path):

    count = 0
    if not os.exists(path):
        return
    files = os.listdir(path)
    print(files)
    for file in files:
        file_path = os.join(path, file)
        if os.isfile(file_path):
            count += 1
        else:
            count_files(file_path)


def count_bytes(path):
    """ """
    # TODO


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
