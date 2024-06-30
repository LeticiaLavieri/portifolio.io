ALTER TABLE creditoSQL RENAME COLUMN c1 TO idade;
ALTER TABLE creditoSQL RENAME COLUMN c2 TO sexo;
ALTER TABLE creditoSQL RENAME COLUMN c3 TO dependentes;
ALTER TABLE creditoSQL RENAME COLUMN c4 TO escolaridade;
ALTER TABLE creditoSQL RENAME COLUMN c5 TO estado_civil;
ALTER TABLE creditoSQL RENAME COLUMN c6 TO salario_anual;
ALTER TABLE creditoSQL RENAME COLUMN c7 TO tipo_cartao;
ALTER TABLE creditoSQL RENAME COLUMN c8 TO qnt_produtos;
ALTER TABLE creditoSQL RENAME COLUMN c9 TO iteracoes_12m;
ALTER TABLE creditoSQL RENAME COLUMN c10 TO meses_inativo_12m;
ALTER TABLE creditoSQL RENAME COLUMN c11 TO limite_credito;
ALTER TABLE creditoSQL RENAME COLUMN c12 TO valor_transacoes_12m;
ALTER TABLE creditoSQL RENAME COLUMN c13 TO qtd_transacoes_12m;


SELECT 
	COUNT(*) AS Quantidade_linhas
FROM creditoSQL;


SELECT *
FROM creditoSQL
LIMIT 10;


SELECT DISTINCT escolaridade FROM creditoSQL;
SELECT DISTINCT estado_civil FROM creditoSQL;
SELECT DISTINCT salario_anual FROM creditoSQL;
SELECT DISTINCT tipo_cartao FROM creditoSQL;


SELECT 
    COUNT(*) AS Quantidade, salario_anual
FROM creditoSQL
    GROUP BY salario_anual;
    
SELECT 
	COUNT(*) AS Quantidade_clientes, 
    sexo 
FROM creditoSQL 
GROUP BY sexo;


SELECT 
	COUNT(*) AS Quantidade,
	sexo,
	salario_anual
FROM creditoSQL
GROUP BY sexo,
	salario_anual;


SELECT 
	MIN(idade) AS idade_minima,
	MAX(idade) AS idade_maxima
FROM creditoSQL;


SELECT 
    MAX(limite_credito) AS limite_maximo,
    escolaridade,
    tipo_cartao,
    sexo
FROM creditoSQL 
WHERE
    escolaridade != 'na' AND 
    tipo_cartao != 'na'
GROUP BY 
    escolaridade,
    tipo_cartao,
    sexo 
ORDER BY 
    limite_maximo DESC LIMIT 10;


SELECT
    MAX(limite_credito) AS limite_minimo,
    escolaridade,
    tipo_cartao,
    sexo 
FROM creditoSQL
WHERE escolaridade != 'na' AND tipo_cartao != 'na' 
GROUP BY 
    escolaridade, 
    tipo_cartao,
    sexo 
ORDER BY limite_minimo ASC LIMIT 10;