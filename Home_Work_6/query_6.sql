SELECT students.fullname
FROM students
JOIN `groups`
ON students.group_id = `groups`.id
WHERE `groups`.name = 'TE-0604'
ORDER BY fullname;