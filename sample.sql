CREATE TABLE students (   -- Create table students with 
       roll SERIAL PRIMARY KEY, -- The following fields
       fname VARCHAR(50),
       lname VARCHAR(50),
       address TEXT
);

INSERT INTO students (roll, fname, lname, address) VALUES (1, 'Noufal', 'Ibrahim', 'Kozhikode'); -- Inserts one row into the table
INSERT INTO students (roll, fname, lname, address) VALUES (2, 'Manjusha', 'Isac', 'Wayanad'); -- Inserts one row into the table


SELECT fname, lname FROM students;
SELECT * FROM students;
SELECT * FROM students WHERE roll=2 AND fname='Noufal';

DELETE from students WHERE roll=2;

DROP TABLE students;



