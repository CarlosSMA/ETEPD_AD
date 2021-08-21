'''
Escola Técnica Estadual Porto Digital
Recife, 21/08/21
Matéria: Análise de Dados
Professor: Cloves Rocha
Devs: Carlos Alvarez & Jorge Freitas
Turma: 3ºA
'''

import psycopg2

# Leitura do arquivo .sql exportado a partir da plataforma https://dbdiagram.io
db_bom_dente_temp = open("db_bom_dente.sql")
db_bom_dente = db_bom_dente_temp.read()

comandos = db_bom_dente.split(';')
print(comandos)

# Loop para executar os comandos do script (criação de tabelas, ligação, etc)
for execucao in comandos:
    c.execute(comandos)