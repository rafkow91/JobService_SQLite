from hashlib import pbkdf2_hmac
from os import system
import sys

from my_secret_file import salt


def hash_password(password):
    hashed_password = pbkdf2_hmac(
        'sha256',
        password.encode('utf8'),
        salt.encode('utf8'),
        999
    )
    return hashed_password.hex()

def clear_screen():
    os_system = sys.platform
    if os_system == 'win32':
        return system('cls')
    return system('clear')
