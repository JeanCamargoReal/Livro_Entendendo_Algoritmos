"""
* Recursão é quando uma função chama a si mesma.

* Quando você escreve uma função recursiva, deve informar quando a
recursão deve parar. É por isso que toda função recursiva tem duas
partes:
o caso-base e o caso recursivo.
O caso recursivo é quando a função chama a si mesma. O caso-base é
quando a função não chama a si mesma novamente, de forma que o
programa não se torna um loop infinito.
"""


def regressiva(i):
    print(i)
    if i <= 1:  # Caso-base
        return
    else:  # Caso Recursivo
        regressiva(i - 1)


regressiva(10)
