-- Criação do Banco de Dados
create database LocadoraVeiculos;

-- Seleção do Banco de Dados
use LocadoraVeiculos;

-- Tabela Cliente
create table cliente(
	idCliente int primary key not null,
	CPF varchar(20) not null,
    nome varchar(50) not null,
	telefone varchar(20) not null,
	email varchar(50) not null,
    endereco varchar(100) not null
);

-- Tabela Pagamento
create table pagamento(
	idPagamento int primary key not null,
    forma enum ('Cartão','Pix','Dinheiro') not null,
    dataPagamento date not null,
    valorTotal decimal (7,2) not null,
    estado enum ('Pago','Pendente') not null
);

-- Tabela Locação
create table locacao(
	idLocacao int primary key not null,
    idCliente int not null,
    idPagamento int not null,
    dataInicio date not null,
    dataFim date not null,
    constraint FkCliente foreign key (idCliente) references cliente(idCliente),
	constraint FkPagamento foreign key (idPagamento) references pagamento(idPagamento)
);

-- Tabela Veículo
create table veiculo(
	idVeiculo int primary key not null,
    modelo varchar(50) not null,
    marca varchar(50) not null,
    ano int not null,
    placa varchar(10) not null,
    valorDiaria decimal (7,2) not null,
    estado enum ('Disponível', 'Alugado', 'Manutenção') not null
);

-- Tabela Locação de Veículos
create table LocacaoVeiculo(
	idLocacao int primary key not null,
    idVeiculo int not null,
    foreign key (idLocacao) references locacao(idLocacao),
    foreign key (idVeiculo) references veiculo(idVeiculo)
);

-- Tabela Manutenção
create table manutencao(
	idManutencao int primary key not null,
    idVeiculo int not null,
    descricao varchar(100) not null,
    dataManutencao date not null,
    custo decimal (7,2) not null,
    constraint FkVeiculo foreign key (idVeiculo) references veiculo(idVeiculo)
);

-- Valor Total Arrecadado
select sum(valortotal) as 'Valor Total Arrecadado' from pagamento
where estado = 'Pago';

-- Consulta da Tabela Manutenção
select descricao, dataManutencao, custo from manutencao;

select idveiculo, modelo, marca from veiculo;
select distinct * from locacaoveiculo;

-- Consulta decrescente do número de alugueis
select veiculo.idveiculo, modelo, marca, count(*) from veiculo
inner join locacaoveiculo
on veiculo.idveiculo = locacaoveiculo.idveiculo
group by idveiculo
order by count(*) desc;

-- Consulta de Pagamentos Pendentes
select idlocacao, cliente.nome, pagamento.valortotal from locacao
inner join cliente on locacao.idcliente = cliente.idcliente
inner join pagamento on locacao.idpagamento = pagamento.idpagamento
where estado = 'Pendente'
group by idlocacao
order by cliente.nome asc;


select * from pagamento
where estado = 'Pendente';

select * from locacao;

use LocadoraVeiculos;