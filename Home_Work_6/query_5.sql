SELECT disciplines.name
FROM disciplines
JOIN teachers
ON disciplines.teacher_id = teachers.id
WHERE teachers.fullname = 'Roger Hunt';