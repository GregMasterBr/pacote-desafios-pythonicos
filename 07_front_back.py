"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
def front_back(a, b):
    # +++ SUA SOLUÇÃO +++
    tamanho_a = len(a)
    tamanho_b = len(b)

    eh_par_a = (True if tamanho_a % 2 == 0 else False)
    eh_par_b = (True if tamanho_b % 2 == 0 else False)

    if eh_par_a:
        metade = int(tamanho_a/2)
        primeira_metade_a = a[:metade]
        segunda_metade_a  = a[metade:tamanho_a+1]
    else:
        metade = int(tamanho_a / 2)
        primeira_metade_a = a[:metade+1]
        segunda_metade_a  = a[metade+1:tamanho_a + 1]

    if eh_par_b:
        metade = int(tamanho_b/2)
        primeira_metade_b = b[:metade]
        segunda_metade_b  = b[metade:tamanho_b+1]
    else:
        metade = int(tamanho_b / 2)
        primeira_metade_b = b[:metade+1]
        segunda_metade_b  = b[metade+1:tamanho_b + 1]


    return primeira_metade_a+ primeira_metade_b+segunda_metade_a+segunda_metade_b


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
