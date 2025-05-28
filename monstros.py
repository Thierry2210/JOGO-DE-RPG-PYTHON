# Lista para armazenar os monstros
lista_monstro = []

# Lista de monstros derrotados
monstros_derrotados = set()

# Conjunto para armazenar nomes já usados
nomes_usados = set()

# Função para criar um monstro
def criar_monstro(tipo, level, multiplicador):
    tipo_formatado = tipo.capitalize().strip()
    nome = f"{tipo_formatado} #{level}"
    
    nomes_usados.add(nome) 
    if tipo_formatado == "Goblin":
        return {
            "nome": f"Goblin #{level}",
            "level": level,
            "dano": int(5 * multiplicador),
            "hp": int(100 * multiplicador),
            "hpMax": int(100 * multiplicador),
            "xp": int(25 * multiplicador)
        }
    elif tipo_formatado == "Orc":
        return {
            "nome": f"Orc #{level}",
            "level": level,
            "dano": int(10 * multiplicador),
            "hp": int(150 * multiplicador),
            "hpMax": int(150 * multiplicador),
            "xp": int(100 * multiplicador)
        }
    elif tipo_formatado == "Dragão":
        return {
            "nome": f"Dragão #{level}",
            "level": level,
            "dano": int(20 * multiplicador),
            "hp": int(200 * multiplicador),
            "hpMax": int(200 * multiplicador),
            "xp": int(250 * multiplicador)
        }
    elif tipo_formatado == "Rei demônio":
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
        
def registrar_derrota(monstro):
    nome = monstro.get("nome")
    if nome:
        if nome in monstros_derrotados:
            print(f"[INFO] O monstro {nome} já foi derrotado anteriormente.")
        else:
            monstros_derrotados.add(nome)
            print(f"[INFO] Monstro {nome} registrado como derrotado.")
    else:
        print("[AVISO] Monstro inválido, não pode registrar derrota.")

        
monstro1 = criar_monstro("Goblin", 1, 1)
monstro2 = criar_monstro("Goblin", 1, 1)  # Vai avisar que já existe e não criar duplicado

# Exibe os monstros criados
def exibir_monstros():
    for monstro in lista_monstro:
        print(
            f"Nome: {monstro['nome']} // Level: {monstro['level']} // Dano: {monstro['dano']} // HP: {monstro['hp']} // EXP: {monstro['xp']}"
        )

# Exibe os tipos únicos criados
def exibir_tipos_monstros():
    tipos = set()
    for monstro in lista_monstro:
        tipo_nome = monstro["nome"].split(" ")[0]
        tipos.add(tipo_nome)
    print("Tipos únicos de monstros criados:", ", ".join(tipos))
