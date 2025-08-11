'''
Conceitos básicos de Inteligência Artificial. Pequenos experimentos de IA sem uso de frameworks para demonstrar princípios fundamentais.

Aqui será feita uma demonstração de busca linear em pyhton puro.

- Implementar um algoritmo de busca linear para encontrar alvos em uma lista:

Argumentos:
    lista, alvo.

Retornos: 
    se encontrado, índice;
    se não, -1.

O programa busca dois alvos: 
    um alvo que existe dentro da lista (alvo_existente);
    e um alvo que não existe (alvo_nao_existente)

A função busca_linear percorre a lista até o tamanho total dela verificando se há algum índice igual à variável existente e nao existente, retornando o valor dela (se encontrar)  e -1 (se não encontrar), respectivamente

'''

def busca_linear(lista, alvo):

    for i in range(len(lista)):
        if lista[i] == alvo:
            return i 
    return -1

numeros = [10, 5, 2, 8, 12, 3]

alvo_existente = 8
alvo_nao_existente = 100

indice_existente = busca_linear(numeros, alvo_existente)
indice_nao_existente = busca_linear(numeros, alvo_nao_existente)

print(f'Lista de números: {numeros}')
print(f'Buscando por {alvo_existente}: Índice {indice_existente}')
print(f'Buscando por {alvo_nao_existente}: Índice {indice_nao_existente}')