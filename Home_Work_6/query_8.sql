SELECT teachers.fullname, disciplines.name, AVG(grades.grade) AS avg_grade
FROM teachers
JOIN disciplines ON teachers.id = disciplines.teacher_id
JOIN grades ON disciplines.id = grades.discipline_id
GROUP BY teachers.fullname, disciplines.name
HAVING teachers.fullname = 'Roger Hunt';