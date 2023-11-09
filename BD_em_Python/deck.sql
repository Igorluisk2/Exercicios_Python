create database deckshop;
use deckshop;

create table produtos(

	id int auto_increment primary key,
    nome varchar(255),
    quantidade varchar(3)
    
    );
    
insert into produtos values(1,"shape", "30");

select * from produtos;

drop database deckshop;