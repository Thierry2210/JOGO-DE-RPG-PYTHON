from imports import *
from random import randint
from time import sleep
import sys

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
        subcabecalho("Você venceu a batalha!")
        print(f"O {jogador['nome']} venceu a batalha e ganhou {monstro['xp'] * multiplicador} de EXP!\n")
        subir_de_nivel()

    else:
        print(f"O {monstro['nome']} venceu!!!")
        subcabecalho("Você foi derrotado!")
        cabecalho("FIM DE JOGO")
        print("Você não sobreviveu à batalha.")
        subcabecalho("Pressione Enter para sair.")
        input()
        cabecalho("Saindo do jogo...")
        sleep(2)
        limpar()
        sys.exit(0)

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
    jogador['hp'] -= monstro['dano']
    print(f"O {monstro['nome']} atacou você e causou {monstro['dano']} de dano!")

# Função para exibir informações da batalha
def exibir_info_batalha(jogador, monstro):
    subcabecalho("Informações da Batalha")
    print(f"Jogador: HP {jogador['hp']} / {jogador['hpMax']}")
    if monstro.get("mostrar_status", True):
        print(f"Monstro: {monstro['nome']} - HP {monstro['hp']} / {monstro['hpMax']}")
    else:
        print(f"Monstro: {monstro['nome']} - HP ??? / ???")
    print(f"Jogador: HP {jogador['hp']} / {jogador['hpMax']}")