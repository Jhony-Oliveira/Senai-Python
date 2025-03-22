import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 1000, 800
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("🐍 Jogo da Cobrinha 🐍")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 100, 255)

# Configurações da cobra
TAMANHO_BLOCO = 20
VELOCIDADE = 10  # Velocidade fixa

# Fonte
FONTE = pygame.font.Font(None, 36)

def gerar_comida():
    """Gera a comida em um local aleatório"""
    return (
        random.randint(0, (LARGURA // TAMANHO_BLOCO) - 1) * TAMANHO_BLOCO,
        random.randint(0, (ALTURA // TAMANHO_BLOCO) - 1) * TAMANHO_BLOCO
    )

def desenhar_cobra(cobra):
    """Desenha a cobra na tela"""
    for segmento in cobra:
        pygame.draw.rect(TELA, VERDE, (segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO))

def exibir_texto(texto, x, y, cor=BRANCO):
    """Exibe um texto na tela"""
    superficie_texto = FONTE.render(texto, True, cor)
    TELA.blit(superficie_texto, (x, y))

def jogo():
    """Loop principal do jogo"""
    cobra = [(300, 200)]
    direcao = (TAMANHO_BLOCO, 0)
    comida = gerar_comida()
    pontuacao = 0
    clock = pygame.time.Clock()
    rodando = True
    recorde = 0  # Recorde inicial

    while rodando:
        TELA.fill(PRETO)

        # Eventos do teclado
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao != (0, TAMANHO_BLOCO):
                    direcao = (0, -TAMANHO_BLOCO)
                elif evento.key == pygame.K_DOWN and direcao != (0, -TAMANHO_BLOCO):
                    direcao = (0, TAMANHO_BLOCO)
                elif evento.key == pygame.K_LEFT and direcao != (TAMANHO_BLOCO, 0):
                    direcao = (-TAMANHO_BLOCO, 0)
                elif evento.key == pygame.K_RIGHT and direcao != (-TAMANHO_BLOCO, 0):
                    direcao = (TAMANHO_BLOCO, 0)

        # Atualiza a posição da cobra
        nova_cabeca = (cobra[0][0] + direcao[0], cobra[0][1] + direcao[1])
        cobra.insert(0, nova_cabeca)

        # Verifica colisão com a comida
        if nova_cabeca == comida:
            pontuacao += 1
            comida = gerar_comida()
        else:
            cobra.pop()  # Remove o último segmento da cobra

        # Verifica colisão com as paredes ou consigo mesma
        if (nova_cabeca[0] < 0 or nova_cabeca[0] >= LARGURA or
                nova_cabeca[1] < 0 or nova_cabeca[1] >= ALTURA or
                nova_cabeca in cobra[1:]):
            if pontuacao > recorde:
                recorde = pontuacao
            tela_game_over(pontuacao, recorde)

        # Desenha os elementos na tela
        desenhar_cobra(cobra)
        pygame.draw.rect(TELA, VERMELHO, (comida[0], comida[1], TAMANHO_BLOCO, TAMANHO_BLOCO))
        exibir_texto(f"Pontos: {pontuacao}", 10, 10)
        exibir_texto(f"Recorde: {recorde}", 450, 10, AZUL)

        pygame.display.flip()
        clock.tick(VELOCIDADE)

def tela_game_over(pontuacao, recorde):
    """Tela de Game Over com opção de reiniciar"""
    TELA.fill(PRETO)
    exibir_texto("💀 GAME OVER 💀", LARGURA // 2 - 100, ALTURA // 2 - 50, VERMELHO)
    exibir_texto(f"Pontos: {pontuacao}", LARGURA // 2 - 50, ALTURA // 2)
    exibir_texto(f"Recorde: {recorde}", LARGURA // 2 - 50, ALTURA // 2 + 30, AZUL)
    exibir_texto("Pressione ENTER para jogar novamente", LARGURA // 2 - 160, ALTURA // 2 + 80)

    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    esperando = False
                    jogo()

# Inicia o jogo
jogo()
