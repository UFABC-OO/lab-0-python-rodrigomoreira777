class OlaUfabc:
    'Classe para imprimir um "Hello World"'
    pass

    def imprime(*self):
        'Metodo que imprime um "Hello World"'
        return f'Sou UFABC!'


def teste_imprime():
    assert OlaUfabc.imprime() == 'Sou UFABC!'


teste = OlaUfabc
print(teste.imprime())


