import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Corrida de Carro")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Configurações do jogo
FPS = 60
VELOCIDADE_JOGADOR = 5
VELOCIDADE_OBSTACULO = 15
LARGURA_CARRO = 60
ALTURA_CARRO = 100

# Função para carregar imagens
def carregar_imagem(caminho):
    try:
        imagem = pygame.image.load(caminho)
        return imagem
    except pygame.error as e:
        print(f"Erro ao carregar a imagem: {caminho}")
        print(e)
        sys.exit()

# Carrega as imagens
carro_jogador = carregar_imagem("C:\\Users\\aluno\\Desktop\\jhony-oliveira\\carro_jogador.png.jpg")  # Substitua pelo caminho da imagem do carro do jogador
carro_obstaculo = carregar_imagem("C:\\Users\\aluno\\Desktop\\jhony-oliveira\\carro_obstaculo.png.jpg")  # Substitua pelo caminho da imagem do carro obstáculo
fundo = carregar_imagem("C:\\Users\\aluno\\Desktop\\jhony-oliveira\\fundo.png.jpg")  # Substitua pelo caminho da imagem de fundo

# Redimensiona as imagens
carro_jogador = pygame.transform.scale(carro_jogador, (LARGURA_CARRO, ALTURA_CARRO))
carro_obstaculo = pygame.transform.scale(carro_obstaculo, (LARGURA_CARRO, ALTURA_CARRO))
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))  # Redimensiona o fundo para o tamanho da tela

# Inicializa as variáveis do jogo
jogador_x = LARGURA // 2 - LARGURA_CARRO // 2
jogador_y = ALTURA - ALTURA_CARRO - 20
obstaculo_x = random.randint(0, LARGURA - LARGURA_CARRO)
obstaculo_y = -ALTURA_CARRO
pontuacao = 0

# Função para desenhar os objetos na tela
def desenhar_objetos():
    TELA.blit(fundo, (0, 0))  # Desenha o fundo
    TELA.blit(carro_jogador, (jogador_x, jogador_y))  # Desenha o carro do jogador
    TELA.blit(carro_obstaculo, (obstaculo_x, obstaculo_y))  # Desenha o carro obstáculo
    # Exibe a pontuação
    fonte = pygame.font.Font(None, 36)
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
    TELA.blit(texto_pontuacao, (10, 10))

# Função para mover o jogador
def mover_jogador():
    global jogador_x
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_x > 0:
        jogador_x -= VELOCIDADE_JOGADOR
    if teclas[pygame.K_RIGHT] and jogador_x < LARGURA - LARGURA_CARRO:
        jogador_x += VELOCIDADE_JOGADOR

# Função para mover o obstáculo
def mover_obstaculo():
    global obstaculo_x, obstaculo_y, pontuacao
    obstaculo_y += VELOCIDADE_OBSTACULO
    if obstaculo_y > ALTURA:
        obstaculo_y = -ALTURA_CARRO
        obstaculo_x = random.randint(0, LARGURA - LARGURA_CARRO)
        pontuacao += 1

# Função para verificar colisão
def verificar_colisao():
    if (jogador_x < obstaculo_x + LARGURA_CARRO and
        jogador_x + LARGURA_CARRO > obstaculo_x and
        jogador_y < obstaculo_y + ALTURA_CARRO and
        jogador_y + ALTURA_CARRO > obstaculo_y):
        return True
    return False

# Função para exibir a tela de início
def tela_inicio():
    TELA.blit(fundo, (0, 0))  # Desenha o fundo na tela de início
    fonte_titulo = pygame.font.Font(None, 74)
    fonte_instrucoes = pygame.font.Font(None, 36)
    texto_titulo = fonte_titulo.render("Corrida de Carro", True, BRANCO)
    texto_instrucoes = fonte_instrucoes.render("Pressione ESPAÇO para começar", True, BRANCO)
    TELA.blit(texto_titulo, (LARGURA // 2 - texto_titulo.get_width() // 2, ALTURA // 3))
    TELA.blit(texto_instrucoes, (LARGURA // 2 - texto_instrucoes.get_width() // 2, ALTURA // 2))
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False

# Função para exibir a tela de game over
def tela_game_over():
    TELA.blit(fundo, (0, 0))  # Desenha o fundo na tela de game over
    fonte_titulo = pygame.font.Font(None, 74)
    fonte_pontuacao = pygame.font.Font(None, 48)
    fonte_instrucoes = pygame.font.Font(None, 36)
    texto_titulo = fonte_titulo.render("Game Over!", True, BRANCO)
    texto_pontuacao = fonte_pontuacao.render(f"Pontuação: {pontuacao}", True, BRANCO)
    texto_instrucoes = fonte_instrucoes.render("Pressione ESPAÇO para jogar novamente ou Q para sair", True, BRANCO)
    TELA.blit(texto_titulo, (LARGURA // 2 - texto_titulo.get_width() // 2, ALTURA // 3))
    TELA.blit(texto_pontuacao, (LARGURA // 2 - texto_pontuacao.get_width() // 2, ALTURA // 2))
    TELA.blit(texto_instrucoes, (LARGURA // 2 - texto_instrucoes.get_width() // 2, 2 * ALTURA // 3))
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    reiniciar_jogo()
                    return True  # Retorna True para reiniciar o jogo
                if evento.key == pygame.K_q:
                    return False  # Retorna False para sair do jogo

# Função para reiniciar o jogo
def reiniciar_jogo():
    global jogador_x, jogador_y, obstaculo_x, obstaculo_y, pontuacao
    jogador_x = LARGURA // 2 - LARGURA_CARRO // 2
    jogador_y = ALTURA - ALTURA_CARRO - 20
    obstaculo_x = random.randint(0, LARGURA - LARGURA_CARRO)
    obstaculo_y = -ALTURA_CARRO
    pontuacao = 0

# Loop principal do jogo
clock = pygame.time.Clock()
tela_inicio()
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    mover_jogador()
    mover_obstaculo()
    desenhar_objetos()

    if verificar_colisao():
        if not tela_game_over():  # Se o jogador escolher sair
            rodando = False
        else:  # Se o jogador escolher jogar novamente
            reiniciar_jogo()

    pygame.display.flip()
    clock.tick(FPS)

# Finaliza o Pygame
pygame.quit()