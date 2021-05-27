'''
Escola Técnica Estadual Porto Digital
Data: 21/05/21
Tema: Problemas dentários no Brasil - Case de estudo em Alagoas
'''
import dados
from time import sleep

#! Criação de uma lista
cidades = list(dados.valores)

#! -=-=-=-=-=-=-=-=- MÉTODOS DO TIPO "LISTA" -=-=-=-=-=-=-=-=-

#* Tamanho de uma lista
#  len -> Tamanho (nº. de índices)
# Neste caso, o nº. de índices representa a quantidade de cidades avaliadas
print('1 - Utilizando o método "len" numa lista')
sleep(2)
print(f"Nº. de cidades: {len(cidades)}", flush=True)
sleep(4)

#* Acessar um índice específico
# Neste caso, é limitar a exposição de dados a uma cidade
print('\n2 - Printando os elementos da lista')
sleep(3)
print("-=-=-=-=- Lista cidades -=-=-=-=-")
for i in cidades:
    print(f"- {i[0]}")

sleep(3)

#* Acessar um range numa lista
# Neste exemplo, há o acesso das 4 primeiras cidades
print('\n3 - Printando um range numa lista')
sleep(2)
print(cidades[:4])
sleep(4)

#* Estender uma lista
print('\n4 - Estendendo uma lista')
sleep(2)
novas_cidades = [["Cidade Teste", 0.7]]
cidades.extend(novas_cidades)
print(cidades[-1])
sleep(2)

print('\n5 - Mostrando os gráficos')
sleep(2)
dados.mostrar_graficos()