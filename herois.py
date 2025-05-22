from cabecalho_limpar import cabecalho,subcabecalho, limpar
from time import sleep

# Função para criar o jogador com base na classe escolhida
def escolher_classe():
    limpar()
    cabecalho("Escolha sua Classe")
    print("1. Mago (Baixo HP, Maior dano)")
    print("2. Guerreiro (Alto HP, dano equilibrado)")
    print("3. Arqueiro (HP médio ,Dano médio)")
    escolha = input("Digite o número da classe que deseja escolher: ")

    if escolha == "1":
        return {
            "nome": input("Digite o nome do jogador: "),
            "classe": "Mago",
            "level": 1,
            "xp": 0,
            "xpMax": 50,
            "hp": 100,
            "hpMax": 100,
            "dano": 40,
        }
    elif escolha == "2":
        return {
            "nome": input("Digite o nome do jogador: "),
            "classe": "Guerreiro",
            "level": 1,
            "xp": 0,
            "xpMax": 50,
            "hp": 1000,
            "hpMax": 1000,
            "dano": 1000,
        }
    elif escolha == "3":
        return {
            "nome": input("Digite o nome do jogador: "),
            "classe": "Arqueiro",
            "level": 1,
            "xp": 0,
            "xpMax": 50,
            "hp": 150,
            "hpMax": 150,
            "dano": 30,
        }
    else:
        print("Escolha inválida! Tente novamente.")
        sleep(1)
        return escolher_classe()

# # Função para atacar o monstro com uma habilidade especial
# def habilidade_especial(jogador, monstro):
#     if jogador['level'] >= 3:
#         dano_especial = jogador['dano'] * 7
#         monstro['hp'] -= dano_especial
#         print(f"Você usou uma habilidade especial e causou {dano_especial} de dano!")
#     else:
#         print("Você ainda não desbloqueou habilidades especiais!")


# Inicializa o jogador com a classe escolhida
jogador = escolher_classe()

# Função para exibir o jogador
def exibir_jogador(jogador):
    print(
        f"Nome: {jogador['nome']} // Classe: {jogador['classe']} // Level: {jogador['level']} // Dano: {jogador['dano']} // HP: {jogador['hp']}/HpMax: {jogador['hpMax']} // EXP: {jogador['xp']}/XpMax: {jogador['xpMax']}"
    )

def reset_jogador():
    jogador['hp'] = jogador['hpMax']

# Função para subir de nível
def subir_de_nivel():
    while jogador['xp'] >= jogador['xpMax']:
        subcabecalho("\nVocê subiu de nível!")
        jogador['level'] += 1
        jogador['xp'] = 0
        jogador['xpMax'] = int(jogador['xpMax'] * 1.5)
        jogador['hpMax'] = int(jogador['hpMax'] * 1.5)
        jogador['hp'] = jogador['hpMax']
        print(f"Parabéns! Você subiu para o nível {jogador['level']}!")
        print(f"HP máximo: {jogador['hpMax']}")
        print(f"XP máximo: {jogador['xpMax']}")
        print(f"HP atual: {jogador['hp']}")
        print(f"XP atual: {jogador['xp']}")
        print(f"XP necessário para o próximo nível: {jogador['xpMax'] - jogador['xp']}")