import pymysql
from datetime import datetime,timedelta, date
from faker import Faker
from random import randint
from pprint import pprint


disciplines = [
    "Higher mathematics",
    "Programming",
    "History of Ukraine",
    "Physics",
    "English",
    "Mechanics",
    "Dynamics"
]

groups = ['TE-0604', 'TY-0601', 'TN-0603']
NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50
fake = Faker()
connect = pymysql.connect(host="localhost", database='students', user='root', password='kir090890')
cursor = connect.cursor()


def seed_teachers():
    teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]
    sql = "INSERT INTO teachers(fullname) VALUES(%s);"
    cursor.executemany(sql, zip(teachers, ))


def seed_disciplines():
    sql = "INSERT INTO disciplines(name, teacher_id) VALUES(%s, %s);"
    cursor.executemany(sql, zip(disciplines, iter(randint(1, NUMBER_TEACHERS) for _ in range(len(disciplines)))))


def seed_groups():
    sql = "INSERT INTO `groups`(name) VALUES(%s);"
    cursor.executemany(sql, zip(groups, ))


def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    sql = "INSERT INTO students(fullname, group_id) VALUES(%s, %s);"
    cursor.executemany(sql, zip(students, iter(randint(1, len(groups)) for _ in range(len(students)))))


def seed_grades():
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-06-25", "%Y-%m-%d")
    sql = "INSERT INTO grades(discipline_id, student_id, grade, date_of) VALUES(%s, %s, %s, %s);"

    def get_list_date(start: date, end: date) -> list[date]:
        result = []
        current_date = start
        while current_date <= end:
            if current_date.isoweekday() < 6:
                result.append(current_date)
            current_date += timedelta(1)
        return result

    list_dates = get_list_date(start_date, end_date)

    grades = []
    for day in list_dates:
        random_discipline = randint(1, len(disciplines))
        random_students = [randint(1, NUMBER_STUDENTS) for _ in range(4)]
        for student in random_students:
            grades.append((random_discipline, student, randint(1, 12), day.date()))
    cursor.executemany(sql, grades)


if __name__ == '__main__':
    try:
        seed_teachers()
        seed_disciplines()
        seed_groups()
        seed_students()
        seed_grades()
        connect.commit()
    except pymysql.Error as error:
        pprint(error)
    finally:
        connect.close()
