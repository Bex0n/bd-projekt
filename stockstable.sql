CREATE TABLE stocks (
	name VARCHAR(255),
	date DATE,
	open FLOAT,
	high FLOAT,
	low FLOAT,
	close FLOAT,
	adjclose FLOAT,
	volume INT
);

CREATE TABLE ownedstocks (
	id INT PRIMARY KEY,
	name VARCHAR(255),
	date DATE,
	open FLOAT,
	volume INT
);

CREATE TABLE historystocks (
	id INT PRIMARY KEY,
	name VARCHAR(255),
	date DATE,
	open FLOAT,
	close FLOAT,
	volume INT
);