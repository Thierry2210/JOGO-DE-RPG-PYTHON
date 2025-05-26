from imports import *
from time import sleep

def historia_rei_demonio(jogador, multiplicador):
    subcabecalho("\033[1;35mO Trono das Sombras\033[0m")
    print("Você caminha por terras esquecidas, onde até o vento parece sussurrar lamentos antigos.")
    print("Ao longe, uma fortaleza negra ergue-se entre montanhas escuras como carvão.")
    print("Você sente que seu destino te chama... o Rei Demônio o aguarda.")
    sleep(4)

    print("\nAo adentrar a fortaleza, o ar se torna denso, quase impossível de respirar.")
    print("Salões gigantescos e corredores tomados por sombras se estendem infinitamente.")
    print("Você sente os olhos da escuridão te observando.")
    sleep(3)

    print("\nNo centro da sala do trono, sentado com imponência, está ele.")
    print("O Rei Demônio, envolto em uma armadura viva que pulsa como carne corrompida.")
    print("Seus olhos brilham com chamas roxas e seu sorriso é o de quem conhece todos os seus medos.\n")
    sleep(4)

    print("\033[35mRei Demônio: \"Então é você... o verme que ousou matar meu dragão.\"")
    print("Rei Demônio: \"Por eras assisti sua raça rastejar por essas terras. Sempre tão fraca... tão previsível.\"")
    print("Rei Demônio: \"Mas você... você causou problemas demais.\"\033[0m")
    sleep(3)

    print("\n\033[36mVocê: \"Eu lutei para proteger o que restou deste mundo. Não me arrependo de nada.\"\033[35m\n")
    print("Rei Demônio: \"Coragem? Ou tolice?\"\033[0m — ele se levanta, e o chão treme sob seus pés.\033[35m")
    print("Rei Demônio: \"Venha então, herói. Mostre-me o que o último tolo da sua espécie pode fazer.\"\033[0m")
    sleep(4)

    batalha_rei_demonio(jogador, multiplicador)

def batalha_rei_demonio(jogador, multiplicador):
    subcabecalho("\033[1;35mBATALHA FINAL — REI DEMÔNIO\033[0m")
    sleep(2)

    print("1. Enfrentar o Rei Demônio de frente.")
    print("2. Provocar o Rei Demônio (RISCO + RECOMPENSA).")
    acao = input("Escolha sua ação: ").strip()
    print()

    if acao == "1":
        print("Você olha para o rei, sentindo sua pressão imponente, mas não se curva perante à ele.")
        sleep(3)
        print("A coragem junto à adrenalina sentida em batalhas anteriores toma o seu corpo.")
        print("Você ergue sua arma e a aponta para o Rei, pronto para o combate.")
        sleep(2)

    if acao == "2":
        print("Você encara o Rei Demônio e cospe no chão.")
        sleep(1)
        print("\033[36mVocê: \"Você fala demais para alguém que será esquecido em breve.\"\033[0m")
        sleep(2)
        print("O Rei Demônio ruge de ódio e parte para o ataque com força total!")
        sleep(1)
        jogador['hp'] = int(jogador['hpMax'] * 0.75)
        jogador['dano'] = int(jogador['dano'] * 1.2)
        print(f"Seu HP foi reduzido para {jogador['hp']}, mas sua força aumentou para {jogador['dano']}!")
        sleep(2)

    gerar_monstros(1, multiplicador, "Rei Demônio")
    for monstro in lista_monstro:
        if jogador['hp'] > 0:
            iniciar_batalha(jogador, monstro, multiplicador)
        else:
            print("Você caiu diante do poder do Rei Demônio.")
            return

    print("\nApós uma batalha épica, você finca sua arma no coração do Rei Demônio.")
    print("Ele solta um grito que ecoa por todo o castelo, e a escuridão ao redor começa a se dissipar.\n")
    print("\033[35mRei Demônio: \"Maldito... você... não deveria...\"\033[0m\n")
    print("Com um clarão final, ele explode em chamas negras e desaparece.")
    sleep(4)

    print("Você cai de joelhos, o corpo exausto, mas o espírito vitorioso.\n")
    print("O mundo está livre da sombra que o assolava há séculos.")
    print("Você cumpriu o seu destino. Um novo amanhecer se aproxima.")
    print("Mas a lenda... a sua lenda... apenas começou.")
    sleep(4)
    
    cabecalho("O FIM")
