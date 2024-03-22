-- Create the VideoGamesShops database
CREATE DATABASE VideoGamesShops
go
USE VideoGamesShops
go

--Create the Shops table
CREATE TABLE Shops
(Sid INT PRIMARY KEY IDENTITY NOT NULL,
Name varchar(50) NOT NULL,
City varchar(50) NOT NULL,
NoOfShops int,
NoOfClients int)

-- Create the GamesGenres table
CREATE TABLE GamesGenres
(Gid INT PRIMARY KEY IDENTITY NOT NULL,
Name VARCHAR(50) NOT NULL,
NoOfGames int)

-- Create the VideoGamesCompany table
CREATE TABLE VideoGamesCompany
(Vid INT PRIMARY KEY IDENTITY NOT NULL,
Name VARCHAR(50) NOT NULL,
NoOfEmployees int)

-- Create the Games table
CREATE TABLE Games
(Bid INT PRIMARY KEY IDENTITY NOT NULL,
Name VARCHAR(50) NOT NULL,
Price int NOT NULL,
Gid int FOREIGN KEY REFERENCES GamesGenres(Gid) NOT NULL,
Vid int FOREIGN KEY REFERENCES VideoGamesCompany(Vid) NOT NULL)

-- Create the VideoGamesShops table
CREATE TABLE VideoGamesShops
(Bid INT FOREIGN KEY REFERENCES Games(Bid) NOT NULL,
Sid INT FOREIGN KEY REFERENCES Shops(Sid) NOT NULL,
StockQuantity int NOT NULL,
AddingDate DATE NOT NULL,
CONSTRAINT pk_Games PRIMARY KEY (Bid, Sid))

-- Create the Managers table
CREATE TABLE Managers
(Mid INT FOREIGN KEY REFERENCES Shops(Sid),
Name varchar(50) NOT NULL,
PhoneNumber varchar(50) NOT NULL,
Email varchar(50) NOT NULL,
CONSTRAINT pk_ShopsManagers PRIMARY KEY(Mid))


