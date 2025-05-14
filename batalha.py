from random import randint
from cabecalho_limpar import cabecalho, subcabecalho, limpar

# Função para iniciar a batalha
def iniciar_batalha(jogador, monstro, multiplicador):
    limpar()
    cabecalho("Início da Batalha")
    subcabecalho(f"Você encontrou um {monstro['nome']}!")
    print(f"HP do {monstro['nome']}: {monstro['hp']} / {monstro['hpMax']}")
    print(f"HP do {jogador['nome']}: {jogador['hp']} / {jogador['hpMax']}")
    while jogador["hp"] > 0 and monstro["hp"] > 0:
        print("1. Atacar")
        print("2. Defender")
        escolha = input("Escolha sua ação: ")

        if escolha == "1":
            atacar_monstro(jogador, monstro)
        elif escolha == "2":
            jogador['hp'] += 10  # Defesa recupera um pouco de HP
            print("Você se defendeu e recuperou 10 HP!")
        else:
            print("Escolha inválida!")

        if monstro["hp"] > 0:
            atacar_jogador(jogador, monstro)
        exibir_info_batalha(jogador, monstro)

    if jogador['hp'] > 0:
        jogador['xp'] += monstro['xp'] * multiplicador
        print(f"O {jogador['nome']} venceu a batalha e ganhou {monstro['xp']} de EXP!")
    else:
        print(f"O {monstro['nome']} venceu!!!")

# Função para atacar o monstro
def atacar_monstro(jogador, monstro):
    chance_critico = randint(1, 100)
    if chance_critico <= 20:
        dano_critico = jogador['dano'] * 2
        monstro['hp'] -= dano_critico
        print(f"Ataque crítico! Você causou {dano_critico} de dano!")
    else:
        monstro['hp'] -= jogador['dano']
        print(f"Você causou {jogador['dano']} de dano!\n")

# Função para atacar o jogador
def atacar_jogador(jogador, monstro):
    print("==============================\n")
    jogador['hp'] -= monstro['dano']
    print(f"O {monstro['nome']} atacou você e causou {monstro['dano']} de dano!")

# Função para exibir informações da batalha
def exibir_info_batalha(jogador, monstro):
    subcabecalho("Informações da Batalha")
    print(f"Jogador: HP {jogador['hp']} / {jogador['hpMax']}")
    print(f"Monstro: {monstro['nome']} - HP {monstro['hp']} / {monstro['hpMax']}")
    print("==============================\n")