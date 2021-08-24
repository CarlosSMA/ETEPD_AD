'''
Escola Técnica Estadual Porto Digital
Recife, 21/08/21
Matéria: Análise de Dados
Professor: Cloves Rocha
Devs: Carlos Alvarez & Jorge Freitas
Turma: 3ºA
'''

import psycopg2

#! Ligação com banco de dados
conexao = psycopg2.connect(database="consultorio", user="postgres", password="1234", host="0.0.0.0", port=5432)
cursor = conexao.cursor()

# Execução do script
# Fonte: https://stackoverflow.com/questions/17261061/execute-sql-schema-in-psycopg2-in-python
# Leitura do arquivo .sql exportado a partir da plataforma https://dbdiagram.io
try:
    cursor.execute(open("db/db_bom_dente.sql").read())
    conexao.commit()
    pass
except:
    pass

# Prompt de comandos do usuário
while True:

    # Inserir os comandos & sair caso desejado
    comando = input("Insira um comando\n> ")
    if comando == "quit" or comando == "exit":
        break

    # Checar por erros de sintaxe
    try:
        cursor.execute(comando)
        pass
    except psycopg2.errors.SyntaxError:
        print(f"Comando \"{comando}\" inválido.")
        pass

    # Salvar as alterações
    conexao.commit()

# Fechar a conexão antes de sair
cursor.close()
conexao.close()
