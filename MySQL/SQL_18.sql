select * from tbproduto;

select * from tbproduto where PRECO_LISTA between 16.007 and 16.009;

select * from tbcliente;

select * from tbcliente where IDADE >= 18 and IDADE <= 22 and SEXO = 'M';

select * from tbcliente where CIDADE = ' Rio de Janeiro' or BAIRRO = 'Jardins';