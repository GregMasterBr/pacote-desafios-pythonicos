"""
05. verbing

Dada uma string, se seu tamanho for pelo menos 3,
adicione 'ing' no seu fim, a menos que a string
já termine com 'ing', nesse caso adicione 'ly'.

Se o tamanho da string for menor que 3, não altere nada.

Retorne o resultado da string.
"""

def verbing(s):
    excecao=['visit',]
    # +++ SUA SOLUÇÃO +++
    form_verbing = ''
    if len(s)>2:
        if 'ing' in s:
            form_verbing = s + 'ly'
        else:
            if s[-1]=='e':
                if s[-2] not in 'aeou':
                    form_verbing=s.replace(s[-1],'ing')

                if ('i' in s[-2]):
                    form_verbing = s.replace(s[-2]+s[-1], 'y')+'ing'
                else:
                    form_verbing = s.replace(s[-1],'ing')
            elif (s[-3] not in 'aeiou' and s[-2] in 'aeiou' and  s[-1] not in 'aeiou'): #CVC
                if s in excecao:
                    form_verbing = s + 'ing'
                else:
                    form_verbing = s+s[-1]+'ing'
            else:
                form_verbing = s+'ing'
    else:
        form_verbing=s

    return form_verbing


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(verbing, 'hail', 'hailing')
    test(verbing, 'swiming', 'swimingly')
    test(verbing, 'do', 'do')
    test(verbing, 'make', 'making')
    test(verbing, 'run', 'running')
    test(verbing, 'visit', 'visiting') #excessão -> a última silaba não é tônica
    test(verbing, 'die', 'dying')
    test(verbing, 'lie', 'lying')


