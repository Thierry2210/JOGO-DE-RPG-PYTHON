historico_acoes = [] # Fila

def registrar_acao(acao):
    historico_acoes.append(acao)
    
def mostrar_historico():
    print("\nHistórico de Ações:")
    i = 1
    while historico_acoes:
        acao = historico_acoes.pop(0)  # remove o último elemento (LIFO)
        print(f"{i}. {acao}")
        i += 1