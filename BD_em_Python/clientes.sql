create database cadastros;
use cadastros;

create table clientes(
id_cliente int auto_increment primary key,
CPF	varchar(25),
nome varchar(30),
RG varchar(25),
fone varchar(30),
id_estado int,
id_cidade int,
id_sexo int,
id_nacionalidade int,
id_raca int,
id_escolaridade int,
constraint fk_estado foreign key (id_estado) references estado (id_estado),
constraint fk_cidade foreign key (id_cidade) references estado (id_cidade),
constraint fk_sexo foreign key (id_sexo) references estado (id_sexo),
constraint fk_nacionalidade foreign key (id_nacionalidade) references estado (id_nacionalidade),
constraint fk_raca foreign key (id_raca) references estado (id_raca),
constraint fk_escolaridade foreign key (id_escolaridade) references estado (id_escolaridade),





);

create table estado(
id_estado int auto_increment primary key,
estado varchar(30)


);
create table cidade(
id_cidade int auto_increment primary key,
cidade varchar(30)
);

create table sexo(
id_sexo int auto_increment primary key,
sexo varchar(30)



);

create table nacionalidade (
id_nacionalidade int auto_increment primary key,
nacionalidade varchar(30)
);

create table raca (
id_raca int auto_increment primary key,
raca varchar(30)
);

create table escolaridade (
id_escolaridade int auto_increment primary key,
escolaridade varchar(30)
);

				/*inserts*/

insert into estado values (null, "Mato Grosso do Sul");
insert into estado values (null, "São Paulo");
insert into estado values (null, "Santa Catarina");
insert into estado values (null, "Paraná");
insert into estado values (null, "Rio Grande do sul");
insert into estado values (null, "Mato Grosso");
insert into estado values (null, "Minas Gerais");
insert into estado values (null, "Goias");
insert into estado values (null, "Tocantins");
insert into estado values (null, "Rio de Janeiro");
insert into estado values (null, "Espirito Santo");
insert into estado values (null, "Bahia");
insert into estado values (null, "Sergipe");
insert into estado values (null, "Alagoas");
insert into estado values (null, "Pernanbuco");
insert into estado values (null, "Paraiba");
insert into estado values (null, "Rio Grande do Norte");
insert into estado values (null, "Ceará");
insert into estado values (null, "Piauí");
insert into estado values (null, "Maranhão");
insert into estado values (null, "Pará");
insert into estado values (null, "Amapá");
insert into estado values (null, "Amazonas");
insert into estado values (null, "Rondônia");
insert into estado values (null, "Roraima");
insert into estado values (null, "Acre");
insert into estado values (null, "Distrito Federal");



		/* cidades */

/*MS */
insert into cidade values (null, "Campo Grande");
insert into cidade values (null, "Bonito");
insert into cidade values (null, "Dourados");
insert into cidade values (null, "Ponta Porã");
insert into cidade values (null, "Três Lagoas");

/*SP*/
insert into cidade values (null, "São Paulo");
insert into cidade values (null, "Araçatuba");
insert into cidade values (null, "Santos");
insert into cidade values (null, "Piracicaba");
insert into cidade values (null, "São Bernardo");

/*SC*/
insert into cidade values (null, "Florianopolis");
insert into cidade values (null, "Lajes");
insert into cidade values (null, "Itajaí");
insert into cidade values (null, "Laguna");
insert into cidade values (null, "Joinville");

/*Pr*/
insert into cidade values (null, "Curitiba");
insert into cidade values (null, "Cascavel");
insert into cidade values (null, "Rio Negro");
insert into cidade values (null, "Ponta Grossa");
insert into cidade values (null, "Jacarezinho");

/*Rs*/
insert into cidade values (null, "Porto Alegre");
insert into cidade values (null, "Rio Grande");
insert into cidade values (null, "Santa Maria");
insert into cidade values (null, "Erexim");
insert into cidade values (null, "Santa Maria");

/*Mt*/
insert into cidade values (null, "Cuiaba");
insert into cidade values (null, "Claudia");
insert into cidade values (null, "Denise");
insert into cidade values (null, "Vera");
insert into cidade values (null, "Jangada");

/*Mg*/
insert into cidade values (null, "Belo Horizonte");
insert into cidade values (null, "Juiz de Fora");
insert into cidade values (null, "Poços de Caldas");
insert into cidade values (null, "Uberaba");
insert into cidade values (null, "Uberlandia");

/*GO*/
insert into cidade values (null, "Goiania");
insert into cidade values (null, "Mineiros");
insert into cidade values (null, "Luziania");
insert into cidade values (null, "Ceres");
insert into cidade values (null, "Catalão");

/*TO*/
insert into cidade values (null, "Palmas");
insert into cidade values (null, "Araguaína");
insert into cidade values (null, "Gurupi");
insert into cidade values (null, "Porto Nacional");
insert into cidade values (null, "Paraíso do Tocantins");

/*RJ*/
insert into cidade values (null, "Rio de Janeiro");
insert into cidade values (null, "Niterói");
insert into cidade values (null, "Nova Iguaçu");
insert into cidade values (null, "Duque de Caxias");
insert into cidade values (null, "São Gonçalo");

/*ES*/
insert into cidade values (null, "Vitória");
insert into cidade values (null, "Serra");
insert into cidade values (null, "Linhares");
insert into cidade values (null, "Vila Velha");
insert into cidade values (null, "Cariacica");

