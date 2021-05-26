'''
Escola Técnica Estadual Porto Digital
Data: 21/05/21
Tema: Problemas dentários no Brasil - Case de estudo em Alagoas
'''
from pandas.core.accessor import CachedAccessor
import dados
from time import sleep

#! Criação de uma lista
cidades = list(dados.valores)

#! -=-=-=-=-=-=-=-=- MÉTODOS DO TIPO "LISTA" -=-=-=-=-=-=-=-=-

# len -> Tamanho (nº. de índices)
# Neste caso, o nº. de índices representa a quantidade de cidades avaliadas
print(len(cidades))
sleep(2)

# Acessar um índice específico
# Neste caso, é limitar a exposição de dados a uma cidade
print("-=-=-=-=- Lista cidades -=-=-=-=-")
for i in cidades:
    print(f"- {i[0]}")

sleep(2)

# Acessar um range numa lista
# Neste exemplo, há o acesso das 4 primeiras cidades
print(cidades[:4])
sleep(2)

