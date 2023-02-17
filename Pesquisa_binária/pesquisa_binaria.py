"""
Pesquisa Binária

- A pesquisa binária é um algoritmo. Sua entrada é uma lista ordenada de elementos.
Se o elemento que você está buscando está na lista, a pesquisa binária retorna a
sua localização. Caso contrário, a pesquisa binária retorna None.

- Com a pesquisa binária, você chuta um número intermediário e elimina a metade dos
números restantes a cada vez.

- A cada estapa da pesquisa binária, você elimina o número de palavras pela metade
até que só reste uma palavra.

- De maneira geral, para uma lista de n números, a pesquisa binária precisa de log2n
para retornar o valor correto, enquanto a pesquisa simples precisa de n etapas.

- A pesquisa binária só funciona quando a sua lista está ordenada.
"""

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        chute = lista[meio]
        
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3)) # => 1
print(pesquisa_binaria(minha_lista, -1)) # => None