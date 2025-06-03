# Årsoppgave
Dette er en nettside hvor man kan skrive text, og bytte på farger og fonter. dessuten kan man registrere en bruker, loggen in, og logge ut.

Jeg har brukt html, css og javascript for å lage websiden, og python(flask) i backend for å få koble til en database på en raspberry pi.

## instalasjon av pakker:
flask: `pip install flask`

mysql connector: `pip install mysql-connector-python`

## instalasjon av mariadb (database):
på raspberry pien:
1. Update the package list: `sudo apt update`
2. Install MariaDB server and client: `sudo apt install mariadb-server mariadb-client`
3. Secure the installation: `sudo mariadb-secure-installation`
4. Start the MariaDB service: `sudo systemctl start mariadb`
5. Verify the installation: `mariadb -u root -p (enter your root password)`

## oppsett av database:
create database "navn";
create table users (id INT AUTO_INCREMENT PRIMARY KEY, user_name VARCHAR(255), epost VARCHAR(255));
## endre på verdier i koden (python):
`host = "10.2.3.63",`

`user = "Max@%",`

`password = "AX-d120",`

`database = "arsdatabase",`

`charset = "utf8mb4",`

`collation = "utf8mb4_general_ci"`
  
(bytt ut med egen data)

        
