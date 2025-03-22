import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Adivinhação de Palavras")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Fonte
FONTE = pygame.font.Font(None, 48)

# Lista de palavras e dicas
palavras_e_dicas = [
    {"palavra": "PYTHON", "dicas": ["Linguagem de programação", "Usada em inteligência artificial", "Tem uma cobra no nome"]},
    {"palavra": "JAVA", "dicas": ["Linguagem de programação orientada a objetos", "Usada em aplicativos Android", "Nome de uma ilha na Indonésia"]},
    {"palavra": "GATO", "dicas": ["Animal doméstico", "Faz 'miau'", "Tem bigodes"]},
    {"palavra": "ABACAXI", "dicas": ["Fruta tropical", "Tem uma coroa", "Usado em sucos e sobremesas"]},
    {"palavra": "SOL", "dicas": ["Estrela central do sistema solar", "Fonte de luz e calor", "Planetas giram ao seu redor"]},
    {"palavra": "LUA", "dicas": ["Satélite natural da Terra", "Controla as marés", "Tem fases"]},
]

# Função para sortear uma nova palavra e dica
def sortear_palavra_e_dica():
    palavra_atual = random.choice(palavras_e_dicas)
    palavra_secreta = palavra_atual["palavra"]
    dicas = palavra_atual["dicas"]
    dica_atual = random.choice(dicas)
    return palavra_secreta, dicas, dica_atual

# Função para desenhar botões
def desenhar_botao(texto, x, y, largura, altura, cor):
    pygame.draw.rect(TELA, cor, (x, y, largura, altura))
    superficie_texto = FONTE.render(texto, True, BRANCO)
    TELA.blit(superficie_texto, (x + 10, y + 10))

# Função para desenhar texto
def desenhar_texto(texto, x, y, cor):
    superficie_texto = FONTE.render(texto, True, cor)
    TELA.blit(superficie_texto, (x, y))

# Inicializa o jogo
palavra_secreta, dicas, dica_atual = sortear_palavra_e_dica()
tentativas_restantes = 6
palpite = ""
mensagem = "Clique em 'Iniciar' para começar!"
jogando = False
mostrar_botoes_inicio = True

# Loop principal do jogo
clock = pygame.time.Clock()
while True:
    TELA.fill(BRANCO)

    # Desenha os botões
    if mostrar_botoes_inicio:
        desenhar_botao("Iniciar", 50, 400, 200, 50, VERDE)
    else:
        desenhar_botao("Reiniciar", 50, 400, 200, 50, AZUL)
        desenhar_botao("Próxima Palavra", 300, 400, 300, 50, VERDE)

    # Exibe a mensagem, dica e palpite atual
    desenhar_texto(mensagem, 50, 50, PRETO)
    if jogando:
        desenhar_texto(f"Dica: {dica_atual}", 50, 150, PRETO)
        desenhar_texto(f"Palpite: {palpite}", 50, 250, PRETO)
        desenhar_texto(f"Tentativas restantes: {tentativas_restantes}", 50, 350, PRETO)

    # Verifica eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Verifica se o botão "Iniciar" foi clicado
            if mostrar_botoes_inicio and 50 <= x <= 250 and 400 <= y <= 450:
                jogando = True
                mostrar_botoes_inicio = False
                mensagem = f"Dica: {dica_atual}"
            # Verifica se o botão "Reiniciar" foi clicado
            elif not mostrar_botoes_inicio and 50 <= x <= 250 and 400 <= y <= 450:
                palavra_secreta, dicas, dica_atual = sortear_palavra_e_dica()
                tentativas_restantes = 6
                palpite = ""
                mensagem = f"Dica: {dica_atual}"
            # Verifica se o botão "Próxima Palavra" foi clicado
            elif not mostrar_botoes_inicio and 300 <= x <= 600 and 400 <= y <= 450:
                palavra_secreta, dicas, dica_atual = sortear_palavra_e_dica()
                tentativas_restantes = 6
                palpite = ""
                mensagem = f"Dica: {dica_atual}"
        elif evento.type == pygame.KEYDOWN and jogando:
            if evento.key == pygame.K_RETURN:  # Quando o jogador pressiona Enter
                if palpite.upper() == palavra_secreta:
                    mensagem = "Parabéns! Você acertou!"
                    jogando = False
                else:
                    mensagem = "ERRRROUUUU"
                    tentativas_restantes -= 1
                    if tentativas_restantes == 0:
                        mensagem = f"A palavra era {palavra_secreta}"
                        jogando = False
                    else:
                        # Gera uma nova dica para a mesma palavra
                        dica_atual = random.choice([d for d in dicas if d != dica_atual])
                        mensagem = f"Dica: {dica_atual}"
                    palpite = ""  # Limpa o palpite
            elif evento.key == pygame.K_BACKSPACE:  # Remove o último caractere
                palpite = palpite[:-1]
            else:
                if evento.unicode.isalpha():  # Aceita apenas letras
                    palpite += evento.unicode.upper()

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(30)