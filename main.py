from random import randint
import json

# Lista de monstros
lista_monstro = []

# Dados do jogador
jogador = {
    "nome": input("Digite o nome do jogador: "),
    "level": 1,
    "xp": 0,
    "xpMax": 50,
    "hp": 100,
    "hpMax": 100,
    "dano": 25,
    "inventario": {
        "poções": 0,
        "ouro": 100
    }
}

# Funções da loja
def loja():
    print("Bem-vindo à loja!")
    print("1. Comprar Poção (10 ouro)")
    print("2. Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == "1" and jogador['inventario']['ouro'] >= 10:
        jogador['inventario']['poções'] += 1
        jogador['inventario']['ouro'] -= 10
        print("Você comprou uma poção!")
    elif escolha == "1":
        print("Você não tem ouro suficiente!")

# Função para usar poção
def usar_pocao():
    if jogador['inventario']['poções'] > 0:
        jogador['hp'] = min(jogador['hpMax'], jogador['hp'] + 50)
        jogador['inventario']['poções'] -= 1
        print("Você usou uma poção e recuperou 50 HP!")
    else:
        print("Você não tem poções!")

# Função para criar um monstro
def criar_monstro(level):
    tipos = ["Goblin", "Orc", "Dragão"]
    tipo = tipos[randint(0, len(tipos) - 1)]
    novo_monstro = {
        "nome": f"{tipo} #{level}",
        "level": level,
        "dano": int(5 * level * multiplicador),
        "hp": int(100 * level * multiplicador),
        "hpMax": int(100 * level * multiplicador),
        "xp": int(10 * level * multiplicador)
    }
    return novo_monstro

# Função para gerar monstros
def gerar_monstros(n_monstros):
    for x in range(n_monstros):
        novo_monstro = criar_monstro(x + 1)
        lista_monstro.append(novo_monstro)

def exibir_monstros():
    for monstro in lista_monstro:
        print(
            f"Nome: {monstro['nome']} // Level: {monstro['level']} // Dano: {monstro['dano']} // HP: {monstro['hp']} // EXP: {monstro['xp']}"
        )

def exibir_jogador():
    print(
        f"Nome: {jogador['nome']} // Level: {jogador['level']} // Dano: {jogador['dano']} // HP: {jogador['hp']}/{jogador['hpMax']} // EXP: {jogador['xp']}/{jogador['xpMax']}"
    )

def reset_jogador():
    jogador['hp'] = jogador['hpMax']

def reset_monstro(monstro):
    monstro['hp'] = monstro['hpMax']

# Função para subir de nível
def subir_de_nivel():
    if jogador['xp'] >= jogador['xpMax']:
        jogador['level'] += 1
        jogador['xp'] = 0
        jogador['xpMax'] = int(jogador['xpMax'] * 1.5)
        jogador['hpMax'] = int(jogador['hpMax'] * 1.5)
        jogador['hp'] = jogador['hpMax']  # Recupera todo o HP
        print(f"Parabéns! Você subiu para o nível {jogador['level']}!")

# Função para realizar um ataque crítico
def ataque_critico(monstro):
    dano_critico = jogador['dano'] * 2
    monstro['hp'] -= dano_critico
    print(f"Ataque crítico! Você causou {dano_critico} de dano!")

# Função para atacar o monstro com uma habilidade especial
def habilidade_especial(monstro):
    if jogador['level'] >= 3:  # Habilidade disponível a partir do nível 3
        dano_especial = jogador['dano'] * 3
        monstro['hp'] -= dano_especial
        print(f"Você usou uma habilidade especial e causou {dano_especial} de dano!")
    else:
        print("Você ainda não desbloqueou habilidades especiais!")

# Função para iniciar a batalha
def iniciar_batalha(monstro):
    while jogador["hp"] > 0 and monstro["hp"] > 0:
        print("1. Atacar")
        print("2. Defender")
        print("3. Usar Poção")
        escolha = input("Escolha sua ação: ")

        if escolha == "1":
            atacar_monstro(monstro)
        elif escolha == "2":
            jogador['hp'] += 10  # Defesa recupera um pouco de HP
            print("Você se defendeu e recuperou 10 HP!")
        elif escolha == "3":
            usar_pocao()
        else:
            print("Escolha inválida!")

        if monstro["hp"] > 0:
            atacar_jogador(monstro)
        exibir_info_batalha(monstro)

    if jogador['hp'] > 0:
        print(f"O {jogador['nome']} venceu a batalha e ganhou {monstro['xp']} de EXP e 20 ouro!")
        jogador['xp'] += monstro['xp']
        jogador['inventario']['ouro'] += 20  # Recompensa em ouro
        exibir_jogador()
    else:
        print(f"O {monstro['nome']} venceu!!!")

    subir_de_nivel()
    reset_jogador()
    reset_monstro(monstro)

#Funções de atacar
def atacar_monstro(monstro):
    monstro['hp'] -= jogador['dano']

def atacar_jogador(monstro):
    jogador['hp'] -= monstro['dano']

#Função para exibir informações da batalha
def exibir_info_batalha(monstro):
    print(f"Jogador: {jogador['hp']} / {jogador['hpMax']}")
    print(f"Monstro_Atacado: {monstro['nome']} / {monstro['hp']} / {monstro['hpMax']}")
    print("\n")

# Funções para salvar e carregar o jogo
def salvar_jogo():
    with open("save.json", "w") as arquivo:
        json.dump(jogador, arquivo)
    print("Jogo salvo!")

def carregar_jogo():
    global jogador
    with open("save.json", "r") as arquivo:
        jogador = json.load(arquivo)
    print("Jogo carregado!")

def introducao():
    print("Bem-vindo ao mundo de RPG!")
    print("Sua missão é derrotar o Dragão e salvar o reino!")

# Configuração de dificuldade
dificuldade = input("Escolha a dificuldade (fácil, médio, difícil): ").lower()
multiplicador = {"fácil": 0.8, "médio": 1, "difícil": 1.5}[dificuldade]

# Missões
missoes = [{"descricao": "Derrote 3 monstros", "completada": False, "progresso": 0, "objetivo": 3}]

def verificar_missoes():
    for missao in missoes:
        if not missao["completada"] and missao["progresso"] >= missao["objetivo"]:
            missao["completada"] = True
            jogador['inventario']['ouro'] += 50
            print(f"Missão completa! Você ganhou 50 ouro: {missao['descricao']}")

introducao()
gerar_monstros(5)
monstro_selecionado = lista_monstro[0]
print(f"Monstro para atacar: {monstro_selecionado}")
iniciar_batalha(monstro_selecionado)