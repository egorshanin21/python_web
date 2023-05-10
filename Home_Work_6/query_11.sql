SELECT AVG(grades.grade) AS average_grade
FROM grades
JOIN disciplines ON disciplines.id = grades.discipline_id
JOIN teachers ON teachers.id = disciplines.teacher_id
WHERE grades.student_id = 6
AND teachers.id = 1;