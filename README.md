Swarm Project

Function: This file has instructions on how to set up the database (if you do
not have already the  smember.db file) and how to run this program


How to run: type in the directory of these files: python3 swarm_member.py
This will start a server in the address you have in this file. It already
contains the localhost and Aryadne’s raspberry pi. To change this, just put your
new ip address in the table swarm of this database:

	(INSERT INTO swarm VALUES (3, ‘your-ip, your-port’))

How to create the smember data base:

	install sqlite3

Create de smember database running in the command line
(inside the directory you want):

	sqlite3 smember.db

inside the sqlite program type:

	CREATE TABLE static_data(
		ID MEDIUMINT PRIMARY KEY NOT NULL,
		VALUE CHAR(50),
		DESCRIPTION CHAR(50) NOT NULL,
		UNIT CHAR(20) NOT NULL);

	CREATE TABLE dynamic_data(
	   ID TINYINT PRIMARY KEY NOT NULL,
	   DESCRIPTION CHAR(4) NOT NULL,
	   UNIT TINYINT NOT NULL,
	   VALUE REAL,
	   TIMESTAMP REAL NOT NULL);
