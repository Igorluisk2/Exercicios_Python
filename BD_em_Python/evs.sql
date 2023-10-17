create database evs;
use evs;
drop table eletric_car;
drop database evs;
create table eletric_car(
brand varchar (50),
model varchar(50),
AccelSec varchar(30),
TopSpeed_KmH varchar(25),
Range_Km varchar(30),
Efficiency_WhKm varchar(50),
FastCharge_KmH varchar(50),
RapidCharge varchar (3),
id_PowerTrain int,
constraint fk_powertrain foreign key (id_powertrain) references PowerTrain (id_powertrain),
id_PlugType int,
constraint fk_plugtype foreign key (id_plugtype) references PlugType (id_plugtype),
id_BodyStyle int,
constraint fk_bodystyle foreign key (id_bodystyle) references BodyStyle (id_bodystyle),
Segment varchar(1),
Seats int,
PriceEuro varchar(50)
);
drop table eletric_car;
insert into eletric_car values
("Tesla", "Model 3 Long Range Dual Motor", "4.6", "233", "450", "161", "940", "Yes", 1, 1, 1, "D", 5, "55480"),
("Volkswagen","ID.3 Pure","10","160","270","167","250","Yes",2,1,2,"C",5,"30000"),
("Polestar","2","4.7","210","400","181","620","Yes",1,1,3,"D",5,"56440"),
("BMW","iX3 ","6.8","180","360","206","560","Yes",2,1,4,"D",5,"68040"),
("Honda","e ","9.5","145","170","168","190","Yes",2,1,2,"B",4,"32997"),
("Lucid","Air ","2.8","250","610","180","620","Yes",1,2,1,"F",5,"105000"),
("Volkswagen","e-Golf ","9.6","150","190","168","220","Yes",3,1,2,"C",5,"31900"),
("Peugeot","e-208 ","8.1","150","275","164","420","Yes",3,1,2,"B",5,"29682"),
("Tesla","Model 3 Standard Range Plus","5.6","225","310","153","650","Yes",3,1,1,"D",5,"46380"),
("Audi","Q4 e-tron ","6.3","180","400","193","540","Yes",1,1,4,"D",5,"55000"),
("Mercedes","EQC 400 4MATIC","5.1","180","370","216","440","Yes",1,1,4,"D",5,"69484"),
("Nissan","Leaf ","7.9","144","220","164","230","Yes",3,2,2,"C",5,"29234"),
("Hyundai","Kona Electric 64 kWh","7.9","167","400","160","380","Yes",3,1,4,"B",5,"40795"),
("BMW","i4 ","4","200","450","178","650","Yes",2,1,4,"D",5,"65000"),
("Hyundai","IONIQ Electric","9.7","165","250","153","210","Yes",3,1,3,"C",5,"34459"),
("Volkswagen","ID.3 Pro S","7.9","160","440","175","590","Yes",2,1,2,"C",4,"40936"),
("Porsche","Taycan Turbo S","2.8","260","375","223","780","Yes",1,1,1,"F",4,"180781"),
("Volkswagen ","e-Up! ","11.9","130","195","166","170","Yes",3,1,2,"A",4,"21421"),
("MG","ZS EV","8.2","140","220","193","260","Yes",3,1,4,"B",5,"30000"),
("Mini","Cooper SE ","7.3","150","185","156","260","Yes",3,1,2,"B",4,"31681"),
("Opel","Corsa-e ","8.1","150","275","164","420","Yes",3,1,2,"B",5,"29146"),
("Tesla","Model Y Long Range Dual Motor","5.1","217","425","171","930","Yes",1,1,4,"D","7","58620"),
("Skoda","Enyaq iV 50","10","160","290","179","230","Yes",2,1,1,"C",5,"35000"),
("Audi","e-tron GT ","3.5","240","425","197","850","Yes",1,1,1,"F",4,"125000"),
("Tesla","Model 3 Long Range Performance","3.4","261","435","167","910","Yes",1,1,4,"D",5,"61480"),
("Volkswagen","ID.4 ","7.5","160","420","183","560","Yes",2,1,2,"C",5,"45000"),
("Volkswagen","ID.3 Pro","9","160","350","166","490","Yes",2,1,4,"C",5,"33000"),
("Volvo","XC40 P8 AWD Recharge","4.9","180","375","200","470","Yes",2,1,4,"C",5,"60437"),
("BMW","i3 120 Ah","7.3","150","235","161","270","Yes",1,1,4,"B",4,"38017"),
("Peugeot","e-2008 SUV ","8.5","150","250","180","380","Yes",3,1,4,"B",5,"34361"),
("Audi","e-tron 50 quattro","6.8","190","280","231","450","Yes",1,1,4,"E",5,"67358"),
("Kia","e-Niro 64 kWh","7.8","167","370","173","350","Yes",3,1,4,"C",5,"38105"),
("Renault","Zoe ZE50 R110","11.4","135","315","165","230","Yes",3,1,2,"B",5,"31184"),
("Tesla","Cybertruck Tri Motor","3","210","750","267","710","Yes",3,1,5,"N","6","75000"),
("Mazda","MX-30 ","9","150","180","178","240","Yes","2",1,4,"C",5,"32646"),
("Nissan","Leaf e+","7.3","157","325","172","390","Yes",1,2,2,"C",5,"37237"),
("Lexus","UX 300e","7.5","160","270","193","190","Yes",3,2,2,"C",5,"50000"),
("CUPRA","el-Born ","6.5","160","425","181","570","Yes",2,1,4,"C",4,"45000"),
("Renault","Zoe ZE50 R135","9.5","140","310","168","230","Yes",3,1,2,"B",5,"33133"),
("Mercedes","EQA ","5","200","350","171","440","Yes",1,1,4,"C",5,"45000"),
("Tesla","Model S Long Range","3.8","250","515","184","560","Yes",1,3,3,"F",5,"79990"),
("Hyundai ","Kona Electric 39 kWh","9.9","155","255","154","210","Yes",3,1,4,"B",5,"33971"),
("Audi","e-tron Sportback 55 quattro","5.7","200","380","228","610","Yes",1,1,4,"E",5,"81639"),
("Skoda","CITIGOe iV ","12.3","130","195","166","170","Yes",1,1,2,"A",4,"24534"),
("SEAT","Mii Electric ","12.3","130","195","166","170","Yes",3,1,2,"A",4,"20129"),
("Kia","e-Soul 64 kWh","7.9","167","365","175","340","Yes",3,1,4,"B",5,"36837"),
("Opel","Ampera-e ","7.3","150","335","173","210","Yes",1,1,"6","B",5,"41906"),
("Porsche","Taycan 4S","4","250","365","195","730","Yes",3,1,1,"F",4,"102945"),
("Lightyear","One ","10","150","575","104","540","Yes",1,1,4,"F",5,"149000"),
("Aiways","U5 ","9","150","335","188","350","Yes",1,1,4,"C",5,"36057");



