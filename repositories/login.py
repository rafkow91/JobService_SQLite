from repositories.base_repositories import BaseRepository

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
