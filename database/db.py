from sqlite3 import *
import sqlite3

def get_connection():
    connection = sqlite3.connect('./database/job_service.db')
    cursor = connection.cursor()

    return cursor
