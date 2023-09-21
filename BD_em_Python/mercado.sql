
create database vendas;
use vendas;

CREATE TABLE CIDADE (
    CODCID   INTEGER NOT NULL,
    NOMECID  VARCHAR(60),
    UF       CHAR(2)
);

CREATE TABLE CLIENTE (
    CODCLI    INTEGER NOT NULL,
    NOME      VARCHAR(60),
    ENDERECO  VARCHAR(60),
    CODCID    SMALLINT NOT NULL,
    CEP       CHAR(10),
    CPF       CHAR(20)
);

CREATE TABLE ITEMPEDIDO (
    NUMPED   INTEGER NOT NULL,
    CODPROD  INTEGER NOT NULL,
    QTDADE   SMALLINT
);

CREATE TABLE PEDIDO (
    NUMPED   INTEGER NOT NULL,
    ENTREGA  SMALLINT,
    CODCLI   INTEGER,
    CODVEND  INTEGER
);

CREATE TABLE PRODUTO (
    CODPROD    INTEGER NOT NULL,
    DESCRICAO  VARCHAR(25),
    UNIDADE    CHAR(3),
    VALOR_UN   NUMERIC(10,2)
);

CREATE TABLE SETOR (
    CODSETOR   INTEGER NOT NULL,
    NOMESETOR  VARCHAR(50)
);

CREATE TABLE VENDEDOR (
    CODVEND   INTEGER NOT NULL,
    NOMEVEND  VARCHAR(60),
    CODSETOR  SMALLINT,
    SALARIO   NUMERIC(10,2)
);

INSERT INTO CIDADE (CODCID, NOMECID, UF) VALUES (1, 'DOURADOS', 'MS');
INSERT INTO CIDADE (CODCID, NOMECID, UF) VALUES (2, 'CAMPO GRANDE', 'MS');
INSERT INTO CIDADE (CODCID, NOMECID, UF) VALUES (3, 'SÃO PAULO', 'SP');
INSERT INTO CIDADE (CODCID, NOMECID, UF) VALUES (4, 'CUIABA', 'MT');
INSERT INTO CIDADE (CODCID, NOMECID, UF) VALUES (5, 'FLORIANÓPOLIS', 'SC');
INSERT INTO CIDADE (CODCID, NOMECID, UF) VALUES (6, 'SÃO SEBASTIÃO', 'SC');
INSERT INTO CIDADE (CODCID, NOMECID, UF) VALUES (7, 'CAARAPÓ', 'MS');
INSERT INTO CIDADE (CODCID, NOMECID, UF) VALUES (8, 'BRASÍLIA', 'DF');
INSERT INTO CIDADE (CODCID, NOMECID, UF) VALUES (10, 'TUPÃ', 'SP');
INSERT INTO CIDADE (CODCID, NOMECID, UF) VALUES (11, 'SÃO JOSÉ DO RIO PRETO', 'SP');
INSERT INTO CIDADE (CODCID, NOMECID, UF) VALUES (12, 'APUCARANA', 'PR');
INSERT INTO CIDADE (CODCID, NOMECID, UF) VALUES (13, 'JARDIM', 'MS');
INSERT INTO CIDADE (CODCID, NOMECID, UF) VALUES (14, 'JATEI', 'MS');
INSERT INTO CIDADE (CODCID, NOMECID, UF) VALUES (15, 'AMAMBAI', 'MS');

COMMIT WORK;

INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (1, 'Nicolash Pereira Rodrigues', 'Rua José Germano, 1456', 1, '13971-150 ', '13971-150           ');
INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (2, 'Cauã Oliveira Azevedo', 'Rua Luís Squilace, 175', 3, '05326-010 ', '855.498.901-51      ');
INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (3, 'Martim Melo Araujo', 'Rua de Mizar, 429', 2, '32550-220 ', '421.837.827-49      ');
INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (4, 'Matheus Pinto Almeida', 'Travessa Getúlio Vargas, 1426', 4, '54250-382 ', NULL);
INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (5, 'Estevan Pereira Cardoso', 'Travessa Maria da Penha Costa, 692', 5, '29707-190 ', '231.416.173-41      ');
INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (6, 'Rebeca Sousa Fernandes', 'Avenida da Saudade, 1899', 3, '09030-030 ', NULL);
INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (7, 'Thaís Melo Rodrigues', 'Rua N, 1379', 11, '35900-626 ', '884.501.839-36      ');
INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (8, 'Matheus Martins Ribeiro', 'Rua Ubaldo Damiano, 1006', 1, '17204-281 ', NULL);
INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (9, 'Leonardo Barros Melo', 'Rua Treze de Maio, 808', 2, '65900-220 ', '735.643.235-89      ');
INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (10, 'Emilly Rocha Ribeiro', 'Passagem Santa Luzia, 221', 1, '66117-060 ', '613.666.706-12      ');
INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (11, 'Luan Goncalves Melo', 'Rua Chapada Velha, 944', 3, '05728-070 ', '656.106.888-25      ');
INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (12, 'Júlia Gomes Araujo', 'Rua Alamanda, 751', 3, '06728-320 ', '184.206.138-00      ');
INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (13, 'Camila Rodrigues Barbosa', 'Rua dos Cumarus, 1977', 2, '38703-678 ', '973.600.869-06      ');
INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (14, 'Melissa Araujo Almeida', 'Rua 104A, 1820', 1, '74083-310 ', '677.324.633-40      ');
INSERT INTO CLIENTE (CODCLI, NOME, ENDERECO, CODCID, CEP, CPF) VALUES (15, 'Laura Barros Rodrigues', 'Rua Doutor Muraí, 697', 3, '03159-080 ', '670.936.770-37      ');

