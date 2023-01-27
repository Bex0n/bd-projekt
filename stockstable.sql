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
	name VARCHAR(255),
	date DATE,
	open FLOAT,
	volume INT
);