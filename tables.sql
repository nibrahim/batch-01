CREATE TABLE artist (
       id INTEGER PRIMARY KEY,
       shortname VARCHAR(10),
       fullname VARCHAR(80),
       lang VARCHAR(15)
);

INSERT INTO artist(id, fullname, shortname, lang) VALUES (1, 'Xavier', 'X', 'English');
INSERT INTO artist(id, fullname, shortname, lang) VALUES (2, 'Xerox', 'X', 'English');
INSERT INTO artist(id, fullname, shortname, lang) VALUES (3, 'Xavier', 'xav', 'English');
INSERT INTO artist(id, fullname, shortname, lang) VALUES (4, 'Joe Satriani', 'satch', 'Instrumental');



SELECT shortname, fullname from artist;
SELECT shortname, fullname from artist limit 2;
SELECT shortname, fullname from artist order by fullname;
SELECT shortname, fullname from artist order by fullname DESC;


SELECT * from artist WHERE shortname='satch' OR shortname='xav';
SELECT * from artist WHERE fullname LIKE 'X%';

UPDATE artist SET shortname='parc' WHERE id=2;
DELETE from artist where id=1;

-- fdsfsd
CREATE TABLE song (
       id INTEGER PRIMARY KEY,  
       artist INTEGER references artist(id),
       name VARCHAR(100),
       year integer,
       lyrics TEXT
);

INSERT INTO song(id, artist, name, year, lyrics) VALUES (1, 3, 'Example 1', 1990, 'This is an example song');
INSERT INTO song(id, artist, name, year, lyrics) VALUES (2, 3, 'Example 2', 1990, 'This is the second example song');
INSERT INTO song(id, artist, name, year, lyrics) VALUES (3, 2, 'Sample 1', 1995, 'This is the sample song');
INSERT INTO song(id, artist, name, year, lyrics) VALUES (4, 2, 'Sample 2', 2000, 'This is the second sample song');

INSERT INTO song(id, artist, name, year, lyrics) VALUES (5, 4, 'Summer Song', 1993, '');
INSERT INTO song(id, artist, name, year, lyrics) VALUES (6, 4, 'Crystal Planet', 2002, '');

INSERT INTO song(id, artist, name, year, lyrics) VALUES (7, 1, 'Something', 2002, '');


SELECT name FROM song WHERE year > 1997;
SELECT name from song where year < 2005 and year > 1990;
SELECT a.lang, s.name FROM artist a, song s WHERE s.artist = a.id; -- Names and languages of all songs
SELECT q.language from (SELECT a.lang AS Language, s.name as Title FROM artist a, song s WHERE s.artist = a.id) as q;
SELECT s.name, s.year, s.lyrics from artist a, song s WHERE s.artist = a.id and a.fullname = 'Joe Satriani'; -- All songs by Joe Satriani
