DROP TABLE IF EXISTS MOVIEEXEC;
DROP TABLE  IF EXISTS MOVIE;
DROP TABLE IF EXISTS MOVIESTAR;
DROP TABLE IF EXISTS STARSIN;
DROP TABLE IF EXISTS STUDIO;

CREATE TABLE MOVIEEXEC (
	CERT INTEGER NOT NULL PRIMARY KEY,
	NAME CHAR(30),
	ADDRESS VARCHAR(255),
	NETWORTH INTEGER
);

CREATE TABLE STUDIO (
    NAME CHAR(50) NOT NULL PRIMARY KEY,
    ADDRESS VARCHAR(255),
    PRESC INTEGER
);

CREATE TABLE MOVIE (
	TITLE VARCHAR(255) NOT NULL,
	YEAR INTEGER NOT NULL,
	LENGTH INTEGER,
	INCOLOR CHAR(1),
	STUDIONAME CHAR(50),
	PRODUCER INTEGER,
	PRIMARY KEY( TITLE, YEAR),
	FOREIGN KEY(PRODUCER) REFERENCES MOVIEEXEC(CERT),
	FOREIGN KEY(STUDIONAME) REFERENCES STUDIO(NAME)
);

CREATE TABLE MOVIESTAR (
	NAME CHAR(30) NOT NULL PRIMARY KEY,
	ADDRESS VARCHAR(255),
	GENDER CHAR(1),
	BIRTHDATE DATE
);

CREATE TABLE STARSIN (
	MOVIETITLE VARCHAR(255) NOT NULL,
	MOVIEYEAR INTEGER NOT NULL,
	STARNAME CHAR(30) NOT NULL,
	FOREIGN KEY(MOVIETITLE) REFERENCES MOVIE(TITLE),
	FOREIGN KEY(STARNAME) REFERENCES MOVIESTAR(NAME),
	PRIMARY KEY(MOVIETITLE, MOVIEYEAR, STARNAME)
);

----- Constraints -----
INSERT INTO STUDIO (NAME, ADDRESS, PRESC)
  VALUES ('Disney','USA, 234534 CF, World',4);

  INSERT INTO STUDIO (NAME, ADDRESS, PRESC)
  VALUES ('Fox','USA, 234576 CF, Fox Str',3);

  INSERT INTO STUDIO (NAME, ADDRESS, PRESC)
  VALUES ('MGM','USA, 127823 NY, 8th Str',1);

  INSERT INTO STUDIO (NAME, ADDRESS, PRESC)
  VALUES ('Paramount','USA, 986745 CF, Para Str',1);

  INSERT INTO STUDIO (NAME, ADDRESS, PRESC)
  VALUES ('USA Entertainm.','USA, 213243 CF, Uni Str',3);

INSERT INTO STUDIO (NAME, ADDRESS, PRESC)
VALUES ('Warner Bros','USA, 324235 NY, Bacon Str',2);

INSERT INTO MOVIEEXEC (NAME, ADDRESS, CERT, NETWORTH)
 VALUES ('George Lucas', 'Oak Rd.', 555, 200000000);

INSERT INTO MOVIEEXEC (NAME, ADDRESS, CERT, NETWORTH)
 VALUES ('Ted Turner', 'Turner Av.', 333, 125000000);

INSERT INTO MOVIEEXEC (NAME, ADDRESS, CERT, NETWORTH)
 VALUES ('Stephen Spielberg', '123 ET road', 222, 100000000);

INSERT INTO MOVIEEXEC (NAME, ADDRESS, CERT, NETWORTH)
 VALUES ('Merv Griffin', 'Riot Rd.', 199, 112000000);

INSERT INTO MOVIEEXEC (NAME, ADDRESS, CERT, NETWORTH)
 VALUES ('Calvin Coolidge', 'Fast Lane', 123, 20000000);

INSERT INTO MOVIESTAR
 VALUES ('Jane Fonda', 'Turner Av.', 'F', '1977-07-07');

INSERT INTO MOVIESTAR
 VALUES ('Alec Baldwin', 'Baldwin Av.', 'M', '1977-07-06');

INSERT INTO MOVIESTAR
 VALUES ('Kim Basinger', 'Baldwin Av.', 'F', '1979-07-05');

INSERT INTO MOVIESTAR
 VALUES ('Harrison Ford', 'Prefect Rd.', 'M', '1955-05-05');

INSERT INTO MOVIESTAR
 VALUES ('Debra Winger', 'A way', 'F', '1978-06-05');

INSERT INTO MOVIESTAR
 VALUES ('Jack Nicholson', 'X path', 'M', '1949-05-05');

INSERT INTO MOVIE
 VALUES ('Pretty Woman', 1990, 119, 'y', 'Disney', 199);

INSERT INTO MOVIE
 VALUES ('The Man Who Wasn''t There', 2001, 116, 'N', 'USA Entertainm.',
   555);

INSERT INTO MOVIE
 VALUES ('Logan''s run', 1976, NULL, 'Y', 'Fox', 333);

INSERT INTO MOVIE
 VALUES ('Star Wars', 1977, 124, 'Y', 'Fox', 555);

INSERT INTO MOVIE
 VALUES ('Empire Strikes Back', 1980, 111, 'Y', 'Fox', 555);

INSERT INTO MOVIE
 VALUES ('Star Trek', 1979, 132, 'Y', 'Paramount', 222);

INSERT INTO MOVIE
 VALUES ('Star Trek: Nemesis', 2002, 116, 'Y', 'Paramount', 123);

INSERT INTO MOVIE
 VALUES ('Terms of Endearment', 1983, 132, 'Y', 'MGM', 123);

INSERT INTO MOVIE
 VALUES ('The Usual Suspects', 1995, 106, 'Y', 'MGM', 199);

INSERT INTO MOVIE
 VALUES ('Gone With the Wind', 1938, 238, 'Y', 'MGM', 123);

INSERT INTO STARSIN
 VALUES ('Star Wars', 1977, 'Kim Basinger');

INSERT INTO STARSIN
 VALUES ('Star Wars', 1977, 'Alec Baldwin');

INSERT INTO STARSIN
 VALUES ('Star Wars', 1977, 'Harrison Ford');

INSERT INTO STARSIN
 VALUES ('Empire Strikes Back', 1980, 'Harrison Ford');

INSERT INTO STARSIN
 VALUES ('The Usual Suspects', 1995, 'Jack Nicholson');

INSERT INTO STARSIN
 VALUES ('Terms of Endearment', 1983, 'Jane Fonda');

INSERT INTO STARSIN
 VALUES ('Terms of Endearment', 1983, 'Jack Nicholson');

