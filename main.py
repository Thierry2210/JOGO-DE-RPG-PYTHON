from herois import escolher_classe, exibir_jogador  # Importa funções do herois.py
from monstros import gerar_monstros, lista_monstro  # Importa funções do monstros.py
from historia import introducao, historia  # Importa funções do historia.py
from batalha import iniciar_batalha  # Importa funções do batalha.py
from cabecalho_limpar import cabecalho, limpar  # Importa funções do cabecalho_limpar.py

# Inicializa o jogador com a classe escolhida
jogador = escolher_classe()

# Escolhe a dificuldade do jogo
dificuldade = input("Escolha a dificuldade (fácil, médio, difícil): ").lower()
multiplicadores = {"fácil": 0.8, "médio": 1, "difícil": 1.5}
multiplicador = multiplicadores.get(dificuldade)

if multiplicador is None:
    print("Dificuldade inválida! Usando 'médio' como padrão.")
    multiplicador = 1


# Introdução e início da história
cabecalho("Bem-vindo ao Jogo de RPG!")
introducao()
cabecalho("Informações do Jogador")
exibir_jogador(jogador)
cabecalho("Início da História")

# História interativa
limpar()
tipo_monstro = historia(jogador)

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
    dano_critico = jogador['dano'] * 3
    monstro['hp'] -= dano_critico
    print(f"Ataque crítico! Você causou {dano_critico} de dano!")

# Gera os monstros com base na dificuldade escolhida
gerar_monstros(5, multiplicador)

# Seleciona o monstro com base na história
monstro_selecionado = None
for monstro in lista_monstro:
    if monstro["nome"].startswith(tipo_monstro):
        monstro_selecionado = monstro
        break

limpar()
if monstro_selecionado:
    print(f"Monstro para atacar: {monstro_selecionado}")
    iniciar_batalha(jogador, monstro_selecionado, multiplicador)
else:
    print("Nenhum monstro correspondente foi encontrado!")