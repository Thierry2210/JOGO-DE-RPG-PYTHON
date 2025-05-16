# Função para gerar uma lista de monstros
def gerar_monstros(n_monstros, multiplicador, tipo):
    lista_monstro.clear()
    for level in range(1, n_monstros + 1):
        novo_monstro = criar_monstro(tipo, level, multiplicador)
        lista_monstro.append(novo_monstro)

lista_monstro = []

# Função para criar um monstro pelo seu tipo e level
def criar_monstro(tipo, level, multiplicador):
    tipo = tipo.capitalize().strip()
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
        print(f"[AVISO] Tipo de monstro inválido: Algo forte demais para ser mensurado apareceu.")
        return {
            "nome": f"Monstro Desconhecido #{level}",
            "level": 999,
            "dano": 9999,
            "hp": 999999,
            "hpMax": 999999,
            "xp": 999999999,
            "mostrar_stats": False
        }

# Função para exibir os monstros
def exibir_monstros():
    for monstro in lista_monstro:
        print(
            f"Nome: {monstro['nome']} // Level: {monstro['level']} // Dano: {monstro['dano']} // HP: {monstro['hp']} // EXP: {monstro['xp']}"
        )