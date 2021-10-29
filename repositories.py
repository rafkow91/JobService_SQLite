#
from datetime import date, time
from sqlite3 import connect


DB_URL = './database/job_service.db'


class WorktimeRepository:
    def __init__(self, employee_id: int) -> None:
        self.employee_id = employee_id

    def add_workday(self, worktime_date: date):
        connection = connect(DB_URL)
        cursor = connection.cursor()
        cursor.execute(
            '''
                INSERT INTO worktime (`employee_id`, `workday`)
                VALUES (?, ?)
            ''',
            (self.employee_id, worktime_date)
        )

        connection.commit()

    def get_workday(self, worktime_date: date):
        connection = connect(DB_URL)
        cursor = connection.cursor()
        cursor.execute(
            '''
                SELECT *
                FROM worktime
                WHERE `employee_id` = ? AND `workday` = ?
            ''',
            (self.employee_id, worktime_date)
        )

        return cursor.fetchone()

    def add_start_time(self, worktime_date: date, time: time):
        connection = connect(DB_URL)
        cursor = connection.cursor()
        cursor.execute(
            '''
                UPDATE worktime
                SET `start_time` = ?
                WHERE `employee_id` = ? AND `workday` = ?
            ''',
            (time, self.employee_id, worktime_date)
        )

        connection.commit()

    def get_start_time(self, worktime_date: date):
        connection = connect(DB_URL)
        cursor = connection.cursor()
        cursor.execute(
            '''
                SELECT start_time
                FROM worktime
                WHERE `employee_id` = ? AND `workday` = ?
            ''',
            (self.employee_id, worktime_date)
        )

        return cursor.fetchone()

    def add_end_time(self, worktime_date: date, time: time):
        connection = connect(DB_URL)
        cursor = connection.cursor()
        cursor.execute(
            '''
                UPDATE worktime
                SET `end_time` = ?
                WHERE `employee_id` = ? AND `workday` = ?
            ''',
            (time, self.employee_id, worktime_date)
        )

        connection.commit()

    def get_end_time(self, worktime_date: date):
        connection = connect(DB_URL)
        cursor = connection.cursor()
        cursor.execute(
            '''
                SELECT end_time
                FROM worktime
                WHERE `employee_id` = ? AND `workday` = ?
            ''',
            (self.employee_id, worktime_date)
        )

        return cursor.fetchone()
