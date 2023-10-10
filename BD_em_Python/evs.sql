create database evs;
use evs;

create table eletric_car(
id_brand int auto_increment primary key,
model varchar(50),
AccelSec varchar(30),
TopSpeed_KmH varchar(25),
Range_Km varchar(30),
Efficiency_WhKm int,
FastCharge_KmH int,
RapidCharge varchar (3),
id_PowerTrain int,
id_PlugType int,
id_BodyStyle int,
Segment varchar(1),
Seats int,
PriceEuro int
);
drop table eletric_car;
insert into eletric_car values
(null, "Model 3 Long Range Dual Motor", "4.6", "233", "450", "161", "940", "Yes", null, null, null, "D", 5, "55480"),
(null,"ID.3 Pure","10","160","270","167","250","Yes",null,null,null,"C","5","30000"),
(null,"2","4.7","210","400","181","620","Yes",null,null,null,"D","5","56440"),
(null,"iX3 ","6.8","180","360","206","560","Yes",null,null,null,"D","5","68040"),
(null,"e ","9.5","145","170","168","190","Yes",null,null,null,"B","4","32997"),
(null,"Air ","2.8","250","610","180","620","Yes",null,null,null,"F","5","105000"),
(null,"e-Golf ","9.6","150","190","168","220","Yes",null,null,null,"C","5","31900"),
(null,"e-208 ","8.1","150","275","164","420","Yes",null,null,null,"B","5","29682"),
(null,"Model 3 Standard Range Plus","5.6","225","310","153","650","Yes",null,null,null,"D","5","46380"),
(null,"Q4 e-tron ","6.3","180","400","193","540","Yes",null,null,null,"D","5","55000"),
(null,"EQC 400 4MATIC","5.1","180","370","216","440","Yes",null,null,null,"D","5","69484"),
(null,"Leaf ","7.9","144","220","164","230","Yes",null,null,null,"C","5","29234"),
(null,"Kona Electric 64 kWh","7.9","167","400","160","380","Yes",null,null,null,"B","5","40795"),
(null,"i4 ","4","200","450","178","650","Yes",null,null,null,"D","5","65000"),
(null,"IONIQ Electric","9.7","165","250","153","210","Yes",null,null,null,"C","5","34459"),
(null,"ID.3 Pro S","7.9","160","440","175","590","Yes",null,null,null,"C","4","40936"),
(null,"Taycan Turbo S","2.8","260","375","223","780","Yes",null,null,null,"F","4","180781"),
(null,"e-Up! ","11.9","130","195","166","170","Yes",null,null,null,"A","4","21421"),
(null,"ZS EV","8.2","140","220","193","260","Yes",null,null,null,"B","5","30000"),
(null,"Cooper SE ","7.3","150","185","156","260","Yes",null,null,null,"B","4","31681"),
(null,"Corsa-e ","8.1","150","275","164","420","Yes",null,null,null,"B","5","29146"),
(null,"Model Y Long Range Dual Motor","5.1","217","425","171","930","Yes",null,null,null,"D","7","58620"),
(null,"Enyaq iV 50","10","160","290","179","230","Yes",null,null,null,"C","5","35000"),
(null,"e-tron GT ","3.5","240","425","197","850","Yes",null,null,null,"F","4","125000"),
(null,"Model 3 Long Range Performance","3.4","261","435","167","910","Yes",null,null,null,"D","5","61480"),
(null,"ID.4 ","7.5","160","420","183","560","Yes",null,null,null,"C","5","45000"),
(null,"ID.3 Pro","9","160","350","166","490","Yes",null,null,null,"C","5","33000"),
(null,"XC40 P8 AWD Recharge","4.9","180","375","200","470","Yes",null,null,null,"C","5","60437"),
(null,"i3 120 Ah","7.3","150","235","161","270","Yes",null,null,null,"B","4","38017"),
(null,"e-2008 SUV ","8.5","150","250","180","380","Yes",null,null,null,"B","5","34361"),
(null,"e-tron 50 quattro","6.8","190","280","231","450","Yes",null,null,null,"E","5","67358"),
(null,"e-Niro 64 kWh","7.8","167","370","173","350","Yes",null,null,null,"C","5","38105"),
(null,"Zoe ZE50 R110","11.4","135","315","165","230","Yes",null,null,null,"B","5","31184"),
(null,"Cybertruck Tri Motor","3","210","750","267","710","Yes",null,null,null,"N","6","75000"),
(null,"MX-30 ","9","150","180","178","240","Yes",null,null,null,"C","5","32646"),
(null,"Leaf e+","7.3","157","325","172","390","Yes",null,null,null,"C","5","37237"),
(null,"UX 300e","7.5","160","270","193","190","Yes",null,null,null,"C","5","50000"),
(null,"el-Born ","6.5","160","425","181","570","Yes",null,null,null,"C","4","45000"),
(null,"Zoe ZE50 R135","9.5","140","310","168","230","Yes",null,null,null,"B","5","33133"),
(null,"EQA ","5","200","350","171","440","Yes",null,null,null,"C","5","45000"),
(null,"Model S Long Range","3.8","250","515","184","560","Yes",null,null,null,"F","5","79990"),
(null,"Kona Electric 39 kWh","9.9","155","255","154","210","Yes",null,null,null,"B","5","33971"),
(null,"e-tron Sportback 55 quattro","5.7","200","380","228","610","Yes",null,null,null,"E","5","81639"),
(null,"CITIGOe iV ","12.3","130","195","166","170","Yes",null,null,null,"A","4","24534"),
(null,"Mii Electric ","12.3","130","195","166","170","Yes",null,null,null,"A","4","20129"),
(null,"e-Soul 64 kWh","7.9","167","365","175","340","Yes",null,null,null,"B","5","36837"),
(null,"Ampera-e ","7.3","150","335","173","210","Yes",null,null,null,"B","5","41906"),
(null,"Taycan 4S","4","250","365","195","730","Yes",null,null,null,"F","4","102945"),
(null,"One ","10","150","575","104","540","Yes",null,null,null,"F","5","149000"),
(null,"U5 ","9","150","335","188","350","Yes",null,null,null,"C","5","36057"),
(null,"e-tron 55 quattro","5.7","200","365","237","590","Yes",null,null,null,"E","5","79445"),
(null,"Roadster ","2.1","410","970","206","920","Yes",null,null,null,"S","4","215000"),
(null,"Mokka-e ","8.5","150","255","176","390","Yes",null,null,null,"B","5","35000"),
(null,"Enyaq iV 80","8.8","160","420","183","560","Yes",null,null,null,"C","5","40000"),
(null,"Model X Long Range","4.6","250","450","211","490","Yes",null,null,null,"F","7","85990"),
(null,"e Advance","8.3","145","170","168","190","Yes",null,null,null,"B","4","35921"),
(null,"3 Crossback E-Tense","8.7","150","250","180","380","Yes",null,null,null,"B","5","37422"),
(null,"Twingo ZE","12.6","135","130","164","0","No",null,null,null,"A","4","24790"),
(null,"e-C4 ","9.7","150","250","180","380","Yes",null,null,null,"C","5","40000"),
(null,"Model S Performance","2.5","261","505","188","550","Yes",null,null,null,"F","5","96990"),
(null,"Zoe ZE40 R110","11.4","135","255","161","230","Yes",null,null,null,"B","5","29234"),
(null,"Model Y Long Range Performance","3.7","241","410","177","900","Yes",null,null,null,"D","7","65620"),
(null,"Ariya 87kWh","7.6","160","440","198","520","Yes",null,null,null,"C","5","50000"),
(null,"I-Pace ","4.8","200","365","232","340","Yes",null,null,null,"E","5","75351"),
(null,"Mustang Mach-E ER RWD","7","180","450","200","430","Yes",null,null,null,"D","5","54475"),
(null,"Taycan 4S Plus","4","250","425","197","890","Yes",null,null,null,"F","4","109302"),
(null,"e-NV200 Evalia ","14","123","190","200","190","Yes",null,null,null,"N","7","33246"),
(null,"Cybertruck Dual Motor","5","190","460","261","710","Yes",null,null,null,"N","6","55000"),
(null,"Kangoo Maxi ZE 33","22.4","130","160","194","0","No",null,null,null,"N","5","38000"),
(null,"Mustang Mach-E ER AWD","6","180","430","209","410","Yes",null,null,null,"D","5","62900"),
(null,"i3s 120 Ah","6.9","160","230","165","260","Yes",null,null,null,"B","4","41526"),
(null,"Enyaq iV 80X","7","160","400","193","540","Yes",null,null,null,"C","5","45000"),
(null,"Taycan Cross Turismo ","3.5","250","385","217","770","Yes",null,null,null,"F","4","150000"),
(null,"M-Byte 95 kWh 4WD","5.5","190","390","244","460","Yes",null,null,null,"E","5","64000"),
(null,"Sion ","9","140","225","156","270","Yes",null,null,null,"C","5","25500"),
(null,"e-Niro 39 kWh","9.8","155","235","167","230","Yes",null,null,null,"C","5","34400"),
(null,"Q4 Sportback e-tron ","6.3","180","410","188","550","Yes",null,null,null,"D","5","57500"),
(null,"EQ forfour ","12.7","130","95","176","0","No",null,null,null,"A","4","22030"),
(null,"Mustang Mach-E SR AWD","6","180","340","206","360","Yes",null,null,null,"D","5","54000"),
(null,"Taycan Turbo","3.2","260","390","215","810","Yes",null,null,null,"F","4","148301"),
(null,"ID.3 1st","7.3","160","340","171","470","Yes",null,null,null,"C","5","38987"),
(null,"Model X Performance","2.8","250","440","216","480","Yes",null,null,null,"F","7","102990"),
(null,"EQ fortwo coupe","11.6","130","100","167","0","No",null,null,null,"A","2","21387"),
(null,"Mustang Mach-E SR RWD","6.6","180","360","194","380","Yes",null,null,null,"D","5","46900"),
(null,"EQV 300 Long","10","140","330","273","290","Yes",null,null,null,"N","7","70631"),
(null,"500e Hatchback","9","150","250","168","330","Yes",null,null,null,"B","4","34900"),
(null,"Cybertruck Single Motor","7","180","390","256","740","Yes",null,null,null,"N","6","45000"),
(null,"e-tron Sportback 50 quattro","6.8","190","295","219","470","Yes",null,null,null,"E","5","69551"),
(null,"Enyaq iV vRS","6.2","180","400","193","540","Yes",null,null,null,"C","5","47500"),
(null,"Enyaq iV 60","9","160","320","181","440","Yes",null,null,null,"C","5","37500"),
(null,"e-tron S 55 quattro","4.5","210","320","270","510","Yes",null,null,null,"E","5","93800"),
(null,"EQ fortwo cabrio","11.9","130","95","176","0","No",null,null,null,"A","2","24565"),
(null,"e-Soul 64 kWh","7.9","167","365","175","320","Yes",null,null,null,"B","5","36837"),
(null,"Ariya e-4ORCE 87kWh","5.7","200","420","207","500","Yes",null,null,null,"C","5","57500"),
(null,"500e Convertible","9","150","250","168","330","Yes",null,null,null,"B","4","37900"),
(null,"ID.3 Pro Performance","7.3","160","340","171","470","Yes",null,null,null,"C","5","35575"),
(null,"e-Soul 39 kWh","9.9","157","230","170","220","Yes",null,null,null,"B","5","33133"),
(null,"M-Byte 72 kWh 2WD","7.5","190","325","222","420","Yes",null,null,null,"E","5","53500"),
(null,"Ariya 63kWh","7.5","160","330","191","440","Yes",null,null,null,"C","5","45000"),
(null,"e-tron S Sportback 55 quattro","4.5","210","335","258","540","Yes",null,null,null,"E","5","96050"),
(null,"Ariya e-4ORCE 63kWh","5.9","200","325","194","440","Yes",null,null,null,"C","5","50000"),
(null,"Ariya e-4ORCE 87kWh Performance","5.1","200","375","232","450","Yes",null,null,null,"C","5","65000"),
(null,"M-Byte 95 kWh 2WD","7.5","190","400","238","480","Yes",null,null,null,"E","5","62000");


 select eletric_car.model, BodyStyle.bodystyle from eletric_car join BodyStyle on eletric_car.id_bodystyle = BodyStyle.id_bodystyle;
 select * from eletric_car;
 select * from BodyStyle;





