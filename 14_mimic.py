"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys
from collections import defaultdict

def ler_arquivo_gerar_lista(filename):
  with open(filename) as arq:
        lista_palavras = arq.read().lower().split()
  return lista_palavras
  

def mimic_dict(filename):
  """Retorna o dicionario imitador mapeando cada palavra para a lista de
  palavras subsequentes."""
  dicionario = defaultdict(list)
  mimic_lista = ler_arquivo_gerar_lista(filename)

  for chave, valor in zip(mimic_lista, mimic_lista[1:]):
    dicionario[chave].append(valor)
  dicionario[mimic_lista[-1]] = ['']
  dicionario[''].append(mimic_lista[0])
  return dicionario


def print_mimic(mimic_dict, word):
  """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
  texto_lero_lero = ''

  for i in range (200):
    palavra_aleatoria = random.choice(mimic_dict[word])
    texto_lero_lero = ' '.join((texto_lero_lero, palavra_aleatoria))
    word = palavra_aleatoria
    
  print(texto_lero_lero)
  return texto_lero_lero

# Chama mimic_dict() e print_mimic()
def main():
  if len(sys.argv) != 2:
    print('Utilização: ./14_mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
