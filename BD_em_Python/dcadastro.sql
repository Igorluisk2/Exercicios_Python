create database dcadastro;
use dcadastro;

create table cadastro(
	id int auto_increment primary key,
    sobrenome varchar(55) not null,
    cpf varchar(55) not null,
    rg varchar(55) not null,
    telefone varchar(55) not null,
    sexo varchar(55) not null,
    cep varchar(55) not null,
    cnh varchar(55) not null,
    estado_civil varchar(55) not null,
	endereco varchar (55) not null

);

drop database dcadastro;

select * from cadastro;