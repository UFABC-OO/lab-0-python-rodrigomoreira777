class OlaUfabc:
    'Classe para implementar um "Hello World"'
    pass

    def imprime(self):
        'Metodo que imprime um "Hello World"'
        ola = 'Olá Mundo!'
        return ola


teste = OlaUfabc


def test_imprime():
    assert OlaUfabc.imprime(teste) == 'Olá Mundo!'
