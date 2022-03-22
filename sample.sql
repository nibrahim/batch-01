CREATE TABLE students (   -- Create table students with 
       roll SERIAL PRIMARY KEY, -- The following fields
       fname VARCHAR(50),
       lname VARCHAR(50),
       address TEXT
);

CREATE TABLE pnumber (
       id SERIAL PRIMARY KEY,
       student INTEGER UNIQUE references students(roll),
       number VARCHAR(10)
       );

CREATE TABLE subjects (
       id SERIAL PRIMARY KEY,
       name VARCHAR(10)
       );

CREATE TABLE enrollments (
       student INTEGER references students (roll),
       subject INTEGER references subjects (id)
       )

       
-- Insert some students
INSERT INTO students (roll, fname, lname, address) VALUES ('Noufal', 'Ibrahim', 'Kozhikode');
-- Repeat above statement 11 times

INSERT into subjects(name) VALUES ('maths');
INSERT into subjects(name) VALUES ('geography');
INSERT into subjects(name) VALUES ('history');
INSERT into subjects(name) VALUES ('science');

-- Insert some phone numbers
INSERT INTO pnumber (student, number) VALUES (7, '+91987655');
INSERT INTO pnumber (student, number) VALUES (8, '+412345432');

-- Connect to subjects
INSERT INTO enrollments (student, subject) VALUES (3, 2);
INSERT INTO enrollments (student, subject) VALUES (3, 3);
INSERT INTO enrollments (student, subject) VALUES (3, 4);
INSERT INTO enrollments (student, subject) VALUES (4, 1);
INSERT INTO enrollments (student, subject) VALUES (4, 2);
INSERT INTO enrollments (student, subject) VALUES (4, 3);

-- Queries
SELECT fname, lname FROM students;
SELECT * FROM students;
SELECT * FROM students WHERE roll=2 AND fname='Noufal';

DELETE from students WHERE roll=2;

DROP TABLE students;





-- 1 to 1
-- Many to 1
-- 1 to Many

-- Many to Many
select s1.roll, s1.fname, s1.lname from students s1, enrollments e, subjects s2 WHERE e.student = s1.roll AND e.subject = s2.id and s2.name = 'geography'; -- All students enrolled for Geography
select s1.roll, s2.name from students s1, enrollments e, subjects s2 WHERE e.student = s1.roll AND e.subject = s2.id and s1.roll = 3; -- All subjects of Roll number 3








