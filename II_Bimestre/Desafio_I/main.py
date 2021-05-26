'''
Escola Técnica Estadual Porto Digital
Data: 21/05/21
Tema: Problemas dentários no Brasil - Case de estudo em Alagoas
'''
from pandas.core.accessor import CachedAccessor
import dados

#! Criação de uma lista
cidades = list(dados.valores)

#! -=-=-=-=-=-=-=-=- MÉTODOS DO TIPO "LISTA" -=-=-=-=-=-=-=-=-

# len -> Tamanho (nº. de índices)
# Neste caso, o nº. de índices representa a quantidade de cidades avaliadas
print(len(cidades))

# Acessar um índice específico
# Neste caso, é limitar a exposição de dados a uma cidade
print("-=-=-=-=- Lista cidades -=-=-=-=-")
for i in cidades:
    print(i[0], flush=True)
