SELECT
    student.first_name AS student_first,
    student.last_name AS student_last,
    instructor.first_name AS instructor_first,
    instructor.last_name AS instructor_last
FROM student
INNER JOIN instructor
    ON student.advisor_id = instructor.instructor_id;