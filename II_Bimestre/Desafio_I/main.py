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

print(f"Nº. de cidades: {len(cidades)}", flush=True)
sleep(4)

#* Acessar um índice específico
# Neste caso, é limitar a exposição de dados a uma cidade
print("-=-=-=-=- Lista cidades -=-=-=-=-")
for i in cidades:
    print(f"- {i[0]}")

sleep(4)

#* Acessar um range numa lista
# Neste exemplo, há o acesso das 4 primeiras cidades
print(cidades[:4])
sleep(4)

#* Estender uma lista
novas_cidades = [["Cidade Teste", 0.7]]
cidades.extend(novas_cidades)
print(cidades[-1])