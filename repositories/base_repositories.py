from sqlite3 import connect

from config import DB_PATH


class BaseRepository:
    def __init__(self) -> None:

        self.connection = connect(DB_PATH)
        self.cursor = self.connection.cursor()
