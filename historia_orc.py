from imports import *
from time import sleep

# Função auxiliar para lidar com emboscadas de orcs
def emboscada_orcs(jogador, multiplicador, contexto="emboscado por orcs"):
    print(f"\nVocê é {contexto}! Prepare-se para a batalha.")
    sleep(2)
    batalha_orcs(jogador, multiplicador)

# Função de escolha robusta (assumindo que não está duplicada)
def escolha_opcao(pergunta, opcoes_validas):
    while True:
        escolha = input(pergunta).strip()
        if escolha in opcoes_validas:
            return escolha
        else:
            print("Escolha inválida! Tente novamente.")

# Função principal da história dos orcs
def historia_orcs(jogador, multiplicador):
    subcabecalho("\033[1;32mContinuação da Jornada\033[0m")
    print("Terras dos Orcs")
    print("Após algum tempo caminhando, acampando e batalhando pela sua vida durante dias e noites.")
    print("Você finalmente encontra uma saída da floresta.")
    print("O sol brilha intensamente e você sente o calor em sua pele.")
    sleep(3)
    print("Mas a alegria dura pouco, pois você percebe que está em uma região devastada.")
    print("A terra está seca e árida, e o céu está coberto por nuvens escuras.")
    sleep(2)
    print("Você avista uma montanha ao longe e decide seguir em direção a ela.")
    print("Enquanto caminha avista um vilarejo ao longe e corre na esperança de encontrar abrigo.")
    sleep(3)
    print("Mas o lugar está destruído, e o ar cheira a fumaça e tensão.")
    sleep(2)
    print("Você nota uma caverna próxima e vê orcs se aproximando.")

    print("\nO que você faz?")
    print("1. Investigar a caverna.")
    print("2. Explorar o vilarejo destruído.")
    escolha = escolha_opcao("Digite o número da sua escolha: ", ["1", "2"])
    print()

    if escolha == "1":
        explorar_caverna(jogador, multiplicador)
    elif escolha == "2":
        explorar_vilarejo(jogador, multiplicador)

def explorar_caverna(jogador, multiplicador):
    print("Você sobe até a caverna com cautela e vê um grupo de orcs ao redor de uma fogueira.")
    sleep(2)
    print("Eles parecem discutir algo importante e não notaram sua presença.")
    print("\nO que você faz?")
    print("1. Ouvir a conversa.")
    print("2. Atacar de surpresa.")
    escolha = escolha_opcao("Escolha: ", ["1", "2"])
    print()

    if escolha == "1":
        print("Você se esconde e escuta que estão planejando um ataque ao vilarejo.")
        sleep(2)
        print("Ao tentar sair silenciosamente, um orc te avista!")
        emboscada_orcs(jogador, multiplicador, contexto="descoberto pelos orcs após espioná-los")
    elif escolha == "2":
        print("Você ataca de surpresa e derruba um orc rapidamente!")
        jogador['xp'] += 50 * multiplicador
        print("Mas os outros reagem e te cercam.")
        emboscada_orcs(jogador, multiplicador, contexto="envolvido em uma luta após atacar os orcs")

def explorar_vilarejo(jogador, multiplicador):
    print("Você caminha pelas ruínas do vilarejo. Há sinais claros de batalha recente.")
    sleep(2)
    print("Entre os escombros, encontra um sobrevivente escondido.")
    print("Ele sussurra: 'Eles voltam à noite... os orcs... cuidado...'")
    sleep(3)
    print("Antes que possa perguntar mais, ele desmaia.")
    print("Você busca abrigo em uma torre de vigia próxima.")
    sleep(2)
    print("Mas ao anoitecer, ouve grunhidos... os orcs estão voltando!")
    emboscada_orcs(jogador, multiplicador, contexto="atacado por orcs ao anoitecer")

def batalha_orcs(jogador, multiplicador):
    subcabecalho("BATALHA CONTRA ORCS")
    sleep(2)
    print("1. Lutar de frente.")
    print("2. Tentar fugir.")
    acao = escolha_opcao("Escolha sua ação: ", ["1", "2"])
    print()

    if acao == "1":
        criar_monstro("Orc", 3, multiplicador)
        for monstro in lista_monstro:
            if jogador['hp'] > 0:
                iniciar_batalha(jogador, monstro, multiplicador)
            else:
                print("Você foi derrotado pelos orcs!")
                return
        print("\nVocê vence os orcs e segue, exausto, mas determinado.")
        sleep(2)

    elif acao == "2":
        print("Você tenta fugir, mas é atingido por uma lança nas costas.")
        jogador['hp'] = max(1, jogador['hp'] // 2)
        print(f"Seu HP foi reduzido para {jogador['hp']}. Você precisa lutar mesmo ferido!")
        sleep(2)
        criar_monstro("Orc", 3, multiplicador)
        for monstro in lista_monstro:
            if jogador['hp'] > 0:
                iniciar_batalha(jogador, monstro, multiplicador)
            else:
                print("Você foi derrotado pelos orcs!")
                return
        print("\nCom muito esforço, você vence os orcs e escapa vivo.")
        sleep(2)

    print("\nApós a batalha, você respira fundo e tenta se recuperar.")
    sleep(2)
    print("Você se levanta, sente o peso das batalhas, mas também uma força renovada.")
    sleep(2)
    print("O território dos orcs ficou para trás, mas você sabe que desafios ainda maiores te aguardam.")
    sleep(2)
    print("\n Você encontra algumas armas ao passar pelo vilarejo, elas parecem ser úteis.")
    upar_item(jogador)
    print("Com determinação, você segue sua jornada, buscando respostas e sobrevivência.")
    sleep(2)
    print("A aventura é muito mais perigosa do que você pensava...")
    sleep(2)