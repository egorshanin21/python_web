SELECT MAX(date_of) AS date_of
FROM grades
JOIN disciplines ON disciplines.id = grades.discipline_id
WHERE disciplines.name = 'Programming';

SELECT grades.id
FROM grades
JOIN disciplines ON disciplines.id = grades.discipline_id
WHERE disciplines.name = 'Programming'
AND date_of = (SELECT MAX(date_of) FROM grades WHERE discipline_id = disciplines.id);


SELECT students.fullname, grades.grade
FROM grades
JOIN students ON students.id = grades.student_id
JOIN `groups` ON `groups`.id = students.group_id
JOIN disciplines ON disciplines.id = grades.discipline_id
WHERE disciplines.name = 'Programming'
AND `groups`.name = 'TE-0604'
AND grades.date_of = (
  SELECT MAX(date_of)
  FROM grades
  JOIN disciplines ON disciplines.id = grades.discipline_id
  WHERE disciplines.name = 'Programming'
);
