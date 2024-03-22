USE VideoGamesShops
GO

-- INSERT statements --

-- SHOPS --
INSERT INTO Shops (Name, City, NoOfShops, NoOfClients)
VALUES 
	   ('Game Galaxy', 'Miami', 17, 400),
	   ('PlayStation Paradise', 'Seattle', 12, 550),
	   ('Xbox Haven', 'Dallas', 10, 250),
	   ('Gaming Grotto', 'Denver', 4, 800),
	   ('Tech Emporium', 'Boston', 11, 350),
	   ('Virtual Reality Zone', 'Austin', 8, 600),
	   ('Pixel Playground', 'Atlanta', 10, 180);
		
SELECT * From Shops

-- GENRES --
INSERT INTO GamesGenres (Name, NoOfGames)
VALUES 
       ('Action', 1500),
       ('Adventure', 2330),
       ('Sports', 1500),
       ('Strategy', 2000),
       ('Role-Playing', 1800),
       ('Simulation', 1200),
       ('Racing', 900);

SELECT * FROM GamesGenres;

-- COMPANIES --
INSERT INTO VideoGamesCompany (Name, NoOfEmployees)
VALUES 
       ('Gaming Co.', 200),
       ('TechPlay', 150),
       ('PixelSoft', 100),
       ('GameCraft', 120),
       ('GameTech', 180),
       ('FunPlay', 130),
       ('InfiniteGames', 90);

SELECT * From VideoGamesCompany

-- GAMES --
INSERT INTO Games (Name, Price, Gid, Vid)
VALUES 
	   ('BlockCraft: World Builder', 60, 1, 3),
	   ('GalacticMiner: Space Adventure', 40, 3, 2),
	   ('EpicCraft: Fantasy Realm', 50, 2, 4),
	   ('PixelPlayground: Sports Edition', 80, 4, 1),
	   ('SuperQuest: Epic Adventure', 70, 5, 2),
	   ('SpeedRacer: Turbo Edition', 45, 6, 3),
	   ('CityBuilder: Urban Empire', 55, 7, 1);

SELECT * From Games

-- VIDEO GAMES SHOPS --
INSERT INTO VideoGamesShops (Bid, Sid, StockQuantity, AddingDate)
VALUES 
	   (1, 2, 50, '2023-11-14'), 
	   (2, 4, 30, '2023-11-15'),  
	   (3, 1, 40, '2023-11-16'), 
	   (4, 3, 20, '2023-11-17'),
	   (5, 3, 25, '2023-11-18'), 
	   (6, 1, 35, '2023-11-19'),  
	   (7, 2, 15, '2023-11-20');

SELECT * From VideoGamesShops

-- MANAGERS --
INSERT INTO Managers (Mid, Name, PhoneNumber, Email)
VALUES 
	   (1, 'John Doe', '5559876541', 'john.doe@yahoo.com'),
	   (2, 'Jane Smith', '5559876543', 'jane.smith@yahoo.com'),
	   (3, 'Bob Johnson', '5555555555', 'bob.johnson@gmail.com'),
	   (4, 'Alice Williams', '5551112233', 'alice.williams@gmail.com'),
	   (5, 'David Miller', '5552223344', 'david.miller@gmail.com'),
	   (6, 'Emma Wilson', '5557778899', 'emma.wilson@yahoo.com'),
	   (7, 'Chris Anderson', '5554445566', 'chris.anderson@hotmail.com');

SELECT * From Managers

-- UPDATE statements --

SELECT * From Games
UPDATE Games
SET Price = 120
WHERE Name = 'PixelPlayground: Sports Edition' OR Bid = 2;

SELECT * From Games


SELECT * From Shops
UPDATE Shops
SET City = 'California'
WHERE NoOfClients >= 550 AND NoOfShops > 10 

SELECT * From Shops

-- DELETE statements

SELECT * From VideoGamesShops
DELETE FROM VideoGamesShops
WHERE Bid <> 2 AND Sid IN (1, 2); 


SELECT * From Managers
DELETE FROM Managers
WHERE Name LIKE 'J%' And Name IS NOT NULL;  


-- a. UNION, INTERSECT, EXCEPT

-- UNION -- 
SELECT *
FROM Shops
WHERE City = 'Denver' OR NoOfShops > 10
UNION
SELECT *
FROM Shops
WHERE City LIKE 'M%' OR NoOfClients > 400


-- INTERSECT --
SELECT *
FROM VideoGamesCompany
WHERE Vid <=3 and NoOfEmployees >50
INTERSECT
SELECT *
FROM VideoGamesCompany
WHERE Name LIKE 'G%' AND NoOfEmployees <=200



-- EXCEPT --
SELECT DISTINCT Price
FROM Games
WHERE Price >=20
EXCEPT
SELECT TOP 4 Price
FROM Games
WHERE Price <50
ORDER BY Price DESC;


-- b. INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN

-- INNER JOIN --
SELECT * From Managers
SELECT * From VideoGamesShops
SELECT * From shops

SELECT Shops.Name, VideoGamesShops.StockQuantity
FROM Shops
INNER JOIN VideoGamesShops ON Shops.Sid = VideoGamesShops.Sid
Order BY VideoGamesShops.StockQuantity ASC;

-- LEFT JOIN --
SELECT Shops.Name, VideoGamesShops.StockQuantity
FROM Shops
LEFT JOIN VideoGamesShops ON Shops.Sid = VideoGamesShops.Sid;

-- RIGHT JOIN --
SELECT Shops.Name, VideoGamesShops.StockQuantity
FROM Shops
RIGHT JOIN VideoGamesShops ON Shops.Sid = VideoGamesShops.Sid


-- FULL JOIN --
SELECT Shops.Name, VideoGamesShops.StockQuantity, Managers.Name
FROM Shops
FULL JOIN VideoGamesShops ON Shops.Sid = VideoGamesShops.Sid
FULL JOIN Managers ON Shops.Sid = Managers.Mid
Order BY Shops.Name ASC;

-- c. IN and EXISTS
-- IN --
SELECT *
FROM Shops
WHERE Sid IN (SELECT Mid FROM Managers WHERE Mid < 5);

-- EXISTS --
SELECT *
FROM Shops s
WHERE EXISTS (SELECT * FROM Managers WHERE Mid < 5 AND  Mid = s.Sid)
Order BY NoOfShops ASC;


select * from games
select * from VideoGamesShops

-- d. FROM
-- FROM --
SELECT VG.Gid, VG.Name, VG.Price
FROM (SELECT G.Gid, G.Name, G.Price, V.Sid
         FROM Games G INNER JOIN VideoGamesShops V ON G.Bid = V.Bid) VG


-- e. GROUP BY and HAVING

SELECT * FROM SHOPS
SELECT * FROM VIdeoGamesShops


-- Subquery in HAVING
SELECT S.Sid, MAX(VGS.StockQuantity) AS MaxStock
FROM Shops S
INNER JOIN VideoGamesShops VGS ON S.Sid = VGS.Sid
GROUP BY S.Sid
HAVING MAX(VGS.StockQuantity) > (SELECT AVG(StockQuantity) FROM VideoGamesShops);


SELECT S.Sid, AVG(VGS.StockQuantity) AvgStock
FROM Shops S
INNER JOIN VideoGamesShops VGS ON S.Sid = VGS.Sid
GROUP BY S.Sid
HAVING AVG(VGS.StockQuantity) > 10;


SELECT S.City, sum(VGS.StockQuantity) SumStock
FROM Shops S
INNER JOIN VideoGamesShops VGS ON S.Sid = VGS.Sid
GROUP BY S.City
