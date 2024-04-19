Criando o db:

CREATE DATABASE italiancars;
GO

USE italiancars;
GO

CREATE TABLE Fabricante (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nomeFabricante VARCHAR(50) NOT NULL
);

CREATE TABLE Carro (
    id INT IDENTITY(1,1) PRIMARY KEY,
    idFabricante INT FOREIGN KEY REFERENCES Fabricante(id),
    modelo VARCHAR(50) NOT NULL,
    ano INT NOT NULL,
    cor VARCHAR(50) NOT NULL,
    km INT NOT NULL,
    preco FLOAT NOT NULL
);

INSERT INTO Fabricante(nomeFabricante) VALUES
('Alfa Romeo'),
('Ferrari'),
('Maserati');


Rodando a aplicação:

pip install flask

pip install pyodbc

python app.py
