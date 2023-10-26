create database titanic_base;
use titanic_base;

-- PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked

create table passageiros(
passageiroID int,
sobrevivente varchar(5) not null,
passageiroClasse varchar(6) not null,
nome varchar(255) not null,
sexo varchar(50) not null,
idade varchar(50),
pais_filhos varchar(50) not null,
parentes varchar(5) not null,
bilhete varchar(50) not null,
tarifa varchar(50) not null,
cabine varchar(50),
embarcacao varchar(50) not null

);
-- drop database titanic_base;
select * from passageiros;
select nome,sexo,bilhete,sobrevivente from passageiros;
select count(sobrevivente) from passageiros;
select * from passageiros where sobrevivente = 1; 
select * from passageiros where idade <12; 
select count(sobrevivente) from passageiros where idade < 12 and sobrevivente = 1;
select count(sobrevivente) from passageiros where idade < 12 and sobrevivente = 0;
select count(sobrevivente) from passageiros where sexo = 'female' and sobrevivente = 1;
select count(sobrevivente) from passageiros where sexo = 'female' and sobrevivente = 0;
select count(sobrevivente) from passageiros where sexo = 'male' and sobrevivente = 1;
select count(sobrevivente) from passageiros where sexo = 'male' and sobrevivente = 0;
