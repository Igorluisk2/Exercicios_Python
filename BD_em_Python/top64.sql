create database top64;
use top64;

-- Game 	Developer(s)	Publisher(s)	Release date	Sales

create table games(
jogo varchar(50) not null,
desenvolvedor varchar(50) not null,
publicador varchar(50) not null,
lancamento varchar(50) not null,
vendas varchar(50) not null
);


-- drop table games;
select * from games;
select jogo,desenvolvedor,publicador from games;