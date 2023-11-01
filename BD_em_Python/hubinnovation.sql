create database hubinnovation;
use hubinnovation;

-- drop database hubinnovation;

create table cadastro(
	
    id_cad int primary key,
    nome varchar(255),
    email varchar(255),
    fone varchar(255),
    cpf varchar(255),
    nascimento date,
    genero varchar(255),
	cad_pale int
);

create table palestra(
	
    id_pale int,
	titulo varchar(255),
    nomepale varchar(255),
	vagas int,
    descricao varchar(655),
    sala int
);


/*		Cadastro		*/
insert into cadastro values(1,"Mario", "mario@gmail.com", 67991295332, 10987612312, "2005-06-10", "Atras do armario",1);
insert into cadastro values(2,"Igor", "igor@gmail.com", 67992913452, 02369612177, "1996-05-14", "Masculino",2);
insert into cadastro values(3,"Josefa", "josefa@gmail.com", 67991295349, 10987612358, "2006-07-12", "Feminino",3);
insert into cadastro values(44,"kelly","lly@hotmail.com",67992913452,02369612177,"1994-04-24","Feminino",4);

/*		Palestra		*/
insert into palestra values(1,"Creative cut-Freestyle livre","Dias Barber", 20, "Workshop para você barbeiro, quer transformar seus cortes de cabelo em uma “obra de arte”? Então você precisa estar neste workshop, aprendendo técnicas diferenciadas e tendências do estilo freestyle. Agregue valor ao seu trabalho e surpreenda o seu cliente!", 306);
insert into palestra values(2, "Modelagem 3D de Personagens", "Gabriel Ferreira Medeiros", 20, "Nesse workshop abordaremos os principais elementos que são essenciais para a modelagem de um personagem estilizado em 3D. Entre os assuntos abordados, veremos coisas como o blocking, o processo de baking, low e high poly, adição de children, retopologia básica, mapeamento UV, princípios da animação e exportação.", 310);
insert into palestra values(3, "Introdução à Robótica com Kit Lego Educacional", "FACOM/UFMS", 20, "Nesta oficina, serão apresentados experimentos com sensores e motores, demonstrando conceitos e a operação básica dos motores e dos principais sensores presentes no Kit Lego Educacional.", 304);
insert into palestra values(4, "Workshop de Inteligência Emocional e Empreendedorismo", "Tiago Paes", 20, "Palestra onde será abordado sobre como compreender as 4 emoções básicas (Medo, Raiva, Alegria e Tristeza) e líder com cada uma delas de maneira positiva, e também sobre as principais características de um empreendedor de sucesso.", 302);
insert into palestra values(5, "Nenhum propósito acontece na zona de conforto", "Katira de Carli", 20, "'Diante ao medo paralisamos, ter medo é bom pois ele nos protege. Porém ele não pode nos parar, pois depois que rompemos essa barreira descobrimos as maravilhas que a vida pode nos proporcionar. As oportunidades estão na nossa frente, basta dar o primeiro passo e sair da zona de conforto rumo ao nosso propósito. Reclamar ou vitimizar não vai resolver nada, foque na solução, afinal somos o timoneiro de nossas vidas!'", 303);
insert into palestra values(6, "Workshop – Introdução ao Revit Architecture", "Jéder Muniz da Silva", 20, "O presente workshop visa apresentar aos participantes um dos importantes softwares ligados ao Building Information Modeling – BIM, ou Modelagem da Informação da Construção. Em laboratório, serão apresentadas as principais ferramentas de desenho, bem como algumas configurações de elementos, como paredes e pisos. A importância da compatibilização será tema fortemente abordado e relembrado, trazendo a visão ampliada nos projetos, fortalecendo os interessados para o mercado de trabalho e busca de aprendizagem mais aprofundada no Revit na Instituição.", 302);
insert into palestra values(7, "Workshop Inteligência Artificial: Vai estar no Controle ou na Plateia?", "Mauricio Escobar Gleizer", 20, "Neste workshop instigante, vamos nos aprofundar no campo dinâmico da Inteligência Artificial (IA) e explorar a questão crucial de como vamos lidar com esse novo mundo. Através de discussões envolventes e uso prático de algumas ferramentas, navegaremos pelo estado atual das tecnologias de IA e seu profundo impacto na vida das pessoas. Para garantir que você não esteja apenas na plateia, mas seja um participante ativo, capacitado para moldar os impactos dessa nova revolução digital - defendendo seu uso responsável e, por fim, garantindo um futuro em que os humanos permaneçam no controle!", 300);
insert into palestra values(8, "Descomplica LinkedIn: Qual o potencial do LinkedIn? Dicas para um Perfil de Sucesso e Estratégias de Recrutamento", "Igor Acosta Albuquerque", 20, "Descomplica LinkedIn: Qual o potencial do LinkedIn? Dicas para um Perfil de Sucesso e Estratégias de Recrutamento” é um workshop envolvente projetado para simplificar o LinkedIn para profissionais e recrutadores. Neste workshop, vamos mergulhar no vasto potencial do LinkedIn como uma plataforma robusta para networking e recrutamento. Vamos fornecer orientações práticas sobre como construir um perfil impressionante que chame a atenção e atraia as oportunidades ideais. Além disso, vamos abordar táticas de recrutamento eficientes na plataforma, auxiliando você a se mover e se beneficiar do mercado de trabalho vibrante do LinkedIn. Venha conosco para liberar a força do LinkedIn e acelerar sua carreira ou empresa.", 299);
insert into palestra values(9, "10 ferramentas de IA pra você fazer 10x mais em menos tempo", "Kenneth Corrêa", 20, "Kenneth Corrêa já testou mais de 300 ferramentas de inteligência artificial e filtrou para você as 10 que eles mais utilizam no dia a dia de suas empresas. Numa palestra mão na massa, você vai aprender a usar essas ferramentas e escrever melhores prompts (e aprender o que é isso, se ainda não sabe).", 298);
insert into palestra values(10, "Demandas da Engenharia de Software no mercado atual", "Kleber Meira Lima", 20, "Nessa palestra, será discutido o uso dos processos utilizados na Engenharia de Software no desenvolvimento de sistemas e aplicativos no âmbito atual. Projetar sistemas vai muito além do que desenvolver código. Está relacionado ao entendimento e comunicação com o cliente, validação e alinhamento com as pessoas. Será discutida a importância desses momentos e o quanto eles estão relacionados com o sucesso do negócio.", 297);
insert into palestra values(11, "Workshop teórico-prático de aplicação de medicamentos injetáveis", "Dra Camila Amato Montalbano", 20, "Nesse workshop os participantes aprendem uma série de conhecimentos e habilidades essenciais relacionadas à administração segura e eficaz de medicamentos por meio de aplicações de injetáveis.", 296);
insert into palestra values(12, "Atendimento Pré-Hospitalar no Ambiente Rodoviário", "Gisele Fernanda da Abreu", 20, "O ambiente rodoviário é propenso a acidentes de trânsito, que muitas vezes resultam em ferimentos graves. Ter habilidades em atendimento pré-hospitalar específicas para esse cenário pode significar a diferença entre a vida e a morte para as vítimas de acidentes rodoviários.", 295);
insert into palestra values(13, "Complicações agudas da diabetes na emergência (Cetoacidose Diabética)", "Dra Thainá Alves", 20, "O objetivo da palestra é expor as complicações agudas na emergência, principalmente a cetoacidose diabética e o estado hiperosmolar hiperglicemico, desde a definição até o tratamento.", 294);
insert into palestra values(14, "A regulamentação na Podologia e o futuro da profissão no Brasil", "Diva Vieira dos Santos Laurindo", 20, "O podólogo precisa fazer parte do processo da regulamentação, pois nossa profissão e muito importante para saúde dos pés da população, mas precisamos regular nossa atividade, para dar segurança ao profissional e para a sociedade.", 293);
insert into palestra values(15, "Protocolo Flash Detox Express", "Paula Tatiana Coelho Novaes", 20, "Flash Detox é um método inovador que alia nanotecnologia, termoterapia e manobras de massagem diferenciadas, com resultados surpreendentes na redução de medidas e celulite já na primeira sessão. Esse tratamento express para o verão conta com dermocosméticos que possuem poderosos princípios ativos formulados para garantir resultados de impacto em curto prazo.", 292);
insert into palestra values(16, "Retenção 30+ Na Extensão De Cílios: Seja Um Profissional Acima Da Média", "Vanessa Medeiros", 20, "Na busca pela entrega de durabilidade nas extensões de cílios, existem fatores que irão ser aliados no quesito RETENÇÃO! Neste workshop você irá aprender o uso correto dos produtos essenciais para a entrega do melhor resultado e conhecer o estudo dos fios de uma maneira revolucionária! Além de conhecer os produtos essenciais para a saúde ocular da sua cliente.", 291);
insert into palestra values(17, "Moda, Estilo E Consumo Consciente", "Lauren Cury", 20, "Levantando a bandeira do consumo consciente, a produtora de moda e proprietária do Gaveta Brechó há mais de 10 anos, Lauren Cury, traz uma reflexão sobre os impactos da indústria da moda e a importância de revermos alguns hábitos na hora da compra.", 290);
insert into palestra values(18, "TAPING NO PÓS CIRÚRGICO ESTÉTICO", "Janaina Mecchi", 20, "O uso do taping dentro e fora do centro cirúrgico, vem se mostrando como um aliado de diversos tratamentos e até mesmo prevenções de intercorrências e complicações do pós operatório de cirurgias plásticas estéticas. Aproveite a oportunidade de começar aplicar ou aprimorar ainda mais suas habilidades com o taping linfático ou compressivo.", 289);
insert into palestra values(19, "A Arte Na Montagem Do Rabo De Cavalo Perfeito: Técnica E Inspiração", "Rodolfo Parangaba", 20, "O rabo de cavalo é um penteado rápido que pode ser casual, elegante, despojado...e ao contrário do que se pensa, é preciso muita técnica e inspiração para sua execução. Venha aprender os segredos da preparação e criação deste penteado que todo bom cabeleireiro deve saber fazer com perfeição!", 288);
insert into palestra values(20, "Moda E Moodboard Digital: Utilizando A Ferramenta Pinterest", "Luciana Duailibe", 20, "Produtores de moda e afins, bora criar? Aprenda como criar um moodboard digital, um painel semântico que contextualiza visualmente o conceito, seu processo criativo e o tema do trabalho de  Moda a ser desenvolvido, utilizando o Pinterest como ferramenta.", 287);
insert into palestra values(21, "Softgel Nails: A Nova Tecnologia No Mundo Das Unhas", "Laiza França Amorim", 20, "Unhas lindas, com a aspecto natural, de maneira rápida e prática. Venha aprender esta técnica que está revolucionando o trabalho das nailsdesigners!", 286);
insert into palestra values(22, "Lançamento do Livro: Comunicação Não Violenta para Mulheres", "Ariane Osshino", 20, "Lançamento do Livro: Comunicação Não Violenta para Mulheres", 285);
insert into palestra values(23, "Oficina prática para Líderes: construindo habilidades eficazes através das peças", "Maria Aparecida de Lima", 20, "Nessa oficina a professora Maria vai mostrar que um ambiente igualitário possibilita experiências práticas de aprendizagem proporcionando que líderes de equipe tenham um olhar para explorar os diferentes tipos de habilidades que são essenciais para integrar equipe, entender suas diferenças, entre outros temas.", 284);
insert into palestra values(24, "Educação Financeira com Pais e Filhos", "Mário Minoru Matsumoto", 20, "Workshop prático para alcançar os objetivos educacionais, profissionais e estabilidade financeira.  Para essa palestra são duas inscrições a serem feitas: do pai e do filho", 283);
insert into palestra values(25, "Gestão e Liderança", "Cláudio Ribas", 20, "Gerenciar é: garantir resultado por meio de outros, liderar é fazer isso de forma duradoura.", 282);



select * from cadastro;
select * from palestra;



delimiter $


create trigger tg_usuarioPalestra after insert
on cadastro
for each row 
begin 
	update palestra set vagas = vagas - 1 where id_pale = new.cad_pale;
end $


delimiter ;