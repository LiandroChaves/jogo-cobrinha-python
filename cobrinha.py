import pygame
import random

# Inicializando o Pygame
pygame.init()

# Definindo as cores
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
CINZA = (229, 229, 229)

# Dimensões da tela
largura = 800
altura = 600
tamanho = 20
velocidade = 10

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

def mostrar_placar(pontos):
    fonte = pygame.font.SysFont('Arial', 30)
    texto = fonte.render(f'Pontuação: {pontos}', True, PRETO)
    tela.blit(texto, [0, 0])

def mostrar_mensagem(texto):
    fonte = pygame.font.SysFont('Arial', 50)
    mensagem = fonte.render(texto, True, VERMELHO)
    tela.blit(mensagem, [largura // 6, altura // 3])
    pygame.display.update()
    pygame.time.delay(2000)

def perguntar_continuar():
    fonte = pygame.font.SysFont('Arial', 30)
    continuar = True

    while continuar:
        tela.fill(PRETO)
        mensagem = fonte.render("Deseja continuar? (S/N)", True, BRANCO)
        tela.blit(mensagem, [largura // 4, altura // 3])
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:
                    return True
                elif evento.key == pygame.K_n:
                    return False

def jogo():
    while True:
        x = largura // 2
        y = altura // 2
        x_mudanca = 0
        y_mudanca = 0

        cobra = []
        comprimento = 1

        comida_x = round(random.randrange(0, largura - tamanho) / 20) * 20
        comida_y = round(random.randrange(0, altura - tamanho) / 20) * 20

        pontos = 0

        clock = pygame.time.Clock()

        executando = True
        while executando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    executando = False
                    pygame.quit()
                    quit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT and x_mudanca == 0:
                        x_mudanca = -tamanho
                        y_mudanca = 0
                    elif evento.key == pygame.K_RIGHT and x_mudanca == 0:
                        x_mudanca = tamanho
                        y_mudanca = 0
                    elif evento.key == pygame.K_UP and y_mudanca == 0:
                        y_mudanca = -tamanho
                        x_mudanca = 0
                    elif evento.key == pygame.K_DOWN and y_mudanca == 0:
                        y_mudanca = tamanho
                        x_mudanca = 0

            x += x_mudanca
            y += y_mudanca

            if x < 0 or x >= largura or y < 0 or y >= altura:
                mostrar_mensagem(f'Game Over! Pontuação: {pontos}')
                executando = False

            cabeca = [x, y]
            cobra.append(cabeca)

            if len(cobra) > comprimento:
                del cobra[0]

            for parte in cobra[:-1]:
                if parte == cabeca:
                    mostrar_mensagem(f'Game Over! Pontuação: {pontos}')
                    executando = False

            if x == comida_x and y == comida_y:
                comida_x = round(random.randrange(0, largura - tamanho) / 20) * 20
                comida_y = round(random.randrange(0, altura - tamanho) / 20) * 20
                comprimento += 1
                pontos += 1

            tela.fill(CINZA)
            pygame.draw.rect(tela, VERDE, [comida_x, comida_y, tamanho, tamanho])

            for i, parte in enumerate(cobra):
                if i == len(cobra) - 1:
                    pygame.draw.rect(tela, BRANCO, [parte[0], parte[1], tamanho, tamanho])
                else:
                    cor_corpo = PRETO if i % 2 == 0 else VERMELHO
                    pygame.draw.rect(tela, cor_corpo, [parte[0], parte[1], tamanho, tamanho])

            mostrar_placar(pontos)

            pygame.display.update()
            clock.tick(velocidade)

        if not perguntar_continuar():
            break

    pygame.quit()
    quit()

# Executando o jogo
jogo()
