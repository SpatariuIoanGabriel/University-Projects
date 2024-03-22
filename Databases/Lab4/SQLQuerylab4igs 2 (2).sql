USE VideoGamesShops
GO

-- a) Implement a stored procedure for the INSERT operation on 2 tables in a 1-n relationship
CREATE FUNCTION dbo.ShopExists(@ShopName VARCHAR(50), @City VARCHAR(50))
RETURNS int
AS
BEGIN
    DECLARE @ShopExists int;

    IF EXISTS (SELECT 1 FROM Shops WHERE Name = @ShopName AND City = @City)
        SET @ShopExists = 1;
    ELSE
        SET @ShopExists = 0;

    RETURN @ShopExists;
END;

GO

CREATE OR ALTER PROCEDURE InsertGameAndShopData
    @GameName VARCHAR(50),
    @Price INT,
    @Gid INT, 
    @Vid INT,  
    @ShopName VARCHAR(50),
    @City VARCHAR(50),
    @NoOfShops INT,
    @NoOfClients INT,
    @StockQuantity INT,
    @AddingDate DATE
AS
BEGIN
    DECLARE @ShopID INT;
    IF dbo.ShopExists(@ShopName, @City) = 0
    BEGIN
        INSERT INTO Shops (Name, City, NoOfShops, NoOfClients)
        VALUES (@ShopName, @City, @NoOfShops, @NoOfClients);

        SET @ShopID = SCOPE_IDENTITY(); 
    END
    ELSE
    BEGIN
        SET @ShopID = (SELECT Sid FROM Shops WHERE Name = @ShopName AND City = @City);
    END

    INSERT INTO Games (Name, Price, Gid, Vid)
    VALUES (@GameName, @Price, @Gid, @Vid);
    
    DECLARE @GameID INT;
    SET @GameID = SCOPE_IDENTITY(); 

    INSERT INTO VideoGamesShops (Bid, Sid, StockQuantity, AddingDate)
    VALUES (@GameID, @ShopID, @StockQuantity, @AddingDate);
END;

GO

-- Execute the stored procedure with sample data
EXEC InsertGameAndShopData
    @GameName = 'Galactic Conquest',
    @Price = 60,
    @Gid = 2, 
    @Vid = 3,  
    @ShopName = 'GameZone',
    @City = 'Bucharest',
    @NoOfShops = 1,
    @NoOfClients = 150,
    @StockQuantity = 100,
    @AddingDate = '2023-04-01';

GO

SELECT * FROM Shops;
SELECT * FROM Games;
SELECT * FROM VideoGamesShops;

GO

-- b) Create a view that extracts data from at least 3 tables
CREATE VIEW vw_GameOverview AS
SELECT
    G.Name AS GameName,
    GG.Name AS GenreName,
    VGC.Name AS CompanyName,
    S.Name AS ShopName,
    S.City,
    VGS.StockQuantity,
    VGS.AddingDate
FROM Games G
JOIN GamesGenres GG ON G.Gid = GG.Gid
JOIN VideoGamesCompany VGC ON G.Vid = VGC.Vid
JOIN VideoGamesShops VGS ON G.Bid = VGS.Bid
JOIN Shops S ON VGS.Sid = S.Sid;

GO

SELECT * FROM vw_GameOverview;

GO

-- c) Implement a trigger for a table for INSERT, UPDATE, or DELETE

-- Creating a ChangeLog table for logging changes in database tables
-- This table will store logs of data changes (inserts, updates, deletes) in specified tables
CREATE TABLE ChangeLog
(
    ChangeLogID INT PRIMARY KEY IDENTITY(1,1),
    ChangeDate DATETIME,
    ActionType VARCHAR(10),
    TableName VARCHAR(50),
    RecordCount INT
);

GO

-- Creating a TRIGGER for logging changes in the Games table
-- This trigger logs every insert, update, or delete operation on the Games table into the ChangeLog table
CREATE OR ALTER TRIGGER LogChangesOnGames
ON Games
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    DECLARE @ActionType VARCHAR(10);

    IF EXISTS (SELECT * FROM inserted)
    BEGIN
        IF EXISTS (SELECT * FROM deleted)
            SET @ActionType = 'UPDATE';
        ELSE
            SET @ActionType = 'INSERT';
    END
    ELSE
        SET @ActionType = 'DELETE';

    DECLARE @RecordCount INT;

    IF @ActionType = 'UPDATE'
        SET @RecordCount = (SELECT COUNT(*) FROM inserted);
    ELSE
        SET @RecordCount = (SELECT ISNULL(COUNT(*), 0) FROM inserted) + (SELECT ISNULL(COUNT(*), 0) FROM deleted);

    INSERT INTO ChangeLog (ChangeDate, ActionType, TableName, RecordCount)
    VALUES (GETDATE(), @ActionType, 'Games', @RecordCount);
END;

GO

select * from games

-- Testing the trigger with example operations
UPDATE Games SET Name = Name WHERE Bid = 5;
DELETE FROM VideoGamesShops WHERE Bid = 2;
DELETE FROM Games WHERE Bid = 4;

SELECT * FROM ChangeLog;

GO

-- d) Write a query that uses specific operators in the execution plan
SELECT g.Name AS GameName, vc.Name AS CompanyName, s.Name AS ShopName, vgs.StockQuantity, vgs.AddingDate
FROM Games g
INNER JOIN VideoGamesCompany vc ON g.Vid = vc.Vid
INNER JOIN VideoGamesShops vgs ON g.Bid = vgs.Bid
INNER JOIN Shops s ON vgs.Sid = s.Sid

WHERE g.Price > 50

ORDER BY g.Name, s.Name;


GO
