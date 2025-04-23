import os


def clear_console(current_os):
    if current_os == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