COMMIT WORK;

INSERT INTO SETOR (CODSETOR, NOMESETOR) VALUES (1, 'JARDIM');
INSERT INTO SETOR (CODSETOR, NOMESETOR) VALUES (2, 'VENENOS');
INSERT INTO SETOR (CODSETOR, NOMESETOR) VALUES (3, 'PEÇAS');
INSERT INTO SETOR (CODSETOR, NOMESETOR) VALUES (4, 'FERRAMENTAS');
INSERT INTO SETOR (CODSETOR, NOMESETOR) VALUES (5, 'VACINAS');
INSERT INTO SETOR (CODSETOR, NOMESETOR) VALUES (6, 'VESTUÁRIO');

COMMIT WORK;

INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (1, 'ANTONIO CARLOS DA SILVA', 1, 500);
INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (2, 'ROGERIO SANTOS AMADO', 1, 550);
INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (3, 'JOÃO FLORISVALDO JESUS', 2, 800);
INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (4, 'PEDRO CELESTINO VENÂNCIO', 3, 1000);
INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (5, 'JAIR COSTA', 3, 1000);
INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (6, 'ELIZA DOS ANJOS', 4, 700);
INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (7, 'DENIS OTTANO', 5, 600);
INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (8, 'RONEI ARAÚJO BATISTA', 6, 400);
INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (9, 'JAMES CHEN VILAREAL', 6, 400);
INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (10, 'FABIO BENDITO REIS', 4, 700);
INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (11, 'EDILSON NOGUEIRA', 2, 800);
INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (12, 'RODOLFO DOS SANTOS', 4, 450);
INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (13, 'CRISTIANE ANTUNES ROCHA', 3, 450);
INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (14, 'CRISLAINE RUBENS AZEVEDO', 1, 500);
INSERT INTO VENDEDOR (CODVEND, NOMEVEND, CODSETOR, SALARIO) VALUES (15, 'JADER DE AMARO', 4, 1500);

COMMIT WORK;

INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (1, 5, 1, 3);
INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (2, 2, 2, 5);
INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (3, 10, 4, 1);
INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (4, 20, 1, 2);
INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (5, 2, 8, 9);
INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (6, 2, 2, 4);
INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (7, 10, 5, 7);
INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (8, 2, 14, 11);
INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (9, 5, 15, 15);
INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (10, 5, 15, 4);
INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (11, 20, 9, 10);
INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (12, 10, 9, 11);
INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (13, 1, 5, 6);
INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (14, 1, 13, 9);
INSERT INTO PEDIDO (NUMPED, ENTREGA, CODCLI, CODVEND) VALUES (15, 20, 12, 5);

COMMIT WORK;

INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (1, 'MATA CUPIM', 'UN ', 25);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (2, 'GLIFOSSATO', 'UN ', 12);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (3, 'RANDAP', 'UN ', 33);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (4, 'SERRA CIRCULAR', 'UN ', 200);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (5, 'ROÇADEIRA', 'UN ', 378);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (6, 'MOTO SERRA', 'UN ', 400);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (7, 'CORTADOR DE GRAMA', 'UN ', 800);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (8, 'PÁ DE PONTA', 'UN ', 70);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (9, 'VACINA BDD', 'CX ', 299);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (10, 'VACINA DDD', 'CX ', 200);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (11, 'MASCARA', 'UN ', 5);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (12, 'MASCARA SILICONE', 'UN ', 10);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (13, 'PINO CORTADOR', 'UN ', 5);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (14, 'ROSCA SERRA 22', 'UN ', 12);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (15, 'MANGUEIRA 04', 'M  ', 25);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (16, 'BICO MANGUEIRA', 'UN ', 3);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (17, 'ROUPA PROTECAO', 'UN ', 53);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (18, 'PULVERIZADOR', 'UN ', 76);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (19, 'CHAPEU DE PALHA', 'UN ', 34);
INSERT INTO PRODUTO (CODPROD, DESCRICAO, UNIDADE, VALOR_UN) VALUES (20, 'LUVA DE BORRACHA', 'UN ', 2);

