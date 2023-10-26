create database prod;
use prod;

create table produtos(
	
    referencia varchar(3) primary key,
    descricao varchar(50) unique,
    estoque int not null default 0

);

create table itensvenda(

	venda int,
    produto varchar(3),
    quantidade int

);

insert into produtos values ("001", "Feijão", 10);
insert into produtos values ("002", "Arroz", 5);
insert into produtos values ("003", "Farinha", 15);

insert into itensvenda values (1, "001", 3);
insert into itensvenda values (1, "002", 1);
insert into itensvenda values (1, "003", 5);

delete from produtos where descricao = "Arroz";
delete from itensvenda where produto = "001";

select * from produtos;
select * from itensvenda;


delimiter $

create trigger tgr_itensVenda_insert after insert 
on itensvenda 
for each row 
begin 
	update produtos set estoque = estoque - new.quantidade where referencia = new.produto;
end $

create trigger tgr_itensVenda_delete after delete 
on itensvenda 
for each row 
begin 
	update produtos set estoque = estoque + old.quantidade where referencia = old.produto;
end $

delimiter ;

show triggers;

