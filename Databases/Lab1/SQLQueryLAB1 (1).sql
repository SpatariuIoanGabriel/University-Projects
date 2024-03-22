-- Create the VideoGamesShops database
CREATE DATABASE VideoGamesShops
go
USE VideoGamesShops
go

--Create the Shops table
CREATE TABLE Shops
(Sid INT PRIMARY KEY IDENTITY NOT NULL,
Name varchar(50) NOT NULL,
Addresss varchar(50) NOT NULL,
NoOfShops int)-- Create the GamesGenres table
CREATE TABLE GamesGenres
(Gid INT PRIMARY KEY IDENTITY NOT NULL,
Name VARCHAR(50) NOT NULL)
-- Create the GamesDevelopers table
CREATE TABLE GamesDevelopers
(Did INT PRIMARY KEY IDENTITY NOT NULL,
Name VARCHAR(50) NOT NULL,
Deparment VARCHAR(50) NOT NULL)

-- Create the Games table
CREATE TABLE Games
(Bid INT PRIMARY KEY IDENTITY NOT NULL,
Name VARCHAR(50) NOT NULL,
Price int NOT NULL,
Tid int FOREIGN KEY REFERENCES GamesGenres(Gid) NOT NULL,
Gid int FOREIGN KEY REFERENCES GamesDevelopers(Did) NOT NULL)

-- Create the VideoGamesShops table
CREATE TABLE VideoGamesShops
(Bid INT FOREIGN KEY REFERENCES Games(Bid) NOT NULL,
Sid INT FOREIGN KEY REFERENCES Shops(Sid) NOT NULL,
CONSTRAINT pk_Games PRIMARY KEY (Bid, Sid))

-- Create the Manager table
CREATE TABLE Manager
(Mid INT FOREIGN KEY REFERENCES Shops(Sid),
Name varchar(50) NOT NULL,
Age int NOT NULL,
CONSTRAINT pk_ShopsManagers PRIMARY KEY(Mid))