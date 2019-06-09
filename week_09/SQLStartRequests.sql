DROP TABLE IF EXISTS langauges;

CREATE TABLE langauges (
    id INTEGER,
    language VARCHAR(255),
    answer VARCHAR(255),
    answered INTEGER,
    guide VARCHAR(255)
);


INSERT INTO langauges (id,language,answer,answered,guide)
VALUES 	(1 	,"Python" ,"google" ,0 ,"A folder named Python was created. Go there and fight with program.py!");

INSERT INTO langauges (id,language,answer,answered,guide)
VALUES 	(2 ,"Go" ,	"200 OK ",	0 	,"A folder named Go was created. Go there and try to make Google Go run.");

INSERT INTO langauges (id,language,answer,answered,guide)
VALUES 	(3 	,"Java" 	,"object oriented programming" 	,0 	,"A folder named Java was created. Can you handle the class?");

INSERT INTO langauges (id,language,answer,answered,guide)
VALUES 	(4 	,"Haskell" 	,"Lambda" 	,0 	,"Something pure has landed. Go to Haskell folder and see it!");

INSERT INTO langauges (id,language,answer,answered,guide)
VALUES 	(5 ,	"C#" 	,"NDI=" ,	0 	,"Do you see sharp? Go to the C# folder and check out.");

INSERT INTO langauges (id,language,answer,answered,guide)
VALUES 	(6 	"Ruby" 	,"https://www.ruby-lang.org/bg/" 	,0 	,"Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!");

	
ALTER TABLE langauges
    ADD COLUMN rating INTEGER check (rating between 1 and 9);

UPDATE langauges
SET rating = 8
WHERE language = "Python";

UPDATE langauges
SET rating = 5
WHERE language = "Go";

UPDATE langauges
SET rating = 7
WHERE language = "Java";

UPDATE langauges
SET rating = 7
WHERE language = "Haskell";

UPDATE langauges
SET rating = 4
WHERE language = "C#";

UPDATE langauges
SET rating = 4
WHERE language = "Ruby";

UPDATE langauges
SET answered = 1
WHERE language = "Python" or language="Go";


SELECT language
FROM langauges
WHERE answer="200 OK" OR answer="Lambda"

