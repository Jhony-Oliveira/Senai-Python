import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tênis de Mesa")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Configurações do jogo
FPS = 60
VELOCIDADE_RAQUETE = 10
VELOCIDADE_BOLA_X = 5
VELOCIDADE_BOLA_Y = 5
TAMANHO_RAQUETE = 100
ESPESSURA_RAQUETE = 20
TAMANHO_BOLA = 15

# Inicializa as variáveis do jogo
raquete1_y = ALTURA // 2 - TAMANHO_RAQUETE // 2
raquete2_y = ALTURA // 2 - TAMANHO_RAQUETE // 2
bola_x = LARGURA // 2
bola_y = ALTURA // 2
bola_direcao_x = random.choice([-1, 1])
bola_direcao_y = random.choice([-1, 1])
pontos_jogador1 = 0
pontos_jogador2 = 0

# Função para desenhar as raquetes e a bola
def desenhar_objetos():
    TELA.fill(PRETO)
    # Desenha as raquetes
    pygame.draw.rect(TELA, BRANCO, (50, raquete1_y, ESPESSURA_RAQUETE, TAMANHO_RAQUETE))
    pygame.draw.rect(TELA, BRANCO, (LARGURA - 50 - ESPESSURA_RAQUETE, raquete2_y, ESPESSURA_RAQUETE, TAMANHO_RAQUETE))
    # Desenha a bola
    pygame.draw.ellipse(TELA, BRANCO, (bola_x - TAMANHO_BOLA // 2, bola_y - TAMANHO_BOLA // 2, TAMANHO_BOLA, TAMANHO_BOLA))
    # Desenha os pontos
    fonte = pygame.font.Font(None, 74)
    texto_jogador1 = fonte.render(str(pontos_jogador1), True, BRANCO)
    texto_jogador2 = fonte.render(str(pontos_jogador2), True, BRANCO)
    TELA.blit(texto_jogador1, (LARGURA // 4, 10))
    TELA.blit(texto_jogador2, (3 * LARGURA // 4 - texto_jogador2.get_width(), 10))

# Função para mover as raquetes
def mover_raquetes():
    global raquete1_y, raquete2_y
    teclas = pygame.key.get_pressed()
    # Movimento da raquete do jogador 1 (W e S)
    if teclas[pygame.K_w] and raquete1_y > 0:
        raquete1_y -= VELOCIDADE_RAQUETE
    if teclas[pygame.K_s] and raquete1_y < ALTURA - TAMANHO_RAQUETE:
        raquete1_y += VELOCIDADE_RAQUETE
    # Movimento da raquete do jogador 2 (Cima e Baixo)
    if teclas[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= VELOCIDADE_RAQUETE
    if teclas[pygame.K_DOWN] and raquete2_y < ALTURA - TAMANHO_RAQUETE:
        raquete2_y += VELOCIDADE_RAQUETE

# Função para mover a bola
def mover_bola():
    global bola_x, bola_y, bola_direcao_x, bola_direcao_y, pontos_jogador1, pontos_jogador2
    bola_x += VELOCIDADE_BOLA_X * bola_direcao_x
    bola_y += VELOCIDADE_BOLA_Y * bola_direcao_y

    # Colisão com as paredes superior e inferior
    if bola_y - TAMANHO_BOLA // 2 <= 0 or bola_y + TAMANHO_BOLA // 2 >= ALTURA:
        bola_direcao_y *= -1

    # Colisão com a raquete do jogador 1
    if bola_x - TAMANHO_BOLA // 2 <= 50 + ESPESSURA_RAQUETE and raquete1_y <= bola_y <= raquete1_y + TAMANHO_RAQUETE:
        bola_direcao_x *= -1

    # Colisão com a raquete do jogador 2
    if bola_x + TAMANHO_BOLA // 2 >= LARGURA - 50 - ESPESSURA_RAQUETE and raquete2_y <= bola_y <= raquete2_y + TAMANHO_RAQUETE:
        bola_direcao_x *= -1

    # Pontuação
    if bola_x - TAMANHO_BOLA // 2 <= 0:
        pontos_jogador2 += 1
        resetar_bola()
    if bola_x + TAMANHO_BOLA // 2 >= LARGURA:
        pontos_jogador1 += 1
        resetar_bola()

# Função para resetar a bola
def resetar_bola():
    global bola_x, bola_y, bola_direcao_x, bola_direcao_y
    bola_x = LARGURA // 2
    bola_y = ALTURA // 2
    bola_direcao_x = random.choice([-1, 1])
    bola_direcao_y = random.choice([-1, 1])

# Loop principal do jogo
clock = pygame.time.Clock()
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    mover_raquetes()
    mover_bola()
    desenhar_objetos()

    pygame.display.flip()
    clock.tick(FPS)

# Finaliza o Pygame
pygame.quit()