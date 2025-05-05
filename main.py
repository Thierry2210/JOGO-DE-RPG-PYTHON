from random import randint

lista_monstro = []

# nome_jogador = input("Digite o nome do jogador: ")

jogador = {
    "nome": input("Digite o nome do jogador: "),
    "level": 1,
    "xp": 0,
    "xpMax": 50,
    "hp": 100,
    "hpMax": 100,
    "dano": 25 
}

def criar_monstro(level):
    novo_monstro = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hpMax": 100 * level,
        "xp": 10 * level
    }
    return novo_monstro

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

def subir_de_nivel():
    if jogador['xp'] >= jogador['xpMax']:
        jogador['level'] += 1
        jogador['xp'] = 0
        jogador['xpMax'] *= 1.5
        jogador['hpMax'] *= 1.5

def iniciar_batalha(monstro):
    while jogador["hp"] > 0 and monstro["hp"] > 0:
        atacar_monstro(monstro)
        atacar_jogador(monstro)
        exibir_info_batalha(monstro)

    if jogador['hp'] > 0:
        print(f"O {jogador['nome']} venceu a batalha e ganhou {monstro['xp']} de EXP")
        jogador['xp'] += monstro['xp']
        exibir_jogador()
    else:
        print(f"O {monstro['nome']} venceu!!!")
        exibir_monstros(monstro)

    subir_de_nivel()
    reset_jogador()
    reset_monstro(monstro)

def atacar_monstro(monstro):
    monstro['hp'] -= jogador['dano']

def atacar_jogador(monstro):
    jogador['hp'] -= monstro['dano']

def exibir_info_batalha(monstro):
    print(f"Jogador: {jogador['hp']} / {jogador['hpMax']}")
    print(f"Monstro_Atacado: {monstro['nome']} / {monstro['hp']} / {monstro['hpMax']}")
    print("\n")


gerar_monstros(5)
# exibir_monstros()

monstro_selecionado = lista_monstro[0]

print(f"Monstro para atacar: {monstro_selecionado}")
iniciar_batalha(monstro_selecionado)
iniciar_batalha(monstro_selecionado)
iniciar_batalha(monstro_selecionado)
iniciar_batalha(monstro_selecionado)
iniciar_batalha(monstro_selecionado)
iniciar_batalha(monstro_selecionado)