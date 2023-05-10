import pymysql
from contextlib import contextmanager


@contextmanager
def create_connection():
    conn = None
    try:
        conn = pymysql.connect(host="localhost", database='students', user='root', password='kir090890')
        yield conn
        conn.commit()
    except pymysql.Error as error:
        conn.rollback()
        print(error)
    finally:
        if conn is not None:
            conn.close()