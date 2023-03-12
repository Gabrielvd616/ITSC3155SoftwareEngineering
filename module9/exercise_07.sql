SELECT course.course_code, instructor.first_name, instructor.last_name, course.num_credits
FROM course, instructor
WHERE instructor.instructor_id = course.instructor_id AND course.course_id IN (
    SELECT course_id FROM student_schedule WHERE student_id = 1
);