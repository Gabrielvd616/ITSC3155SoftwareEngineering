SELECT instructor.instructor_id, instructor.first_name, instructor.last_name
FROM instructor
LEFT OUTER JOIN student ON instructor.instructor_id = student.advisor_id
WHERE student.advisor_id IS NULL;