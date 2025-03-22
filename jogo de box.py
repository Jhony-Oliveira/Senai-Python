import pygame
import time

# Inicializa o Pygame
pygame.init()

# Configuração da tela
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Boxe Melhorado")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)

# Fonte
FONTE = pygame.font.Font(None, 36)

# Sons
som_punch = pygame.mixer.Sound("punch.wav")  # Som de soco
som_defesa = pygame.mixer.Sound("block.wav")  # Som de defesa
som_vitoria = pygame.mixer.Sound("win.wav")  # Som de vitória

# Carregando sprites dos lutadores
lutador1_img = pygame.image.load("lutador1.png")  # Substitua por uma imagem real
lutador2_img = pygame.image.load("lutador2.png")  # Substitua por uma imagem real

# Classe do Lutador
class Lutador:
    def __init__(self, x, y, imagem):
        self.x = x
        self.y = y
        self.vida = 100
        self.velocidade = 5
        self.defendendo = False
        self.imagem = pygame.transform.scale(imagem, (80, 120))  # Redimensiona o sprite

    def desenhar(self):
        TELA.blit(self.imagem, (self.x, self.y))

    def atacar(self, adversario):
        if not adversario.defendendo:
            adversario.vida -= 10  # Dano normal
            som_punch.play()
        else:
            adversario.vida -= 5  # Dano reduzido se estiver defendendo
            som_defesa.play()

    def mover(self, direcao):
        if direcao == "esquerda" and self.x > 0:
            self.x -= self.velocidade
        elif direcao == "direita" and self.x < LARGURA - 80:
            self.x += self.velocidade

# Criando os lutadores
lutador1 = Lutador(200, 400, lutador1_img)
lutador2 = Lutador(550, 400, lutador2_img)

# Função para desenhar a barra de vida
def desenhar_barra_de_vida(lutador, x, y):
    largura_barra = 200
    altura_barra = 20
    pygame.draw.rect(TELA, PRETO, (x, y, largura_barra, altura_barra))  # Fundo da barra
    vida_atual = max(lutador.vida, 0)
    pygame.draw.rect(TELA, VERDE, (x, y, (vida_atual / 100) * largura_barra, altura_barra))  # Vida atual

# Loop do jogo
rodando = True
clock = pygame.time.Clock()
vencedor = None

while rodando:
    TELA.fill(BRANCO)

    # Exibir as barras de vida
    desenhar_barra_de_vida(lutador1, 50, 50)
    desenhar_barra_de_vida(lutador2, 550, 50)

    # Desenha os lutadores
    lutador1.desenhar()
    lutador2.desenhar()

    # Verifica se há vencedor
    if lutador1.vida <= 0:
        vencedor = "Lutador Azul venceu!"
    elif lutador2.vida <= 0:
        vencedor = "Lutador Vermelho venceu!"

    # Se houver vencedor, exibe mensagem
    if vencedor:
        texto_vitoria = FONTE.render(vencedor, True, PRETO)
        TELA.blit(texto_vitoria, (LARGURA // 2 - 150, ALTURA // 2))
        som_vitoria.play()
        pygame.display.flip()
        time.sleep(2)  # Espera 2 segundos antes de reiniciar
        lutador1.vida = 100
        lutador2.vida = 100
        vencedor = None
    else:
        # Captura eventos do teclado
        teclas = pygame.key.get_pressed()

        # Movimento do Lutador 1
        if teclas[pygame.K_a]:  # Esquerda
            lutador1.mover("esquerda")
        if teclas[pygame.K_d]:  # Direita
            lutador1.mover("direita")
        if teclas[pygame.K_w]:  # Defesa
            lutador1.defendendo = True
        if teclas[pygame.K_SPACE]:  # Ataque
            lutador1.atacar(lutador2)

        # Movimento do Lutador 2
        if teclas[pygame.K_LEFT]:  # Esquerda
            lutador2.mover("esquerda")
        if teclas[pygame.K_RIGHT]:  # Direita
            lutador2.mover("direita")
        if teclas[pygame.K_UP]:  # Defesa
            lutador2.defendendo = True
        if teclas[pygame.K_RETURN]:  # Ataque
            lutador2.atacar(lutador1)

    # Libera defesa quando as teclas não estiverem pressionadas
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w:
                lutador1.defendendo = False
            if evento.key == pygame.K_UP:
                lutador2.defendendo = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
