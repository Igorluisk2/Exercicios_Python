use poorflix;
create table Usuário(
cpf varchar (30) not null,
nome varchar (30) not null,
fone varchar (30) not null,
email varchar (30) not null,
endereço varchar (30) not null,
cartão varchar (30) not null,
senha varchar (30) not null,
primary key (cpf)
);

create table mensalidade(
mes_ano date not null,
valor_pago float not null,
data_pago date not null,
primary key(mes_ano)
);

create table Video(
titulo varchar (40) not null,
ano varchar (30) not null,
duração varchar (30) not null,
produtora varchar (30) not null,
tipo varchar (30) not null,
episodio varchar (30) not null,
temporada varchar (30) not null,
primary key (titulo)
);

create table Ator(
nome varchar(30) not null,
data_nasci date not null,
local_nasci varchar(30) not null,
primary key(nome)
);