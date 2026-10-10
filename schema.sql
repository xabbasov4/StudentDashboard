CREATE DATABASE UniversityDB;
GO

USE UniversityDB;
GO

CREATE TABLE Students (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(100) NOT NULL,
    Score FLOAT NOT NULL
);
GO

INSERT INTO Students (Name, Score) VALUES 
('Ali', 85),
('Leyla', 72),
('Murad', 48),
('Aysel', 91),
('Kamran', 63);
GO

-- Stored Procedure: GetStudentResult
CREATE PROCEDURE GetStudentResult
AS
BEGIN
    SELECT 
        Name,
        Score,
        CASE 
            WHEN Score >= 90 THEN 'A'
            WHEN Score >= 80 THEN 'B'
            WHEN Score >= 70 THEN 'C'
            WHEN Score >= 60 THEN 'D'
            ELSE 'F'
        END AS Grade
    FROM Students;
END;
GO