from imports import *  # Importa as funções necessárias


def historia_dragao(jogador, multiplicador):
    subcabecalho("O Covil do Dragão")
    print("Após derrotar os orcs, você encontra um velho mapa entre os destroços.")
    print("Ele aponta para uma montanha distante marcada com um símbolo de fogo.")
    sleep(3)
    print("Você sente que há algo poderoso e perigoso esperando lá.")
    print("Decide seguir o mapa em busca de respostas — ou talvez de poder.")
    sleep(3)
    print("Após dias de viagem, escalando terrenos íngremes e enfrentando o frio das alturas,")
    print("você encontra a entrada de uma caverna escura que exala calor.")
    print("O chão está coberto por ossos queimados e o ar é pesado.")
    print("Você ouve uma respiração profunda vindo do interior da caverna.")
    print()
    print("O que você faz?")
    print("1. Entrar furtivamente na caverna.")
    print("2. Gritar para desafiar o que estiver lá dentro.")
    escolha = input("Digite o número da sua escolha: ")

    print()
    if escolha == "1":
        print("\nVocê entra silenciosamente na caverna, se esgueirando pelas sombras.")
        print("Lá dentro, vê um enorme dragão deitado sobre um monte de ouro e relíquias antigas.")
        print("Você tenta se aproximar de um artefato brilhante, mas escorrega sobre um osso.")
        print("O dragão desperta, furioso!")
        sleep(3)
        print("Sem escolha, você se prepara para a batalha mais difícil da sua vida.")
        batalha_dragao(jogador, multiplicador)
        print("\nVocê derrota o dragão e toma posse de seu tesouro ancestral.")
        return

    elif escolha == "2":
        print("\nVocê grita com bravura, desafiando o que quer que esteja lá dentro!")
        print("Um rugido ensurdecedor responde ao seu chamado.")
        print("O chão treme quando o enorme dragão emerge das sombras.")
        print("Com olhos flamejantes, ele solta uma rajada de fogo em sua direção!")
        jogador['hp'] = max(1, jogador['hp'] - 150)
        print(f"Você sofre queimaduras! Seu HP agora é {jogador['hp']}.")
        sleep(3)
        print("Você ergue sua arma, pronto para o combate final!")
        batalha_dragao(jogador, multiplicador)
        print("\nApós uma batalha feroz, você sai da caverna vitorioso, carregando cicatrizes... e glória.")
        return

    else:
        print("\nVocê hesita na entrada da caverna e perde tempo demais.")
        print("O dragão percebe sua presença e ataca sem aviso!")
        print("Você é pego de surpresa e não sobrevive ao ataque.")
        sleep(3)
        cabecalho("FIM DE JOGO")
        sys.exit(0)

def batalha_dragao(jogador, multiplicador):
    subcabecalho("ENFRENTANDO O DRAGÃO")
    sleep(3)
    print("Um rugido ensurdecedor ecoa pelo vale.")
    print("As asas do dragão batem com força, levantando uma nuvem de poeira e cinzas.")
    print("Você sente o calor crescente em sua pele.")
    print("\n1. Enfrentar o dragão de frente, com coragem.")
    print("2. Tentar fugir e se esconder antes que ele te veja.")
    acao = input("Escolha sua ação: ")

    if acao == "1":
        print("\nVocê encara o dragão com bravura e se lança ao combate!")
        sleep(2)
        gerar_monstros(1, multiplicador, "Dragão")
        for monstro in lista_monstro:
            if jogador['hp'] > 0:
                iniciar_batalha(jogador, monstro, multiplicador)
            else:
                print("Você foi completamente dominado pelo dragão.")
                cabecalho("FIM DE JOGO")
                sys.exit(0)
        print("\nContra todas as probabilidades, você vence o dragão e sobrevive à batalha!")
        return

    elif acao == "2":
        print("\nVocê tenta correr por entre as pedras, procurando abrigo nas ruínas ao redor.")
        print("Mas o dragão percebe sua fuga e lança uma labareda em sua direção.")
        print("Você se joga no chão a tempo, mas parte do fogo te atinge.")
        jogador['hp'] = max(1, jogador['hp'] // 2)
        print(f"Você está gravemente queimado! Seu HP foi reduzido para {jogador['hp']}!")
        print("Agora, sem escapatória, você precisa enfrentar o dragão mesmo ferido.")
        sleep(3)
        gerar_monstros(1, multiplicador, "Dragão")
        for monstro in lista_monstro:
            if jogador['hp'] > 0:
                iniciar_batalha(jogador, monstro, multiplicador)
            else:
                print("Você foi derrotado pelas chamas do dragão.")
                cabecalho("FIM DE JOGO")
                sys.exit(0)
        print("\nMesmo ferido, você derrota o dragão e permanece de pé!")
        return

    else:
        print("\nVocê hesita, paralisado pelo medo, e o dragão aproveita.")
        print("Com um único sopro flamejante, você é consumido pelas chamas.")
        sleep(3)
        cabecalho("FIM DE JOGO")
        sys.exit(0)