/*Bahia*/
insert into cidade values (null, "Salvador");
insert into cidade values (null, "Feira de Santana");
insert into cidade values (null, "Vitória da Conquista");
insert into cidade values (null, "Camaçari");
insert into cidade values (null, "Itabuna");

/*Sergipe*/
insert into cidade values (null, "Aracaju");
insert into cidade values (null, "Lagarto");
insert into cidade values (null, "Itabaiana");
insert into cidade values (null, "Estância");
insert into cidade values (null, "Nossa Senhora do Socorro");

/*AL*/
insert into cidade values (null, "Maceió");
insert into cidade values (null, "Arapiraca");
insert into cidade values (null, "Rio Largo");
insert into cidade values (null, "Penedo");
insert into cidade values (null, "Palmeira dos Índios");

/*PE*/
insert into cidade values (null, "Recife");
insert into cidade values (null, "Olinda");
insert into cidade values (null, "Jaboatão dos Guararapes");
insert into cidade values (null, "Caruaru");
insert into cidade values (null, "Petrolina");

/*PB*/
insert into cidade values (null, "João Pessoa");
insert into cidade values (null, "Campina Grande");
insert into cidade values (null, "Santa Rita");
insert into cidade values (null, "Patos");
insert into cidade values (null, "Bayeux");

/*RN*/
insert into cidade values (null, "Natal");
insert into cidade values (null, "Mossoró");
insert into cidade values (null, "Parnamirim");
insert into cidade values (null, "Caicó");
insert into cidade values (null, "Macaíba");

/*CE*/
insert into cidade values (null, "Fortaleza");
insert into cidade values (null, "Caucaia");
insert into cidade values (null, "Juazeiro do Norte");
insert into cidade values (null, "Maracanaú");
insert into cidade values (null, "Sobral");

/*PI*/
insert into cidade values (null, "Teresina");
insert into cidade values (null, "Parnaíba");
insert into cidade values (null, "Picos");
insert into cidade values (null, "Floriano");
insert into cidade values (null, "Piripiri");

/*Maranhão*/
insert into cidade values (null, "São Luis");
insert into cidade values (null, "Imperatriz");
insert into cidade values (null, "Timon");
insert into cidade values (null, "Caxias");
insert into cidade values (null, "Codó");

/*Pará*/
insert into cidade values (null, "Belem");
insert into cidade values (null, "Marabá");
insert into cidade values (null, "Ananindeua");
insert into cidade values (null, "Santarém");
insert into cidade values (null, "Castanhal");

/*Amapá*/
insert into cidade values (null, "Macapá");
insert into cidade values (null, "Santana");
insert into cidade values (null, "Laranjal do Jari");
insert into cidade values (null, "Oiapoque");
insert into cidade values (null, "Mazagão");

/*Amazonas*/
insert into cidade values (null, "Manaus");
insert into cidade values (null, "Parintins");
insert into cidade values (null, "Itacoatiara");
insert into cidade values (null, "Manacapuru");
insert into cidade values (null, "Coari");

/*Rondonia*/
insert into cidade values (null, "Porto Velho");
insert into cidade values (null, "Ji-Paraná");
insert into cidade values (null, "Ariquemes");
insert into cidade values (null, "Vilhena");
insert into cidade values (null, "Cacoal");

/*Roraima*/
insert into cidade values (null, "Boa Vista");
insert into cidade values (null, "Rorainópolis");
insert into cidade values (null, "Caracaraí");
insert into cidade values (null, "Bonfim");
insert into cidade values (null, "Mucajaí");

/*Acre*/
insert into cidade values (null, "Rio Branco");
insert into cidade values (null, "Cruzeiro do Sul");
insert into cidade values (null, "Sena Madureira");
insert into cidade values (null, "Tarauacá");
insert into cidade values (null, "Feijó");

/*DF*/
insert into cidade values (null, "Brasília");
insert into cidade values (null, "Ceilândia");
insert into cidade values (null, "Samambaia");
insert into cidade values (null, "Plano Piloto");
insert into cidade values (null, "Taguatinga");


	/* sexos */

insert into sexo values (null, "Feminino");
insert into sexo values (null, "Masculino");
insert into sexo values (null, "Apache");

	/*Nacionalidade */
    insert into nacionalidade values (null, "Brasileira");
    insert into raca values (null, "Estrangeira");

	/* raça */
insert into raca values (null, "Preto");
insert into raca values (null, "Branco");
insert into raca values (null, "Pardo");
insert into raca values (null, "Indígina");
insert into raca values (null, "Asiático");

	/*Escolaridade*/
insert into escolaridade values (null, "Educação Infantil");
insert into escolaridade values (null, "Ensino Fundamental");
insert into escolaridade values (null, "Ensino Medio");
insert into escolaridade values (null, "Ensino Técnico");
insert into escolaridade values (null, "Ensino Superior Bacharelado");
insert into escolaridade values (null, "Ensino Superior Mestrado");
insert into escolaridade values (null, "Ensino Superior Doutorado");
insert into escolaridade values (null, "Educação Continuada");

			/*selects */
select clientes.nome, cidade.cidade from clientes join cidade on clientes.id_cliente = cidade.id_cidade;
select clientes.nome, estado.estado from clientes join estado on clientes.id_cliente = cidade.id_estado;