select eletric_car.brand, eletric_car.model, eletric_car.AccelSec, eletric_car.TopSpeed_KmH, eletric_car.Range_Km, eletric_car.Efficiency_WhKm, 
FastCharge_KmH, eletric_car.RapidCharge, PowerTrain.powertrain, PlugType.plugtype, BodyStyle.bodystyles, eletric_car.Segment, eletric_car.Seat-s, eletric_car.PriceEuro
from eletric_car inner join PowerTrain on eletric_car.id_powertrain = PowerTrain.id_powertrain
inner join PlugType on eletric_car.id_PlugType = PlugType.id_plugtype inner join BodyStyle on eletric_car.id_BodyStyle = BodyStyle.id_bodystyle;

 select eletric_car.model, BodyStyle.bodystyle from eletric_car join BodyStyle on eletric_car.id_bodystyle = BodyStyle.id_bodystyle;
 select * from eletric_car;
 select * from BodyStyle;


describe eletric_car;

drop table BodyStyle;

create table BodyStyle(
id_bodystyle int primary key,
bodystyles varchar(10)
);

insert into BodyStyle values
(1, "Sedan"),
(2, "Hatchback"),
(3, "Liftback"),
(4, "SUV"),
(5, "Pickup"),
(6, "MPV");

create table PowerTrain(
id_powertrain int auto_increment primary key,
powertrain varchar (3)
);

insert into PowerTrain values
(1, "AWD"),
(2, "RWD"),
(3, "FWD");





create table PlugType(
id_plugtype int auto_increment primary key,
plugtype varchar (16)
);

insert into PlugType values
(1,"Type 2 CCS"),
(2, "Type 2 CHAdeMO"),
(3,"Type 2");

select * from PlugType;

drop table Brand;








