from imports import subcabecalho, gerar_monstros, lista_monstro, iniciar_batalha
from time import sleep

# Função de escolha robusta
def escolha_opcao(pergunta, opcoes_validas):
    while True:
        escolha = input(pergunta).strip()
        if escolha in opcoes_validas:
            return escolha
        else:
            print("Escolha inválida! Tente novamente.")

def historia_dragao(jogador, multiplicador):
    subcabecalho("Retorno do Dragão")
    print("Você continua sua jornada, deixando as terras dos orcs para trás.")
    print("Depois de dias vagando, encontra uma caverna escondida entre as montanhas.")
    print("Dentro, você nao sabe como, mas sente uma presença sinistra.")
    sleep(3)
    print("Devido a isso você decide entrar na caverna.")
    print("Ao entrar, você se depara com um dragão majestoso, mas ferido.")
    print("Ele é o mesmo dragão que voce se deparou no começo de sua jornada.")
    sleep(3)
    print("Você é observado por seus olhos cansados, mas ainda cheios de sabedoria.")
    print("Porém esses olhos duram pouco, em instantes eles começam a brilhar com uma luz púrpura sinistra.")
    print("Seus movimentos ficam mais trêmulos, como se estivesse lutando contra algo dentro de si.")
    sleep(3)
    print("O dragão te encara e com uma voz fraca diz:")
    print("\"Guerreiro... eu não consegui resistir... a escuridão tomou conta...\"")
    print("\"Por favor... me liberte... mate-me antes que eu perca o controle completamente.\"")
    sleep(3)

    print("\nVocê sabe que não há outra opção. O dragão está além da salvação.")
    print("Mesmo após tantas batalhas frias, você sente um aperto no coração.")
    print("Você hesita, mas sabe que deve agir.")
    print("Você não pode deixar que a escuridão consuma o dragão, mesmo que isso signifique lutar contra ele.")
    print("A batalha final contra uma das criatura mais fortes a pisar neste mundo está prestes a começar.")
    sleep(3)

    batalha_dragao(jogador, multiplicador)

def batalha_dragao(jogador, multiplicador):
    subcabecalho("BATALHA CONTRA O DRAGÃO CORROMPIDO")
    sleep(2)

    print("1. Lutar com tudo que você tem")
    print("2. Tentar conversar mais (ALTO RISCO)")
    acao = escolha_opcao("Escolha sua ação: ", ["1", "2"])
    print()

    if acao == "1":
        print("Você ergue sua arma e avança com determinação.")
        print("O dragão ruge, e a batalha começa com um estrondo!")
        print("Você sente a força da escuridão, mas também a luz que brilha dentro de você.")
        sleep(2)
        gerar_monstros(1, multiplicador, "Dragão")
        for monstro in lista_monstro:
            if jogador['hp'] > 0:
                iniciar_batalha(jogador, monstro, multiplicador)
            else:
                print("Você foi derrotado pelo dragão corrompido.")
                return

    if acao == "2":
        print("Você tenta alcançá-lo com palavras, buscando resquícios de sua antiga alma.")
        print("O dragão hesita por um segundo... mas então ruge com fúria, perdendo o controle.")
        print("Agora, ele ataca com toda a força da escuridão. Você deve lutar!")
        jogador['hp'] = int(jogador['hpMax'] * 0.8)
        print(f"Seu HP foi drasticamente reduzido para {jogador['hp']}!")
        gerar_monstros(1, multiplicador, "Dragão")
        for monstro in lista_monstro:
            if jogador['hp'] > 0:
                iniciar_batalha(jogador, monstro, multiplicador)
            else:
                print("Você foi derrotado pelo dragão corrompido.")
                return

    print("\nCom um último golpe, você perfura o coração do dragão.")
    print("Ele solta um rugido, que logo se torna um sussurro de alívio.")
    print("\"Obrigado...\" — ele diz, antes de se desfazer em cinzas e luz.")
    sleep(3)
    print("Você cai de joelhos, exausto e com lágrimas nos olhos.")
    print("A escuridão foi derrotada, mas o custo foi alto.")
    print("Ainda assim, você se levanta. Sua jornada ainda não terminou.")
    sleep(3)
