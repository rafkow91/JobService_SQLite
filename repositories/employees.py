from repositories.base_repositories import BaseRepository


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

    def index(self) -> list[tuple]:
        self.cursor.execute(
            '''
                SELECT
                    e.id,
                    e.first_name, 
                    e.last_name,
                    e.mail,
                    t.title_name
                FROM employees e
                left JOIN titles t ON t.id = e.title_id 
            '''
        )

        return self.cursor.fetchall()

    def get_employee_by_id(self, employee_id: int) -> list[tuple]:
        self.cursor.execute(
            '''
                SELECT
                    e.first_name, 
                    e.last_name,
                    t.title_name,
                    e.phone,
                    e.mail,
                    e.login
                FROM employees e
                left JOIN titles t ON t.id = e.title_id
                WHERE e.id = ?
            ''', 
            (employee_id, )
        )

        return self.cursor.fetchone()



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
