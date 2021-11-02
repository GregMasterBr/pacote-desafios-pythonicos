"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys


# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).


# A função abaixo chama print_words() ou print_top() de acordo com os
# parâmetros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]

    if option == '--count':
        print_words(filename)

    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

def print_words(filename='letras.txt'):
    abcdario =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    arquivo = open(filename)
    arquivo_str = arquivo.read().lower()
    texto_separando_caracteres = list(arquivo_str)
    lista_ocorrência_letras = []
    dicionario_ocorrência_letras = {}

    for letra in abcdario:
        quantidade = texto_separando_caracteres.count(letra)
        if quantidade >0:
            lista_ocorrência_letras.append((letra,quantidade))
            dicionario_ocorrência_letras[letra]= quantidade
            print(letra,quantidade)

    return

def print_top(filename='letras.txt'):
    abcdario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    arquivo = open(filename)
    arquivo_str = arquivo.read().lower()
    texto_separando_caracteres = list(arquivo_str)
    lista_ocorrência_letras = []
    dicionario_ocorrência_letras = {}

    for letra in abcdario:
        quantidade = texto_separando_caracteres.count(letra)
        if quantidade > 0:
            lista_ocorrência_letras.append((letra, quantidade))
            dicionario_ocorrência_letras[letra] = quantidade

    for x,i in enumerate(sorted(dicionario_ocorrência_letras, key=dicionario_ocorrência_letras.get, reverse=True)):
        if x<20:
            print(i, dicionario_ocorrência_letras[i])
    return

if __name__ == '__main__':
    main()
    #print_words('alice.txt')
    #print_top('alice.txt')

    #13_wordcount.py --count nome_do_arquivo
    #13_wordcount.py --topcount nome_do_arquivo

