use der;

create table Customer(
Customer_ID int auto_increment not null,
Customer_Lname varchar (30) not null,
Customer_Fname varchar (30) not null,
Cust_street varchar (30) not null,
Cust_city varchar (30) not null,
St_code varchar (30) not null,
Cust_zip varchar (30) not null,
Fax_phone varchar (30) not null,
Acct_Code varchar (30) not null,
primary key (Customer_ID)
);

create table Acct_Typ_Cd_LU_Tab(
Acct_Code varchar(30) not null,
Account_Type varchar(30) not null,
primary key (Acct_Code)
);

create table Customer_Account(
Customer_ID int auto_increment not null, 
Last_purch_dte date not null,
Last_pymt_dte date not null,
Last_acct_trans_dte date not null,
Trans_code int not null, 
Acct_balance varchar(20) not null,
primary key(Customer_ID)
);

create table Transaction_code(
Trans_code int auto_increment not null,
Transaction_description varchar (30) not null,
primary key (Trans_code)
);

create table Customer_Acct_Hist1(
Customer_ID int auto_increment not null,
Trans_dte date not null,
Trans_code varchar(30) not null,
Old_acct_balance varchar(30) not null,
New_acct_balance varchar(30) not null,
primary key (Customer_ID)
);

create table Purchase_Order(
Seg_ID int auto_increment not null,
Purch_dte date not null,
Customer_ID int not null,
Bar_code varchar(20) not null,
Serial_num  varchar(40) not null,
Model_ID varchar(30) not null,
Quantity varchar(30) not null,
Price varchar(30) not null,
primary key (Seg_ID)
);

create table Bike_Description(
Model_ID int auto_increment not null,
Model_name varchar(30) not null,
Inv_price varchar(30) not null,
Sale_price varchar(30) not null,
Description varchar(30) not null,
primary key (Model_ID)
);

create table Bike_Inventory(
Seg_ID int auto_increment not null,
Serial_Number int not null,
Supplier_ID int not null,
Inventory_dte date not null,
Model_ID int not null,
primary key (Seg_ID)
);

create table Parts_Inventory(
Bar_code int auto_increment not null,
Part_name varchar(30) not null,
Supplier_ID  varchar(30) not null,
Prt_description varchar(40) not null,
Prt_cost varchar(30) not null,
Prt_price varchar(30) not null,
Quantity varchar(30) not null,
primary key (Bar_code)
);

create table State_lkup(
St_code int auto_increment not null,
State_name varchar (30) not null,
primary key (St_code)
);

create table Supplier(
Supplier_ID int auto_increment not null,
Suplier_name varchar (30) not null,
Sup_street varchar (30) not null,
Sup_city varchar (30) not null,
St_code varchar (30) not null,
Sup_zip varchar (30) not null,
Sup_phone varchar (30) not null,
Sup_fax varchar (30) not null,
primary key(Supplier_ID)
);


create database HubFabricas character set utf8mb4 collate utf8mb4_unicode_ci;
use HubFabricas;

create table ADM(
id int auto_increment,
Nome varchar (30) not null,
CPF varchar (14) not null,
Email varchar (30) not null,
Senha varchar (30) not null,
Fone varchar (11) not null, 


);

create table Banco_de_Vagas(
id int auto_increment,
Nome varchar (30) not null,
CPF varchar (14) not null,
Email varchar (30) not null,
Descricao_da_vaga varchar (30) not null,
representante varchar (14) not null,
Email varchar (30) not null,
Fone varchar (11) not null, 

);

create table Banco_de_Talentos(
id int auto_increment,
RG varchar (9) not null,
CPF varchar (14) not null,
Linkedin varchar (30) not null,
Git_hub varchar (30) not null,
Nome varchar (30) not null,
Data_nasc varchar (30) not null,
Fone varchar (11) not null, 

);

create table Edital(
id int auto_increment,
Nome varchar (30) not null,
Numero varchar (30) not null,
Data_inicial varchar (10) not null,
Data_final varchar (10) not null,
Endereço_do_arquivo varchar (30) not null,
Fone varchar (11) not null, 

);

create table Fabricas(
id int auto_increment,
Nome varchar (30) not null,
Endereço_da_imagem varchar (30) not null,
Texto varchar (30) not null,

);

create table Vagas_PSG(
id int auto_increment,
Nome varchar (30) not null,
CPF varchar (14) not null,
Email varchar (30) not null,
responsavel varchar (30) not null,
fone varchar (11) not null,
Dados_dos_pais varchar (30) not null,
Data_nasc varchar (30) not null,
Escolaridade varchar (30) not null,



