from datetime import date, time

from repositories.base_repositories import BaseRepository


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

