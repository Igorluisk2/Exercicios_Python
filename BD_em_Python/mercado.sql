create database mercado character set utf8mb4 collate utf8mb4_unicode_ci;
use mercado;
create table fornecedor(
cod_fornecedor varchar(10) not null,
nome varchar(30),
cidade_sede varchar(30),
grupo_cod_fornecer varchar(10),
primary key(cod_fornecedor)
);
create table material(
cod_material varchar(10) not null,
cod_fornecedor varchar(10) not null,
nome varchar(30),
descricao varchar(30),
primary key(cod_material),
constraint material foreign key(cod_fornecedor) references fornecedor(cod_fornecedor)
);
insert into fornecedor values('ABC','ABC Materiais Eletronicos','Vitoria',null);
insert into fornecedor values('XYZ','XYZ Materiais de Escritorio','Rio de Janeiro','HiX');
insert into fornecedor values('Hidra','Hidra Materiais Hidraulicos','Sao Paulo','HiX');
insert into fornecedor values('HiX','HidraX Materiais Eletricos H','Sao Paulo',null);
select * from fornecedor;

insert into material values('123','ABC','Tomada eletrica 10A Nova',null);
insert into material values('234','ABC','Disjuntor 25A',null);
insert into material values('345','XYZ','Resma Papel A4',null);
insert into material values('456','XYZ','Toner Imp HR5522',null);
insert into material values('678','Hidra','Cano PVC 1/2',null);
insert into material values('679','Hidra','Cano PVC 3/4',null);
insert into material values('680','Hidra','Medidor hidr 1/2',null);
insert into material values('681','Hidra','Joelho 1/2',null); 
insert into material values('682','Hidra','Junta 1/2',null);
insert into material values('1234','ABC','Tomada eletrica 20A Nova',null);
insert into material values('2345','XYZ','Caneta Azul',null);
insert into material values('4567','XYZ','Grapeador',null);
insert into material values('4568','XYZ','Caneta Marca Texto Amarela',null);
insert into material values(4569,'XYZ','Lapis HB',null); 

select * from material;