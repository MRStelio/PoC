import os
import mysql.connector
from dotenv import load_dotenv


class DatabaseConnector:

    def __init__(self):
        """Соединение с БД."""

        load_dotenv()
        self.db = mysql.connector.connect(
          host=os.getenv('DB_HOST'),
          user=os.getenv("DB_USER"),
          password=os.getenv("DB_PASSWORD"),
          database=os.getenv("DB_USED"),
          port=os.getenv("DB_PORT")
        )
        self.cursor = self.db.cursor()

    def insert_data(self, value):
        """Записать тестовые данные в тестовую БД."""

        sql = "INSERT INTO testdata (id, testdata) VALUES (%s, %s)"
        val = (None, value)
        self.cursor.execute(sql, val)
        self.db.commit()
        self.db.close()

    def select_testdata_by_id(self, id_testdata=None):
        """Выбрать тестовые данные по id записи в БД.
        Если не передавать id, берется последняя запись в таблице.
        """

        query_result = None
        if id_testdata is None:
            self.cursor.execute("SELECT id, testdata FROM testdata ORDER BY id DESC LIMIT 1")
            for id, testdata in self.cursor:
                query_result = testdata

        else:
            self.cursor.execute(f"SELECT id, testdata FROM testdata WHERE id={id_testdata}")
            for id, testdata in self.cursor:
                query_result = testdata

        self.db.close()
        return query_result
