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
constraint fk_cidade foreign key (id_cidade) references cidade (id_cidade),
constraint fk_sexo foreign key (id_sexo) references sexo (id_sexo),
constraint fk_nacionalidade foreign key (id_nacionalidade) references nacionalidade (id_nacionalidade),
constraint fk_raca foreign key (id_raca) references raca (id_raca),
constraint fk_escolaridade foreign key (id_escolaridade) references escolaridade (id_escolaridade)
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

#-------------------------------------------#
#           Cadastros de Clente             #
#-------------------------------------------#

insert into clientes values (null, "09583810037", "Ana", "428779086", "(82) 98135-7863", null, null, null, null, null, null);
insert into clientes values (null, "61416831002", "Bruno", "339219397", "(64) 99114-1603", null, null, null, null, null, null);
insert into clientes values (null, "05665108049", "Carlos", "339219397", "(92) 99527-4776", null, null, null, null, null, null);
insert into clientes values (null, "27595409012", "Dantener", "434228977", "(86) 97618-7381", null, null, null, null, null, null);
insert into clientes values (null, "27056934080", "Eduardo", "217934687", "(67) 99785-3276", null, null, null, null, null, null);
insert into clientes values (null, "44123831052", "Ederson", "349681375", "(94) 96733-4290", null, null, null, null, null, null);
insert into clientes values (null, "82669259090", "Fernando", "310164771", "(66) 98532-8113", null, null, null, null, null, null);
insert into clientes values (null, "55433747042", "Gabriel", "272143996", "(92) 97454-7042", null, null, null, null, null, null);
insert into clientes values (null, "94648170032", "Hentony", "177391820", "(94) 96705-3530", null, null, null, null, null, null);
insert into clientes values (null, "73600809083", "Jade", "256051124", "(84) 97225-9129", null, null, null, null, null, null);
insert into clientes values (null, "79690454056", "Kauanny", "490893867", "(35) 98643-4301", null, null, null, null, null, null);
insert into clientes values (null, "87395177053", "Kaua", "389643476", "(84) 98329-1581", null, null, null, null, null, null);
insert into clientes values (null, "75981349018", "Larissa", "389643476", "(97) 97166-8275", null, null, null, null, null, null);
insert into clientes values (null, "79798865006", "Mauricio", "471014606", "(69) 98581-3205", null, null, null, null, null, null);
insert into clientes values (null, "43492892086", "Naíara", "295559895", "(94) 99544-3337", null, null, null, null, null, null);
insert into clientes values (null, "22613667010", "Osvaldo", "378826402", "(24) 96916-4413", null, null, null, null, null, null);
insert into clientes values (null, "36373824071", "Pedro", "101587004", "(94) 99813-2432", null, null, null, null, null, null);
insert into clientes values (null, "79692507009", "Paulo", "165149115", "(86) 98355-8924", null, null, null, null, null, null);
insert into clientes values (null, "45872764057", "Quiteria", "302793781", "(91) 97170-1334", null, null, null, null, null, null);
insert into clientes values (null, "23571860039", "Raimundo", "340782304", "(83) 98834-6310", null, null, null, null, null, null);
insert into clientes values (null, "59034408000", "Sarah", "108642379", "(97) 98024-2476", null, null, null, null, null, null);
insert into clientes values (null, "45872764057", "Thiago", "505502707", "(88) 99846-9398", null, null, null, null, null, null);
insert into clientes values (null, "58828179007", "Uriel", "252298032", "(88) 99846-9398", null, null, null, null, null, null);

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
insert into nacionalidade values (null, "Estrangeira");

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

			/* selects */
select clientes.nome, cidade.cidade from clientes join cidade on clientes.id_cliente = cidade.id_cidade;
select clientes.nome, estado.estado from clientes join estado on clientes.id_cliente = estado.id_estado;
select clientes.nome, clientes.cpf, raca.raca  from clientes join raca on clientes.id_cliente = raca.id_raca;
select clientes.nome, nacionalidade.nacionalidade from clientes join nacionalidade on clientes.id_cliente = nacionalidade.id_nacionalidade;
select clientes.nome, escolaridade.escolaridade from clientes join escolaridade on clientes.id_cliente = escolaridade.id_escolaridade;
select clientes.nome, estado.estado, cidade.cidade from clientes inner join estado on clientes.id_cliente = estado.id_estado inner join cidade on estado.id_estado = cidade.id_cidade;

select clientes.nome, cidade.cidade, estado.estado, clientes.fone, clientes.rg, sexo.sexo, nacionalidade.nacionalidade, raca.raca, escolaridade.escolaridade from clientes inner join cidade on cidade.id_cidade = clientes.id_cliente 
inner join estado on clientes.id_cliente = estado.id_estado inner join sexo on sexo.id_sexo = clientes.id_cliente inner join nacionalidade on nacionalidade.id_nacionalidade = clientes.id_cliente 
inner join raca on raca.id_raca = clientes.id_cliente inner join escolaridade on escolaridade.id_escolaridade = clientes.id_cliente;


		/* updates */
update cidade set cidade = "Abaixo de M" where cidade like "a%";
update nacionalidade set nacionalidade = "Fora do Brasil" Where nacionalidade = "Estrangeira";
update raca set raca = "Serese Humanos";
update estado set estado = "Centro Oeste" where estado = "Mato Grosso do Sul";
update estado set estado = "Centro Oeste" where estado = "Mato Grosso";
update estado set estado = "Centro Oeste" where estado = "Goias";
update estado set estado = "Centro Oeste" where estado = "Distrito Federal";

select * from nacionalidade;
		/* Delete's */



select clientes.nome from clientes;
delete from clientes where nome = 'Quiteria';
delete from clientes where nome = 'Raimundo';

select * from clientes;




