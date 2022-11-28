from datetime import date, datetime, time
from sqlite3 import connect

from config import DB_PATH


class BaseRepository:
    def __init__(self) -> None:
        
        self.connection = connect(DB_PATH)
        self.cursor = self.connection.cursor()


class LoginRepository(BaseRepository):
    def get_data(self, login: str):
        self.cursor.execute(
            '''
                SELECT
                e.password, 
                t.group_id,
                e.id 
            FROM employees e
            left JOIN titles t ON t.id = e.title_id 
            WHERE login like ? 
            ''',
            (login.lower(),)
        )

        return self.cursor.fetchone()


class WorktimeRepository(BaseRepository):
    def __init__(self, employee_id: int) -> None:
        super().__init__()
        self.employee_id = employee_id

    def add_workday(self, worktime_date: date):
        self.cursor.execute(
            '''
                INSERT INTO worktime (`employee_id`, `workday`)
                VALUES (?, ?)
            ''',
            (self.employee_id, worktime_date)
        )

        self.connection.commit()

    def get_workday(self, worktime_date: str):
        self.cursor.execute(
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

        return self.cursor.fetchone()

    def get_month(self, year: int, month: int):
        str_month = '0' + str(month) if month < 10 else str(month)

        start_date = str(year) + '-' + str_month + '-01'
        end_date = str(year) + '-' + str_month + '-31'

        self.cursor.execute(
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

        return self.cursor.fetchall()

    def add_start_time(self, worktime_date: date, time: time):
        self.cursor.execute(
            '''
                UPDATE worktime
                SET `start_time` = ?
                WHERE `employee_id` = ? AND `workday` = ?
            ''',
            (time, self.employee_id, worktime_date)
        )

        self.connection.commit()

    def get_start_time(self, worktime_date: date):
        self.cursor.execute(
            '''
                SELECT start_time
                FROM worktime
                WHERE `employee_id` = ? AND `workday` = ?
            ''',
            (self.employee_id, worktime_date)
        )

        return self.cursor.fetchone()

    def add_end_time(self, worktime_date: date, time: time):
        self.cursor.execute(
            '''
                UPDATE worktime
                SET `end_time` = ?
                WHERE `employee_id` = ? AND `workday` = ?
            ''',
            (time, self.employee_id, worktime_date)
        )

        self.connection.commit()

    def get_end_time(self, worktime_date: date):
        self.cursor.execute(
            '''
                SELECT end_time
                FROM worktime
                WHERE `employee_id` = ? AND `workday` = ?
            ''',
            (self.employee_id, worktime_date)
        )

        return self.cursor.fetchone()

# TODO: do zmiany na tabele!! i coś tu nie działa
    @staticmethod
    def print_worktime(fetch: list):
        print('\n\nData\t\tWejście\t\tWyjście\t\tIlość przepracowanych godzin')
        for item in fetch:
            item = list(item)
            try:
                item.append(round((datetime.strptime(item[2], "%H:%M:%S") - datetime.strptime(item[1], "%H:%M:%S")).total_seconds() / 3600, 2))
            except TypeError:
                item.append('-' * 8)
            print(item)
            # print(
            #     f'{item[0]}\t{item[1]}\t{"-" * 8 if item[2] is None else item[2]}\t{"-" * 8 if (item[1] or item[2]) is None else round((datetime.strptime(item[2], "%H:%M:%S") - datetime.strptime(item[1], "%H:%M:%S")).total_seconds() / 3600, 2)}')
        input('\n\n-- Wciśnij dowolny klawisz aby wrócić do menu --\n')


class EmployeeRepository(BaseRepository):
    def add_new_employee(self, person: dict):
        self.cursor.execute(
            '''
                INSERT INTO employees (`first_name`, `last_name`, `title_id`, `mail`, `phone`, `login`, `password`)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''',
            (person['first_name'], person['last_name'], person['title_id'],
             person['mail'], person['phone'], person['login'], person['password'])
        )

        self.connection.commit()


class TitleRepository(BaseRepository):
    def get_title_id_by_title(self, title: str):
        self.cursor.execute(
            '''
                SELECT id
                FROM titles
                WHERE title_name like ?
            ''',
            (title, )
        )

        return self.cursor.fetchone()

    def get_titles_list(self):
        self.cursor.execute(
            '''
                SELECT title_name 
                FROM titles
            '''
        )

        return self.cursor.fetchall()

    def add_new_title(self, title: dict):
        self.cursor.execute(
            '''
                INSERT INTO titles (`title_name`, `basic_salary`, `group_id`)
                VALUES (?, ?, ?)
            ''',
            (title['name'], title['salary'], title['group_id'])
        )

        self.connection.commit()
