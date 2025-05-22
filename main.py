from imports import *
from time import sleep
from historia_goblin import historia_goblins 
from historia_orc import historia_orcs
from historia_dragao import historia_dragao
from historia_rei_demonio import historia_rei_demonio

# Escolhe a dificuldade do jogo
dificuldade = input("Escolha a dificuldade (fácil, médio, difícil): ").lower()
multiplicadores = {"fácil": 1, "médio": 1.5, "difícil": 3}
multiplicador = multiplicadores.get(dificuldade)

if multiplicador is None:
    print("Dificuldade inválida! Usando 'médio' como padrão.")
    multiplicador = 1.5

# Introdução e início da história
cabecalho("Bem-vindo ao Jogo de RPG!")
def introducao():
    limpar()
    cabecalho("Bem-vindo ao jogo de história interativa!")
    print("Você está prestes a embarcar em uma aventura emocionante.")
    print("Suas escolhas moldarão o desenrolar da história.")
    print("Prepare-se para tomar decisões que afetarão o destino do seu personagem.")
    print()
    subcabecalho("SUAS ESCOLHAS TEM CONSEQUÊNCIAS")
    print()
    print("Vamos começar!\n")
    sleep(3)
    return

introducao()

# Função para exibir as informações do jogador
exibir_jogador(jogador)

# Função para iniciar a história com os goblins
# historia_goblins(jogador, multiplicador)

# Função para iniciar a história com os orcs
# historia_orcs(jogador, multiplicador)

# Função para iniciar a história com o dragão
historia_dragao(jogador, multiplicador)

# Função para iniciar a história com o Rei Demônio
# historia_rei_demonio(jogador, multiplicador)