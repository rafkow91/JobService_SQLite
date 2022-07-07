from datetime import date, datetime, time
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

    def get_workday(self, worktime_date: str):
        connection = connect(DB_URL)
        cursor = connection.cursor()
        cursor.execute(
            '''
                SELECT 
                    `workday`,
                    `start_time`,
                    `end_time`
                FROM worktime
                WHERE `employee_id` = ? AND `workday` = ?
            ''',
            (self.employee_id, worktime_date)
        )

        return cursor.fetchone()

    def get_month(self, year: int, month: int):
        str_month = '0' + str(month) if month < 10 else str(month)

        start_date = str(year) + '-' + str_month + '-01'
        end_date = str(year) + '-' + str_month + '-31'
        
        connection = connect(DB_URL)
        cursor = connection.cursor()
        cursor.execute(
            '''
                SELECT 
                    `workday`,
                    `start_time`,
                    `end_time`
                FROM worktime
                WHERE `employee_id` = ? AND `workday` BETWEEN ? AND ?
            ''',
            (self.employee_id, start_date, end_date)
        )
                
        return cursor.fetchall()

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

# TODO: do zmiany na tabele!! i coś tu nie działa
    @staticmethod
    def print_worktime(fetch: list):
        print('\n\nData\t\tWejście\t\tWyjście\t\tIlość przepracowanych godzin')
        for item in fetch:
            print(
                f'{item[0]}\t{item[1]}\t{"-" * 8 if item[2] is None else item[2]}\t{"-" * 8 if (item[1] or item[2]) is None else round((datetime.strptime(item[2], "%H:%M:%S") - datetime.strptime(item[1], "%H:%M:%S")).total_seconds() / 3600, 2)}')
        input('\n\n-- Wciśnij dowolny klawisz aby wrócić do menu --\n')


class EmployeeRepository():
    @staticmethod
    def add_new_employee(person: dict):
        connection = connect(DB_URL)
        cursor = connection.cursor()
        cursor.execute(
            '''
                INSERT INTO employees (`first_name`, `last_name`, `title_id`, `mail`, `phone`, `login`, `password`)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''',
            (person['first_name'], person['last_name'], person['title_id'],
             person['mail'], person['phone'], person['login'], person['password'])
        )

        connection.commit()


class TitleRepository():
    @staticmethod
    def get_title_id_by_title(title: str):
        connection = connect(DB_URL)
        cursor = connection.cursor()
        cursor.execute(
            '''
                SELECT id
                FROM titles
                WHERE title_name like ?
            ''',
            (title, )
        )

        return cursor.fetchone()

    @staticmethod
    def add_new_title(title: dict):
        connection = connect(DB_URL)
        cursor = connection.cursor()
        cursor.execute(
            '''
                INSERT INTO titles (`title_name`, `basic_salary`, `group_id`)
                VALUES (?, ?, ?)
            ''',
            (title['name'], title['salary'], title['group_id'])
        )

        connection.commit()
