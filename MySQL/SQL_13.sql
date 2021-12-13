use sucos;

alter table tbcliente add primary key (CPF);

alter table tbcliente add column (DATA_NASCIMENTO date);

insert into tbcliente(
CPF, NOME, ENDERECO1, ENDERECO2, BAIRRO, CIDADE, ESTADO, CEP, IDADE,
SEXO, LIMITE_CREDITO, VOLUME_COMPRA, PRIMEIRA_COMPRA, DATA_NASCIMENTO)
VALUES('00388934505', 'João da Silva', 'Rua projetada A número 10', '',
'VILA ROMAN', 'CARATINGA', 'AMAZONAS', '22222222', 30, 'M', 10000.00, 
2000,0,'1989-10-05');

select * from tbcliente;