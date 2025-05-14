# Função para gerar uma lista de monstros
def gerar_monstros(n_monstros, multiplicador):
    lista_monstro.clear()
    for level in range(1, n_monstros + 1):
        novo_monstro = criar_monstros_por_tipo(level, multiplicador)
        lista_monstro.append(novo_monstro)

lista_monstro = []

# Função para criar um monstro pelo seu tipo e level
def criar_monstro(tipo, level, multiplicador):
    if tipo == "Goblin":
        return {
            "nome": f"Goblin #{level}",
            "level": level,
            "dano": int(5 * multiplicador),
            "hp": int(100 * multiplicador),
            "hpMax": int(100 * multiplicador),
            "xp": int(25 * multiplicador)
        }
    elif tipo == "Orc":
        return {
            "nome": f"Orc #{level}",
            "level": level,
            "dano": int(10 * multiplicador),
            "hp": int(150 * multiplicador),
            "hpMax": int(150 * multiplicador),
            "xp": int(100 * multiplicador)
        }
    elif tipo == "Dragão":
        return {
            "nome": f"Dragão #{level}",
            "level": level,
            "dano": int(20 * multiplicador),
            "hp": int(200 * multiplicador),
            "hpMax": int(200 * multiplicador),
            "xp": int(250 * multiplicador)
        }
    elif tipo == "Rei Demônio":
        return {
            "nome": f"Rei Demônio #{level}",
            "level": level,
            "dano": int(50 * multiplicador),
            "hp": int(500 * multiplicador),
            "hpMax": int(500 * multiplicador),
            "xp": int(500 * multiplicador)
        }
    else:
        print("Não foi encontrado nenhum monstro no seu caminho, pode se preparar para a batalha que irá vir a seguir")

tipo1 = "Goblin"

# Função para gerar monstros por tipo
def criar_monstros_por_tipo(level, multiplicador):
    tipos = ["Goblin", "Orc", "Dragão", "Rei Demônio"]
    tipo = tipo1
    return criar_monstro(tipo, level, multiplicador)

# Função para exibir os monstros
def exibir_monstros():
    for monstro in lista_monstro:
        print(
            f"Nome: {monstro['nome']} // Level: {monstro['level']} // Dano: {monstro['dano']} // HP: {monstro['hp']} // EXP: {monstro['xp']}"
        )