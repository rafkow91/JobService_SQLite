from hashlib import pbkdf2_hmac
from os import system
import sys

from tabulate import tabulate

from config import PASSWORD_SALT


def hash_password(password):
    hashed_password = pbkdf2_hmac(
        'sha256',
        password.encode('utf8'),
        PASSWORD_SALT.encode('utf8'),
        999
    )
    return hashed_password.hex()


def clear_screen():
    os_system = sys.platform
    if os_system == 'win32':
        return system('cls')
    return system('clear')


def print_table(table: list[list | tuple]):
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
