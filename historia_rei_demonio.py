from imports import subcabecalho, gerar_monstros, lista_monstro, iniciar_batalha
from time import sleep

def historia_rei_demonio(jogador, multiplicador):
    subcabecalho("O Trono das Sombras")
    print("Você caminha por terras esquecidas, onde até o vento parece sussurrar lamentos antigos.")
    print("Ao longe, uma fortaleza negra ergue-se entre montanhas escuras como carvão.")
    print("Você sente que seu destino te chama... o Rei Demônio o aguarda.")
    sleep(4)

    print("\nAo adentrar a fortaleza, o ar se torna denso, quase impossível de respirar.")
    print("Salões gigantescos e corredores tomados por sombras se estendem infinitamente.")
    print("Você sente os olhos da escuridão te observando.")
    sleep(3)

    print("No centro da sala do trono, sentado com imponência, está ele.")
    print("O Rei Demônio, envolto em uma armadura viva que pulsa como carne corrompida.")
    print("Seus olhos brilham com chamas roxas e seu sorriso é o de quem conhece todos os seus medos.")
    sleep(4)

    print("\nRei Demônio: \"Então é você... o verme que ousou matar meu dragão.\"")
    print("Rei Demônio: \"Por eras assisti sua raça rastejar por essas terras. Sempre tão fraca... tão previsível.\"")
    print("Rei Demônio: \"Mas você... você causou problemas demais.\"")
    sleep(3)

    print("\nVocê: \"Eu lutei para proteger o que restou deste mundo. Não me arrependo de nada.\"")
    print("Rei Demônio: \"Coragem? Ou tolice?\" — ele se levanta, e o chão treme sob seus pés.")
    print("Rei Demônio: \"Venha então, herói. Mostre-me o que o último tolo da sua espécie pode fazer.\"")
    sleep(4)

    batalha_rei_demonio(jogador, multiplicador)

def batalha_rei_demonio(jogador, multiplicador):
    subcabecalho("BATALHA FINAL — REI DEMÔNIO")
    sleep(2)

    print("1. Enfrentar o Rei Demônio de frente.")
    print("2. Provocar o Rei Demônio (RISCO + RECOMPENSA).")
    acao = input("Escolha sua ação: ").strip()
    print()

    if acao == "2":
        print("Você encara o Rei Demônio e cospe no chão.")
        print("Você: \"Você fala demais para alguém que será esquecido em breve.\"")
        print("O Rei Demônio ruge de ódio e parte para o ataque com força total!")
        jogador['hp'] = int(jogador['hpMax'] * 0.75)
        jogador['forca'] = int(jogador['forca'] * 1.2)
        print(f"Seu HP foi reduzido para {jogador['hp']}, mas sua força aumentou para {jogador['forca']}!")

    gerar_monstros(1, multiplicador, "Rei Demônio")
    for monstro in lista_monstro:
        if jogador['hp'] > 0:
            iniciar_batalha(jogador, monstro, multiplicador)
        else:
            print("Você caiu diante do poder do Rei Demônio.")
            return

    print("\nApós uma batalha épica, você finca sua arma no coração do Rei Demônio.")
    print("Ele solta um grito que ecoa por todo o castelo, e a escuridão ao redor começa a se dissipar.")
    print("Rei Demônio: \"Maldito... você... não deveria...\"")
    print("Com um clarão final, ele explode em chamas negras e desaparece.")
    sleep(4)

    print("Você cai de joelhos, o corpo exausto, mas o espírito vitorioso.")
    print("O mundo está livre da sombra que o assolava há séculos.")
    print("Você cumpriu o seu destino. Um novo amanhecer se aproxima.")
    print("Mas a lenda... a sua lenda... apenas começou.")
    sleep(4)
