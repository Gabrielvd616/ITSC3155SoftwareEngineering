SELECT instructor.first_name, instructor.last_name, SUM(course.num_credits)
FROM instructor, course
WHERE instructor.instructor_id = course.instructor_id
GROUP BY course.instructor_id;