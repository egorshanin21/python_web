from pprint import pprint

from sqlalchemy import func, desc, select, and_

from src.models import Teacher, Student, Discipline,Grade,Group
from src.db import session


def select_1():
    result = session.query(Student.fullname,
                           func.round(func.avg(Grade.grade), 2).label(
                               'avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(
        desc('avg_grade')).limit(5).all()
    return result


def select_2(discipline_id: int):

    result = session.query(Discipline.name, Student.fullname,
                           func.round(func.avg(Grade.grade), 2).
                           label('avg_grade')) \
        .select_from(Grade).join(Student).join(Discipline).\
        filter(Discipline.id == discipline_id) \
        .group_by(Student.id, Discipline.name).order_by(desc('avg_grade')).\
        limit(1).all()
    return result


def select_3(discipline_id):
    result = session.query(Discipline.name, Group.name,
                           func.round(func.avg(Grade.grade), 2).
                           label('average_grade')) \
                    .select_from(Grade).join(Student,
                                             Student.id == Grade.student_id) \
                   .join(Discipline, Discipline.id == Grade.discipline_id) \
                   .join(Group, Group.id == Student.group_id) \
                   .filter(Discipline.id == discipline_id) \
                    .group_by(Discipline.name, Group.name) \
                    .order_by(desc('average_grade')).all()
    return result


def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2).
                           label('average_grade')).scalar()
    return result


def select_5(teacher_fullname):
    result = session.query(Discipline.name).\
        join(Teacher, Discipline.teacher_id == Teacher.id).\
        filter(
        Teacher.fullname == teacher_fullname).all()
    return result


def select_6(group_name):
    result = session.query(Student.fullname).\
        join(Group, Student.group_id == Group.id).filter(
        Group.name == group_name).order_by(Student.fullname).all()
    return result


def select_7(group_name, discipline_name):
    result = session.query(Student.fullname, Grade.grade).\
        join(Grade, Student.id == Grade.student_id) \
        .join(Discipline, Grade.discipline_id == Discipline.id) \
        .join(Group, Student.group_id == Group.id) \
        .filter(Group.name == group_name, Discipline.name == discipline_name) \
        .order_by(Student.fullname).all()
    return result


def select_8(teacher_fullname):
    result = session.query(Teacher.fullname, Discipline.name,
                           func.round(func.avg(Grade.grade), 2).
                           label('avg_grade')) \
        .join(Discipline, Teacher.id == Discipline.teacher_id) \
        .join(Grade, Discipline.id == Grade.discipline_id) \
        .group_by(Teacher.fullname, Discipline.name) \
        .having(Teacher.fullname == teacher_fullname).all()
    return result


def select_9(student_fullname):
    result = session.query(Student.fullname, Discipline.name).distinct() \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Discipline, Grade.discipline_id == Discipline.id) \
        .filter(Student.fullname == student_fullname).all()
    return result


def select_10(student_fullname, teacher_fullname):
    result = session.query(Discipline.name).distinct().\
        join(Grade, Grade.discipline_id == Discipline.id) \
        .join(Student, Student.id == Grade.student_id).\
        join(Teacher, Teacher.id == Discipline.teacher_id) \
        .filter(Student.fullname == student_fullname,
                Teacher.fullname == teacher_fullname).all()
    return result


def select_11(student_id, teacher_id):
    result = session.query(func.round(func.avg(Grade.grade), 2).
                           label('average_grade')) \
        .join(Discipline, Discipline.id == Grade.discipline_id) \
        .join(Teacher, Teacher.id == Discipline.teacher_id) \
        .filter(Grade.student_id == student_id,
                Teacher.id == teacher_id).scalar()
    return result


def select_12(discipline_id, group_id):
    subquery = (select(Grade.date_of).join(Student).join(Group).where(
        and_(Grade.discipline_id == discipline_id, Group.id == group_id)
    ).order_by(desc(Grade.date_of)).limit(1).scalar_subquery())

    result = session.query(Discipline.name, Student.fullname, Group.name,
                           Grade.date_of, Grade.grade) \
        .select_from(Grade).join(Student).join(Discipline).join(Group) \
        .filter(and_(Discipline.id == discipline_id, Group.id == group_id,
                     Grade.date_of == subquery)) \
        .order_by(desc(Grade.date_of)).all()
    return result


if __name__ == '__main__':
    pprint(select_1())
    pprint(select_2(1))
    pprint(select_3(2))
    pprint(select_4())
    pprint(select_5('Robert Wilson'))
    pprint(select_6('TE-0604'))
    pprint(select_7('TE-0604', 'Programming'))
    pprint(select_8('Robert Wilson'))
    pprint(select_9('Diana Rice'))
    pprint(select_10('Diana Rice', 'Robert Wilson'))
    pprint(select_11(12, 3))
    pprint(select_12(7, 1))

