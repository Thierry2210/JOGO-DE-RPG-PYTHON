def linha(tam = 75):
    return '=' * tam

def linha2(tam = 75):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(75))
    print(linha())

def subcabecalho(txt):
    print(linha2())
    print(txt.center(75))
    print(linha2())
    
def limpar():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')