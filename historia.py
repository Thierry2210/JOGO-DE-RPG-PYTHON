from cabecalho_limpar import cabecalho, subcabecalho, limpar
from time import sleep

def introducao():
    limpar()
    cabecalho("Bem-vindo ao jogo de história interativa!")
    print("Você está prestes a embarcar em uma aventura emocionante.")
    print("Suas escolhas moldarão o desenrolar da história.")
    print("Prepare-se para tomar decisões que afetarão o destino do seu personagem.")
    print("Vamos começar!\n")
    sleep(2)

def historia(jogador):
    limpar()
    subcabecalho("Início da História")
    print("A Floresta Misteriosa")
    print("Você acorda em uma floresta densa, cercado por árvores altas e sombras misteriosas.")
    print("Enquanto você tenta se lembrar de como chegou aqui, ouve um rugido distante.")
    print("Você percebe que não está sozinho.")
    sleep(2)
    print("O que você faz?")
    print("1. Investigar o som")
    print("2. Tentar encontrar um caminho de volta para casa")
    print("3. Esconder-se e esperar")
    escolha = input("Digite o número da sua escolha: ")

    print("=============================\n")
    # Verifica a escolha do jogador
    if escolha == "1":
        print("\nVocê decide investigar o som e se aproxima cautelosamente.")
        sleep(2)
        print("À medida que avança, você encontra um dragão enorme, com escamas brilhantes.")
        print("O dragão parece ferido e assustado.")
        sleep(2)
        print("O que você faz?")
        print("1. Ajudar o dragão")
        print("2. Atacar o dragão")
        print("3. Fugir")
        escolha_dragao = input("Escolha: ")

        print("=============================\n")
        # Verifica a escolha do jogador em relação ao dragão
        if escolha_dragao == "1":
            print("\nVocê se aproxima lentamente e oferece ajuda.")
            sleep(2)
            print("O dragão, grato, cospe uma pequena chama que ilumina um caminho secreto entre as árvores.")
            print("Você o segue e encontra um antigo santuário abandonado.")
            sleep(2)
            return "Dragão"
        elif escolha_dragao == "2":
            print("\nVocê ataca o dragão, mas ele rapidamente se defende e te derruba com um sopro de fogo.")
            sleep(2)
            print("Você sente uma dor intensa enquanto é lançado ao chão.")
            jogador['hp'] = max(1, jogador['hp'] // 2)
            print(f"Seu HP foi reduzido para {jogador['hp']}!")
            sleep(2)
            print("Antes de desmaiar, você vê pequenas figuras se aproximando... Goblins!")
            return "Goblin"
        elif escolha_dragao == "3":
            print("\nVocê foge desesperadamente pela floresta, mas tropeça e rola até um buraco profundo.")
            print("Lá dentro, você ouve sons... Goblins se aproximando!")
            return "Goblin"

    # Verifica a escolha do jogador em relação ao caminho de casa
    elif escolha == "2":
        print("\nVocê tenta encontrar um caminho de volta para casa, mas a floresta é densa e confusa.")
        print("Após horas de caminhada, você se depara com uma clareira iluminada por uma luz mágica.")
        print("O que você faz?")
        print("1. Investigar a luz")
        print("2. Continuar procurando o caminho de casa")
        escolha_luz = input("Escolha: ")

        print("=============================\n")
        # Verifica a escolha do jogador em relação à luz
        if escolha_luz == "1":
            print("\nVocê investiga a luz e encontra uma fada.")
            sleep(2)
            print("Ela te dá um frasco de luz mágica e desaparece.")
            sleep(2)
            print("Seguindo a luz do frasco, você encontra um grupo de goblins acampados bloqueando o caminho.")
            return "Goblin"
        elif escolha_luz == "2":
            print("\nVocê ignora a luz e segue andando.")
            sleep(2)
            print("Ao sair da trilha, é emboscado por um grupo de goblins escondidos entre as árvores!")
            return "Goblin"

    # Verifica a escolha do jogador em relação ao esconderijo
    elif escolha == "3":
        print("\nVocê decide se esconder e esperar.")
        print("Após algum tempo, um grupo de aventureiros passa por você.")
        print("Eles parecem estar em uma missão importante.")
        print("O que você faz?")
        print("1. Juntar-se aos aventureiros")
        print("2. Continuar escondido")
        escolha_aventureiros = input("Escolha: ")

        print("=============================\n")
        # Verifica a escolha do jogador em relação aos aventureiros
        if escolha_aventureiros == "1":
            print("\nVocê se junta ao grupo e descobre que eles estão indo enfrentar goblins que têm atacado vilarejos.")
            print("Juntos, vocês chegam ao acampamento dos goblins.")
            return "Goblin"
        elif escolha_aventureiros == "2":
            print("\nVocê continua escondido, mas logo é descoberto por goblins farejadores!")
            print("Você precisa lutar!")
            return "Goblin"

    else:
        print("\nEscolha inválida! Tente novamente.")
        return historia()

    # Encontro com os goblins
    subcabecalho("\nBATALHA INICIADA")
    sleep(2)
    print("Um grupo de goblins aparece, armados com adagas e grunhindo ferozmente!")
    print("Você prepara sua arma para a luta...")
    sleep(2)
    print("1. Atacar diretamente")
    print("2. Usar uma armadilha do ambiente")
    print("3. Tentar assustá-los com gritos e gestos")
    acao = input("Escolha sua ação: ")

    if acao == "1":
        print("\nVocê parte para o ataque, acertando um dos goblins em cheio!")
        print("Eles recuam momentaneamente, mas continuam a luta.")

    elif acao == "2":
        print("\nVocê empurra uma pilha de pedras que cai sobre dois goblins!")
        print("Isso enfraquece o grupo inimigo.")
    elif acao == "3":
        print("\nVocê grita com toda sua força e agita os braços como um louco.")
        print("Os goblins se assustam e fogem — exceto um mais corajoso, que avança!")
    else:
        print("\nVocê hesita e os goblins aproveitam para atacar! Você se fere levemente.")

    print("\nVocê vence a batalha contra os goblins — por pouco.")
    sleep(2)
    print("Com o perigo momentaneamente afastado, você segue seu caminho mais forte do que antes...")
    sleep(2)
    subcabecalho("Caminho Incerto")
    print("Você continua pela floresta, agora mais atento e desconfiado.")
    print("As árvores ficam mais esparsas, e o som de passos pesados ecoa à distância.")
    print("A cada passo, a pressão no ar aumenta, como se algo muito forte estivesse próximo.")
    sleep(3)

    print("\nVocê chega a uma área devastada, com árvores quebradas e marcas profundas no solo.")
    print("No centro, um orc gigantesco aguarda, segurando um machado imenso e encarando você com fúria.")
    print("Ele parece proteger alguma coisa... ou alguém.")
    sleep(3)

    subcabecalho("BATALHA CONTRA O ORC")
    print("O orc solta um grito ensurdecedor e parte para cima de você!")
    print("Você precisa agir rápido.")
    print("1. Enfrentar o orc de frente")
    print("2. Usar sua agilidade para desviar e contra-atacar")
    print("3. Tentar negociar com o orc")
    acao_orc = input("Escolha sua ação: ")

    print("=============================\n")
    if acao_orc == "1":
        print("\nVocê encara o orc de frente, arma em punho.")
        print("O impacto da luta é brutal, e você é lançado para trás por um golpe pesado.")
        jogador['hp'] = max(1, jogador['hp'] - 20)
        print(f"Você sofre danos graves! HP atual: {jogador['hp']}")
        print("Mas com esforço, você se levanta e prepara um contra-ataque.")
        resultado = "Orc"
    elif acao_orc == "2":
        print("\nVocê usa sua velocidade para evitar os ataques pesados do orc.")
        print("Aproveitando uma abertura, você atinge seu flanco vulnerável!")
        print("O orc grita de dor, recuando momentaneamente.")
        resultado = "Orc"
    elif acao_orc == "3":
        print("\nVocê levanta as mãos, tentando demonstrar que não quer lutar.")
        print("Surpreendentemente, o orc hesita. Em sua língua rude, ele resmunga algo incompreensível.")
        print("Com gestos, ele aponta para uma árvore caída — sob ela, uma criatura está presa.")
        print("Você percebe que o orc estava protegendo um filhote de criatura mágica.")
        print("Com sua ajuda, o orc consegue libertar o filhote e, em gratidão, entrega a você uma pedra rúnica poderosa.")
        print("Vocês seguem caminhos diferentes, mas algo mudou em você.")
        resultado = "Aliado"
    else:
        print("\nSua indecisão custa caro. O orc aproveita para te atingir com o cabo do machado.")
        jogador['hp'] = max(1, jogador['hp'] - 15)
        print(f"Você cai no chão com dores. HP atual: {jogador['hp']}")
        print("Com dificuldade, você se levanta para continuar lutando.")
        resultado = "Orc"

    sleep(3)
    return resultado
