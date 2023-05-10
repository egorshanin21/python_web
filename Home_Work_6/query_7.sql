SELECT students.fullname, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN disciplines ON grades.discipline_id = disciplines.id
JOIN `groups` ON students.group_id = `groups`.id
WHERE `groups`.name = 'TE-0604' AND disciplines.name = 'Programming'
ORDER BY fullname;