from colorama import *


def brown(text):
    return '\033[33m' + text + '\033[0m'


def light_blue(text):
    return Fore.LIGHTBLUE_EX + text + Fore.RESET


def pink(text):
    return Fore.LIGHTMAGENTA_EX + text + Fore.RESET


def orange(text):
    return Fore.RED + text + Fore.RESET


def red(text):
    return Fore.LIGHTRED_EX + text + Fore.RESET


def yellow(text):
    return Fore.LIGHTYELLOW_EX + text + Fore.RESET


def green(text):
    return Fore.LIGHTGREEN_EX + text + Fore.RESET


def dark_blue(text):
    return Fore.BLUE + text + Fore.RESET


def blank(text):
    return text


if __name__ == "__main__":
    print(brown("This is brown text"))
    print(light_blue("This is light blue text"))
    print(pink("This is pink text"))
    print(orange("This is orange text"))
    print(red("This is red text"))
    print(yellow("This is yellow text"))
    print(green("This is green text"))
    print(dark_blue("This is dark blue text"))
    print(blank("This is blank text"))
