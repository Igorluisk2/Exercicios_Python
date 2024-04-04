create database exloginadm;
use exloginadm;

create table user(
username varchar (50),
passw varchar (50),
setor varchar (50));

insert into user values ('igor','12345','admin');
insert into user values ('suporte','12345','support');

alter table user add column (setor varchar(255) not null);

describe fabricaUsers;

drop table fabricaUsers;


create table fabricaUsers(
id int auto_increment not null primary key,
name varchar(255) not null,
cpf varchar(255) not null,
rg varchar(255) not null,
telefone varchar(255) not null,
email varchar(255) not null,
mother varchar(255) not null,
father varchar(255) not null,
street varchar(255) not null,
neighborhood varchar(255) not null,
number varchar(255) not null,
cep varchar(255) not null,
complement varchar(255) not null
);

INSERT INTO fabricaUsers (name, cpf, rg, telefone, email, mother, father, street, neighborhood, number, cep, complement)
VALUES 
('João Silva', '123.456.789-00', '12345678', '(11) 91234-5678', 'joao@example.com', 'Maria Silva', 'José Silva', 'Rua A', 'Centro', '123', '12345-678', 'Ap. 101'),
('Maria Santos', '987.654.321-00', '98765432', '(11) 98765-4321', 'maria@example.com', 'Ana Santos', 'Pedro Santos', 'Rua B', 'Bairro 1', '456', '54321-987', 'Casa'),
('Pedro Oliveira', '111.222.333-44', '11122233', '(11) 87654-3210', 'pedro@example.com', 'Clara Oliveira', 'Lucas Oliveira', 'Rua C', 'Bairro 2', '789', '67890-123', 'Sobrado'),
('Ana Souza', '555.666.777-88', '55566677', '(11) 76543-2109', 'ana@example.com', 'Teresa Souza', 'Rafael Souza', 'Rua D', 'Bairro 3', '012', '09876-543', 'Loja'),
('Lucas Pereira', '999.888.777-66', '99988877', '(11) 65432-1098', 'lucas@example.com', 'Camila Pereira', 'Marcos Pereira', 'Rua E', 'Bairro 4', '345', '23456-789', 'Bloco 1, Ap. 202'),
('Carla Costa', '333.222.111-00', '33322211', '(11) 54321-0987', 'carla@example.com', 'Isabela Costa', 'Fernando Costa', 'Rua F', 'Bairro 5', '678', '87654-321', 'Andar 3'),
('Rafaela Lima', '444.555.666-99', '44455566', '(11) 43210-9876', 'rafaela@example.com', 'Juliana Lima', 'Rodrigo Lima', 'Rua G', 'Bairro 6', '901', '76543-210', 'Cobertura'),
('Marcos Oliveira', '777.888.999-00', '77788899', '(11) 32109-8765', 'marcos@example.com', 'Patrícia Oliveira', 'Antônio Oliveira', 'Rua H', 'Bairro 7', '234', '65432-109', 'Térreo'),
('Fernanda Santos', '222.333.444-55', '22233344', '(11) 21098-7654', 'fernanda@example.com', 'Cristina Santos', 'Paulo Santos', 'Rua I', 'Bairro 8', '567', '21098-765', 'Apartamento'),
('Rodrigo Silva', '666.777.888-99', '66677788', '(11) 10987-6543', 'rodrigo@example.com', 'Roberta Silva', 'Gustavo Silva', 'Rua J', 'Bairro 9', '890', '10987-654', 'Fundos'),
('Juliana Castro', '888.777.666-55', '88877766', '(11) 98765-4321', 'juliana@example.com', 'Daniela Castro', 'Márcio Castro', 'Rua K', 'Bairro 10', '234', '98765-432', 'Casa 2'),
('Márcio Almeida', '555.444.333-22', '55544433', '(11) 87654-3210', 'marcio@example.com', 'Vanessa Almeida', 'Ricardo Almeida', 'Rua L', 'Bairro 11', '567', '87654-321', 'Apartamento 2'),
('Vanessa Oliveira', '444.333.222-11', '44433322', '(11) 76543-2109', 'vanessa@example.com', 'Fernando Oliveira', 'Adriana Oliveira', 'Rua M', 'Bairro 12', '890', '76543-210', 'Bloco 2, Ap. 101'),
('Ricardo Souza', '333.222.111-00', '33322211', '(11) 65432-1098', 'ricardo@example.com', 'Carolina Souza', 'Daniel Souza', 'Rua N', 'Bairro 13', '012', '65432-109', 'Sala 1'),
('Carolina Lima', '222.111.000-99', '22211100', '(11) 54321-0987', 'carolina@example.com', 'Gabriel Lima', 'Fátima Lima', 'Rua O', 'Bairro 14', '345', '54321-098', 'Sala 2'),
('Gabriel Pereira', '111.000.999-88', '11100099', '(11) 43210-9876', 'gabriel@example.com', 'Aline Pereira', 'Sérgio Pereira', 'Rua P', 'Bairro 15', '678', '43210-987', 'Andar 1'),
('Aline Santos', '000.999.888-77', '00099988', '(11) 32109-8765', 'aline@example.com', 'Fábio Santos', 'Mariana Santos', 'Rua Q', 'Bairro 16', '901', '32109-876', 'Andar 2'),
('Fábio Oliveira', '999.888.777-66', '99988877', '(11) 21098-7654', 'fabio@example.com', 'Renata Oliveira', 'Gustavo Oliveira', 'Rua R', 'Bairro 17', '234', '21098-765', 'Lateral'),
('Renata Silva', '888.777.666-55', '88877766', '(11) 10987-6543', 'renata@example.com', 'Luciana Silva', 'Carlos Silva', 'Rua S', 'Bairro 18', '567', '10987-654', 'Frente'),
('Luciana Almeida', '777.666.555-44', '77766655', '(11) 98765-4321', 'luciana@example.com', 'Marcos Almeida', 'Amanda Almeida', 'Rua T', 'Bairro 19', '890', '98765-432', 'Esquina'),
('Marcos Castro', '666.555.444-33', '66655544', '(11) 87654-3210', 'marcos_c@example.com', 'Patrícia Castro', 'Rafael Castro', 'Rua U', 'Bairro 20', '012', '87654-321', 'Apartamento 3'),
('Patrícia Oliveira', '555.444.333-22', '55544433', '(11) 76543-2109', 'patricia_o@example.com', 'Marcelo Oliveira', 'Camila Oliveira', 'Rua V', 'Bairro 21', '345', '76543-210', 'Fundos 2'),
('Marcelo Lima', '444.333.222-11', '44433322', '(11) 65432-1098', 'marcelo_l@example.com', 'Silvana Lima', 'Ricardo Lima', 'Rua W', 'Bairro 22', '678', '65432-109', 'Térreo 2'),
('Silvana Santos', '333.222.111-00', '33322211', '(11) 54321-0987', 'silvana_s@example.com', 'Carlos Santos', 'Marta Santos', 'Rua X', 'Bairro 23', '901', '54321-098', 'Casa 3'),
('Carlos Pereira', '222.111.000-99', '22211100', '(11) 43210-9876', 'carlos_p@example.com', 'Camila Pereira', 'André Pereira', 'Rua Y', 'Bairro 24', '234', '43210-987', 'Loja 2'),
('Camila Souza', '111.000.999-88', '11100099', '(11) 32109-8765', 'camila_s@example.com', 'Roberto Souza', 'Amanda Souza', 'Rua Z', 'Bairro 25', '567', '32109-876', 'Andar 4'),
('Roberto Oliveira', '000.999.888-77', '00099988', '(11) 21098-7654', 'roberto_o@example.com', 'Lucas Oliveira', 'Vitória Oliveira', 'Avenida A', 'Bairro 26', '890', '21098-765', 'Sobrado 2'),
('Lucas Lima', '999.888.777-66', '99988877', '(11) 10987-6543', 'lucas_l@example.com', 'Mariana Lima', 'Pedro Lima', 'Avenida B', 'Bairro 27', '012', '10987-654', 'Cobertura 2'),
('Mariana Castro', '888.777.666-55', '88877766', '(11) 98765-4321', 'mariana_c@example.com', 'Rafael Castro', 'Lívia Castro', 'Avenida C', 'Bairro 28', '345', '98765-432', 'Térreo 3'),
('Rafael Almeida', '777.666.555-44', '77766655', '(11) 87654-3210', 'rafael_a@example.com', 'Ana Almeida', 'Bruno Almeida', 'Avenida D', 'Bairro 29', '678', '87654-321', 'Apartamento 4'),
('Ana Oliveira', '666.555.444-33', '66655544', '(11) 76543-2109', 'ana_o@example.com', 'Felipe Oliveira', 'Carla Oliveira', 'Avenida E', 'Bairro 30', '901', '76543-210', 'Fundos 3'),
('Felipe Lima', '555.444.333-22', '55544433', '(11) 65432-1098', 'felipe_l@example.com', 'Cristina Lima', 'Diego Lima', 'Avenida F', 'Bairro 31', '234', '65432-109', 'Térreo 4'),
('Cristina Souza', '444.333.222-11', '44433322', '(11) 54321-0987', 'cristina_s@example.com', 'Luiz Souza', 'Fernanda Souza', 'Avenida G', 'Bairro 32', '567', '54321-098', 'Casa 4'),
('Luiz Castro', '333.222.111-00', '33322211', '(11) 43210-9876', 'luiz_c@example.com', 'Bruno Castro', 'Carolina Castro', 'Avenida H', 'Bairro 33', '890', '43210-987', 'Loja 3'),
('Bruno Almeida', '222.111.000-99', '22211100', '(11) 32109-8765', 'bruno_a@example.com', 'Márcia Almeida', 'Ricardo Almeida', 'Avenida I', 'Bairro 34', '012', '32109-876', 'Andar 5'),
('Márcia Oliveira', '111.000.999-88', '11100099', '(11) 21098-7654', 'marcia_o@example.com', 'Vinícius Oliveira', 'Larissa Oliveira', 'Avenida J', 'Bairro 35', '345', '21098-765', 'Sobrado 3'),
('Vinícius Lima', '000.999.888-77', '00099988', '(11) 10987-6543', 'vinicius_l@example.com', 'Juliano Lima', 'Amanda Lima', 'Avenida K', 'Bairro 36', '678', '10987-654', 'Cobertura 3'),
('Juliano Castro', '999.888.777-66', '99988877', '(11) 98765-4321', 'juliano_c@example.com', 'Mariana Castro', 'Ricardo Castro', 'Avenida L', 'Bairro 37', '901', '98765-432', 'Térreo 5'),
('Mariana Almeida', '888.777.666-55', '88877766', '(11) 87654-3210', 'mariana_a@example.com', 'Thiago Almeida', 'Gabriela Almeida', 'Avenida M', 'Bairro 38', '234', '87654-321', 'Apartamento 5'),
('Thiago Oliveira', '777.666.555-44', '77766655', '(11) 76543-2109', 'thiago_o@example.com', 'Amanda Oliveira', 'João Oliveira', 'Avenida N', 'Bairro 39', '567', '76543-210', 'Fundos 4'),
('Amanda Souza', '666.555.444-33', '66655544', '(11) 65432-1098', 'amanda_s@example.com', 'Leonardo Souza', 'Luana Souza', 'Avenida O', 'Bairro 40', '890', '65432-109', 'Térreo 6'),
('Leonardo Lima', '555.444.333-22', '55544433', '(11) 54321-0987', 'leonardo_l@example.com', 'Fernanda Lima', 'Rodrigo Lima', 'Avenida P', 'Bairro 41', '012', '54321-098', 'Casa 5'),
('Fernanda Castro', '444.333.222-11', '44433322', '(11) 43210-9876', 'fernanda_c@example.com', 'Marcelo Castro', 'André Castro', 'Avenida Q', 'Bairro 42', '345', '43210-987', 'Loja 4'),
('Marcelo Almeida', '333.222.111-00', '33322211', '(11) 32109-8765', 'marcelo_a@example.com', 'Patricia Almeida', 'Marcos Almeida', 'Avenida R', 'Bairro 43', '678', '32109-876', 'Andar 6'),
('Patricia Souza', '222.111.000-99', '22211100', '(11) 21098-7654', 'patricia_s@example.com', 'Rodrigo Souza', 'Carla Souza', 'Avenida S', 'Bairro 44', '901', '21098-765', 'Sobrado 4'),
('Rodrigo Oliveira', '111.000.999-88', '11100099', '(11) 10987-6543', 'rodrigo_o@example.com', 'Vanessa Oliveira', 'Pedro Oliveira', 'Avenida T', 'Bairro 45', '234', '10987-654', 'Cobertura 4'),
('Vanessa Castro', '000.999.888-77', '00099988', '(11) 98765-4321', 'vanessa_c@example.com', 'Bruno Castro', 'Renata Castro', 'Avenida U', 'Bairro 46', '567', '98765-432', 'Térreo 7'),
('Bruno Lima', '999.888.777-66', '99988877', '(11) 87654-3210', 'bruno_l@example.com', 'Lucas Lima', 'Aline Lima', 'Avenida V', 'Bairro 47', '890', '87654-321', 'Apartamento 6'),
('Lucas Almeida', '888.777.666-55', '88877766', '(11) 76543-2109', 'lucas_a@example.com', 'Gabriela Almeida', 'Felipe Almeida', 'Avenida W', 'Bairro 48', '012', '76543-210', 'Fundos 5'),
('Gabriela Oliveira', '777.666.555-44', '77766655', '(11) 65432-1098', 'gabriela_o@example.com', 'Fábio Oliveira', 'Amanda Oliveira', 'Avenida X', 'Bairro 49', '345', '65432-109', 'Térreo 8'),
('Fábio Souza', '666.555.444-33', '66655544', '(11) 54321-0987', 'fabio_s@example.com', 'Mariana Souza', 'Leonardo Souza', 'Avenida Y', 'Bairro 50', '678', '54321-098', 'Casa 6');

select * from fabricaUsers;