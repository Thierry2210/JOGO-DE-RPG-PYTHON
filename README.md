# Jogo de RPG em Python

Este é um jogo de RPG de texto interativo feito em Python, onde suas escolhas afetam o desenrolar da história. Enfrente goblins, orcs e dragões enquanto evolui seu personagem até enfrentar o rei demônio!

## Como jogar

1. **Pré-requisitos:**  
   - Python 3 instalado no seu computador.

2. **Rodando o jogo:**  
   - No terminal, navegue até a pasta do projeto e execute
   
4. **Como funciona:**  
   - Escolha sua classe (Mago, Guerreiro ou Arqueiro).
   - Escolha a dificuldade (fácil, médio, difícil).
   - Siga as instruções na tela e faça escolhas para avançar na história.
   - Enfrente batalhas contra monstros e suba de nível.

## Estrutura dos arquivos

O jogo está organizado em múltiplos arquivos para facilitar a manutenção e a leitura do código:

1. **main.py**
  Arquivo principal do jogo. É responsável por:

  * Iniciar o jogo.
  * Mostrar o menu inicial.
  * Capturar as escolhas do jogador (classe, dificuldade, etc).
  * Controlar o fluxo da narrativa.

2. **herois.py**
  Define as classes jogáveis (Mago, Guerreiro, Arqueiro), incluindo:

  * Atributos iniciais (vida, ataque, magia, etc).
  * Evolução do personagem (subida de nível, ganho de atributos).

3. **monstros.py**
  Contém as funções que criam os inimigos (goblins, orcs, dragões), com:

  * Atributos específicos para cada tipo e dificuldade.
  * Variação nos inimigos conforme o progresso do jogo.

4. **batalha.py**
  Lógica de combate entre o jogador e os monstros:

  * Turnos de ataque.
  * Cálculo de dano.
  * Verificação de vitória ou derrota.
  * Uso de habilidades especiais (se houver).

5. **cabecalho_limpar.py**
  Funções auxiliares para:

  * Limpar a tela entre as fases do jogo.
  * Mostrar cabeçalhos estilizados com o nome do jogo e seções.

6.**historia_goblin.py, historia_orc.py, historia_dragao.py**
  Cada um desses arquivos contém partes específicas da narrativa do jogo, relacionadas a:

  * Eventos e escolhas durante encontros com goblins, orcs ou dragões.
  * Desenvolvimento da história com base nas decisões do jogador.

7. **imports.py**
  Arquivo que centraliza todas as importações comuns aos demais módulos. Isso facilita a organização e a manutenção do código.