create table BodyStyle(
id_bodystyle int,
bodystyle varchar (16),
constraint fk_bodystyle foreign key (id_bodystyle) references eletric_car (id_BodyStyle)
);

insert into BodyStyle values
(null, "Sedan"),
(null, "Hatchback"),
(null, "Liftback"),
(null, "SUV"),
(null, "Pickup"),
(null, "MPV"),
(null, "Cabrio"),
(null, "SPV"),
(null, "Station");

create table PowerTrain(
id_powertrain int auto_increment primary key,
powertrain varchar(3),
constraint fk_powertrain foreign key (id_powertrain) references PowerTrain (id_powertrain)
);

insert into PowerTrain values
(null, "AWD"),
(null, "RWD"),
(null, "FWD");

create table Brand(
id_brand int auto_increment primary key,
brand varchar (16)
);

insert into Brand values
(null,"Tesla"),
(null,"Volkswagen"),
(null,"Polestar"),
(null,"BMW"),
(null,"Honda"),
(null,"Lucid"),
(null,"Peugeot "),
(null,"Audi"),
(null,"Mercedes"),
(null,"Nissan"),
(null,"Porsche"),
(null,"Hyundai"),
(null,"Kia"),
(null,"Renault"),
(null,"Skoda"),
(null,"Ford"),
(null,"Opel"),
(null,"Mini"),
(null,"MG"),
(null,"Volvo"),
(null,"Mazda"),
(null,"Lexus"),
(null,"CUPRA"),
(null,"SEAT"),
(null,"Lightyear"),
(null,"Aiways"),
(null,"DS"),
(null,"Citroen"),
(null,"Jaguar"),
(null,"Fiat"),
(null,"Smart"),
(null,"Byton"),
(null,"Sono");

create table PlugType(
id_plugtype int auto_increment primary key,
plugtype varchar (15),
constraint fk_plugtype foreign key (id_plugtype) references PlugType (id_plugtype)
);

insert into PlugType values
(null,"Type 2 CCS"),
(null, "Type 2 CHAdeMO"),
(null,"Type 2");

select * from PlugType;

drop table Brand;








