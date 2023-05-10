SELECT DISTINCT students.fullname, disciplines.name
FROM students
JOIN grades ON students.id = grades.student_id
JOIN disciplines ON grades.discipline_id = disciplines.id
WHERE students.fullname = 'Kimberly Wyatt';