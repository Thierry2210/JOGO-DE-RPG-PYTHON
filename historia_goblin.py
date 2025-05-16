from imports import subcabecalho, cabecalho, limpar, gerar_monstros, lista_monstro, iniciar_batalha
from time import sleep

# Função auxiliar para lidar com emboscadas de goblins
def emboscada_goblins(jogador, multiplicador, contexto="emboscado por goblins"):
    print(f"\nVocê é {contexto}! Prepare-se para a batalha.")
    sleep(2)
    gerar_monstros(1, multiplicador, "Goblin")
    batalha_goblins(jogador, multiplicador)

# Função de escolha robusta
def escolha_opcao(pergunta, opcoes_validas):
    while True:
        escolha = input(pergunta).strip()
        if escolha in opcoes_validas:
            return escolha
        else:
            print("Escolha inválida! Tente novamente.")

# Função principal da história
def historia_goblins(jogador, multiplicador):
    subcabecalho("Início da História")
    print("A Floresta Misteriosa")
    print("Você acorda em uma floresta densa, cercado por árvores altas e sombras misteriosas.")
    print("Não se lembra de como chegou aqui ou quem você é, mas sente uma estranha sensação de que algo está errado.")
    sleep(3)
    print("Enquanto tenta se orientar, ouve um rugido distante. Algo grande está por perto.")
    sleep(3)

    print("O que você faz?")
    print("1. Investigar o som.")
    print("2. Ignorar o som e tentar sair da floresta.")
    escolha = escolha_opcao("Digite o número da sua escolha: ", ["1", "2"])
    print()

    if escolha == "1":
        print("Você decide investigar o som e se aproxima cautelosamente.")
        sleep(2)
        print("À frente, encontra um dragão ferido, com escamas brilhantes e olhos assustados.")
        sleep(3)

        print("\nO que você faz?")
        print("1. Ajudar o dragão")
        print("2. Atacar o dragão")
        print("3. Fugir")
        escolha_dragao = escolha_opcao("Escolha: ", ["1", "2", "3"])

        if escolha_dragao == "1":
            print("\nVocê oferece ajuda ao dragão, que retribui com um rugido agradecido.")
            sleep(2)
            print("Ele sopra uma chama que revela um caminho secreto até um vilarejo.")
            sleep(2)
            print("Mas no meio do trajeto, você é emboscado por goblins saídos da mata!")
            emboscada_goblins(jogador, multiplicador)

        elif escolha_dragao == "2":
            print("\nVocê ataca, mas o dragão gravimente ferido revida com um golpe fraco do seu bater de asas!")
            jogador['hp'] = max(1, jogador['hp'] // 2)
            print(f"Você é lançado para longe. Seu HP foi reduzido para metade {jogador['hp']}/{jogador['hpMax']}.")
            sleep(2)
            print("Você tenta se levantar, mas os goblins que lhe observaram de longe aproveitam a oportunidade e atacam!")
            sleep(2)
            emboscada_goblins(jogador, multiplicador)

        elif escolha_dragao == "3":
            print("\nVocê foge, mas escorrega e cai em um buraco feito por alguém ou ALGO.")
            sleep(2)
            print("Ao se levantar, percebe que está cercado por sombras... GOBLINS.")
            print("Eles aproveitam a chance e avançam sobre você!")
            jogador['hp'] -= 20 
            print(f" Seu HP foi reduzido pelo ataque {jogador['hp']}/{jogador['hpMax']}.")
            sleep(2)
            emboscada_goblins(jogador, multiplicador)

    elif escolha == "2":
        print("Você opta por evitar o som e caminha pela floresta densa.")
        sleep(2)
        print("Após horas, chega a uma clareira iluminada por uma luz mágica.")
        sleep(2)

        print("\nO que você faz?")
        print("1. Investigar a luz")
        print("2. Continuar andando")
        escolha_luz = escolha_opcao("Escolha: ", ["1", "2"])

        if escolha_luz == "1":
            print("\nVocê se aproxima da luz e percebe que é uma fogueira de goblins.")
            print("Ao tentar recuar, pisa em um galho. Eles percebem sua presença!")
            emboscada_goblins(jogador, multiplicador)

        elif escolha_luz == "2":
            print("\nVocê ignora a luz e continua andando. Após algum tempo, encontra uma trilha humana.")
            sleep(2)
            print("Você a segue, mas é surpreendido por goblins emboscados entre as árvores!")
            emboscada_goblins(jogador, multiplicador)

# Função de batalha com goblins
def batalha_goblins(jogador, multiplicador):
    subcabecalho("BATALHA INICIADA")
    sleep(2)

    print("1. Atacar diretamente")
    print("2. Tentar fugir")
    acao = escolha_opcao("Escolha sua ação: ", ["1", "2"])
    print()

    if acao == "1":
        for monstro in lista_monstro:
            if jogador['hp'] > 0:
                iniciar_batalha(jogador, monstro, multiplicador)
            else:
                print("Você foi derrotado pelos goblins!")

    elif acao == "2":
        print("Você tenta fugir, mas uma flecha atinge suas costas.")
        jogador['hp'] = max(1, jogador['hp'] // 2)
        print(f"Seu HP foi reduzido para {jogador['hp']}. Você precisa lutar agora!")
        sleep(2)
        for monstro in lista_monstro:
            if jogador['hp'] > 0:
                iniciar_batalha(jogador, monstro, multiplicador)
            else:
                print("Você foi derrotado pelos goblins!")

    print("\nApós a batalha, você respira fundo e tenta se recuperar.")
    sleep(2)
    print("Você se levanta, sacode a poeira e continua sua jornada.")
    sleep(2)
    print("A floresta parece menos ameaçadora agora, mas você sabe que perigos ainda estão por vir.")
    sleep(2)
    print("Você avança, determinado a tentar sair dessa floresta em busca de saber quem você é.")
    sleep(2)
    print("A aventura está apenas começando...")
    sleep(2)