COMMIT WORK;

INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (1, 1, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (1, 3, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (1, 10, 2);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (2, 4, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (3, 2, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (3, 3, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (4, 9, 5);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (4, 11, 2);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (4, 12, 2);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (5, 2, 2);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (5, 11, 2);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (5, 18, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (5, 20, 2);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (6, 5, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (7, 7, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (8, 8, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (10, 2, 2);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (10, 12, 3);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (10, 17, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (10, 18, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (10, 19, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (13, 8, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (13, 19, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (13, 20, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (14, 13, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (14, 17, 1);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (15, 15, 20);
INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES (15, 16, 1);

COMMIT WORK;



/******************************************************************************/
/*                                Primary keys                                */
/******************************************************************************/

ALTER TABLE CIDADE ADD CONSTRAINT PK_CIDADE PRIMARY KEY (CODCID);
ALTER TABLE CLIENTE ADD CONSTRAINT PK_CLIENTE PRIMARY KEY (CODCLI);
ALTER TABLE ITEMPEDIDO ADD CONSTRAINT PK_ITEMPEDIDO PRIMARY KEY (NUMPED, CODPROD);
ALTER TABLE PEDIDO ADD CONSTRAINT PK_PEDIDO PRIMARY KEY (NUMPED);
ALTER TABLE PRODUTO ADD CONSTRAINT PK_PRODUTO PRIMARY KEY (CODPROD);
ALTER TABLE SETOR ADD CONSTRAINT PK_SETOR PRIMARY KEY (CODSETOR);
ALTER TABLE VENDEDOR ADD CONSTRAINT PK_VENDEDOR PRIMARY KEY (CODVEND);


/******************************************************************************/
/*                                Foreign keys                                */
/******************************************************************************/

ALTER TABLE CLIENTE ADD CONSTRAINT FK_CLIENTE_1 FOREIGN KEY (CODCID) REFERENCES CIDADE (CODCID);
ALTER TABLE ITEMPEDIDO ADD CONSTRAINT FK_ITEMPEDIDO_1 FOREIGN KEY (CODPROD) REFERENCES PRODUTO (CODPROD);
ALTER TABLE ITEMPEDIDO ADD CONSTRAINT FK_ITEMPEDIDO_2 FOREIGN KEY (NUMPED) REFERENCES PEDIDO (NUMPED);
ALTER TABLE PEDIDO ADD CONSTRAINT FK_PEDIDO_1 FOREIGN KEY (CODCLI) REFERENCES CLIENTE (CODCLI);
ALTER TABLE PEDIDO ADD CONSTRAINT FK_PEDIDO_2 FOREIGN KEY (CODVEND) REFERENCES VENDEDOR (CODVEND);
ALTER TABLE VENDEDOR ADD CONSTRAINT FK_VENDEDOR_1 FOREIGN KEY (CODSETOR) REFERENCES SETOR (CODSETOR);


/******************************************************************************/
/*                                SELECTS                                     */
/******************************************************************************/

select count(CODCID) from CIDADE;
select count(CODCLI) from CLIENTE;
select count(CODPROD) from PRODUTO;
select count(CODSETOR) from SETOR;
select count(NUMPED) from PEDIDO;

Select max(SALARIO) from VENDEDOR;
select * from VENDEDOR where SALARIO = 1500.00;
select min(SALARIO) from VENDEDOR;
select * from VENDEDOR where SALARIO = 400.00;

select max(QTDADE) from ITEMPEDIDO;
select min(QTDADE) from ITEMPEDIDO;

select min(VALOR_UN) from PRODUTO;
select max(VALOR_UN) from PRODUTO;

select * from PRODUTO where VALOR_UN = 2.00;
select * from PRODUTO where VALOR_UN = 800;

select * from VENDEDOR where CODSETOR = 4;
select count(CODSETOR) from VENDEDOR where CODSETOR = 4;

select * from VENDEDOR where CODCLI = 5;
select count(CODCLI) from PEDIDO where CODSCLI = 5;

select * from VENDEDOR;
select * from SETOR;