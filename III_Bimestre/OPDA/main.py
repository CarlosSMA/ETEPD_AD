'''
Escola Técnica Estadual Porto Digital
Recife, 21/08/21
Matéria: Análise de Dados
Professor: Cloves Rocha
Devs: Carlos Alvarez & Jorge Freitas
Turma: 3ºA
'''

'''
TODO
- Troubleshooting geral
'''

import psycopg2

#! Ligação com banco de dados
conexao = psycopg2.connect(user="postgres", password="1234", host="0.0.0.0", port=5432)
cursor = conexao.cursor()

# Execução do script
# Fonte: https://stackoverflow.com/questions/17261061/execute-sql-schema-in-psycopg2-in-python
# Leitura do arquivo .sql exportado a partir da plataforma https://dbdiagram.io
cursor.execute(open("db/db_bom_dente.sql", "r").read())