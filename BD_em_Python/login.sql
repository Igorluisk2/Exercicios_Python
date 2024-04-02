create database exloginadm;
use exloginadm;

create table user(
username varchar (50),
passw varchar (50),
setor varchar (50));

insert into user values ('igor','12345','admin');
insert into user values ('suporte','12345','support');

alter table user add column (setor varchar(255) not null);

describe user;

drop table user;
