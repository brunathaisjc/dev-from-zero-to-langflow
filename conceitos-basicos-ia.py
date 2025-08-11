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

print(f'\nLista de números: {numeros}')
print(f'Buscando por {alvo_existente}: Índice {indice_existente}')
print(f'Buscando por {alvo_nao_existente}: Índice {indice_nao_existente}')

# Regras simples em Python

def classificar_num(numero):
    """
    Classificar em 'pequeno', 'médio' ou 'grande'.
    Argumentos:

    Retornos: 


    """
    if numero < 10:
        return "pequeno"
    elif numero <= 10:
        return "medio"
    elif numero <= 50:
        return "medio"
    else:
        return "grande"
    
num1 = 13
num2 = 2
num3 = 60
num4 = 50
num4 = 4

print(f"\nClassificando {num1}: {classificar_num(num1)}")
print(f"Classificando {num2}: {classificar_num(num2)}")
print(f"Classificando {num3}: {classificar_num(num3)}")
print(f"Classificando {num4}: {classificar_num(num4)}\n")
