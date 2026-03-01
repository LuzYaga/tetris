import pygame
import random
from config import *

#Tabuleiro é uma lista de 20 listas, cada uma com 10 zeros.
#Cada 0 representa uma célula vazia.
#Futuramente um número diferente de zero vai representar uma peça colorida.
#Cria o tabuleiro - lista de listas com células vazias
tabuleiro = [[0] * COLUNAS for _ in range(LINHAS)]
pontuacao = 0
game_over = False

def desenhar_tabuleiro(tela, offset_x=0, offset_y=0):
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            cor = tabuleiro[linha][coluna]
            x = coluna * TAMANHO_BLOCO + offset_x
            y = linha * TAMANHO_BLOCO + offset_y
            if cor:
                pygame.draw.rect(tela, cor, (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO))
            #O 1 no final significa que só desenha a borda, não preenche
            pygame.draw.rect(tela, CINZA, (x,y,TAMANHO_BLOCO, TAMANHO_BLOCO), 1)

def nova_peca():
    indice = random.randint(0, len(PECAS) - 1)
    forma = PECAS[indice]
    cor = CORES[indice]
    peca = {
        "forma": forma,
        "cor": cor,
        "linha": 0,
        "coluna": COLUNAS // 2 - 1
    }
    return peca

def desenhar_peca(tela, peca, offset_x=0, offset_y=0):
    for bloco in peca["forma"]:
        linha = peca["linha"] + bloco[0]
        coluna = peca["coluna"] + bloco[1]
        x = coluna * TAMANHO_BLOCO + offset_x
        y = linha * TAMANHO_BLOCO + offset_y
        pygame.draw.rect(tela, peca["cor"], (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO))

def peca_pode_mover(peca, linhas_extra=0, colunas_extra=0):
    for bloco in peca["forma"]:
        nova_linha  = peca["linha"]  + bloco[0] + linhas_extra
        nova_coluna = peca["coluna"] + bloco[1] + colunas_extra
        # Saiu do tabuleiro?
        if nova_linha >= LINHAS or nova_coluna < 0 or nova_coluna >= COLUNAS:
            return False
        #Verifica se já tem uma peça fixada nessa célula
        if tabuleiro[nova_linha][nova_coluna]:
            return False
    return True

def girar_peca(peca):
    nova_forma = []
    for bloco in peca["forma"]:
        nova_linha  =  bloco[1]
        nova_coluna = -bloco[0]
        nova_forma.append([nova_linha, nova_coluna])

    # Normaliza para que não fique com coordenadas negativas
    min_coluna = min(b[1] for b in nova_forma)
    min_linha  = min(b[0] for b in nova_forma)
    nova_forma = [[b[0] - min_linha, b[1] - min_coluna] for b in nova_forma]

    # Cria uma peça temporária para testar se a rotação é válida
    peca_teste = {
        "forma": nova_forma,
        "cor": peca["cor"],
        "linha": peca["linha"],
        "coluna": peca["coluna"]
    }

    # Só rotaciona se couber no tabuleiro
    if peca_pode_mover(peca_teste):
        peca["forma"] = nova_forma

def fixar_peca(peca):
    for bloco in peca["forma"]:
        linha = peca["linha"] + bloco[0]
        coluna = peca["coluna"] + bloco[1]
        #salva a cor da peça no tabuleiro
        tabuleiro[linha][coluna] = peca["cor"]

nivel = 1

def limpar_linhas():
    global pontuacao, nivel
    linhas_completas = []

    for linha in range(LINHAS):
        #VERIFICA SE TODAS AS CÉLULAS DA LINHA ESTÃO PREENCHIDAS
        if all(tabuleiro[linha][coluna] for coluna in range(COLUNAS)):
            linhas_completas.append(linha)

    for linha in linhas_completas:
        #REMOVE A LINHA COMPLETA
        del tabuleiro[linha]
        #Adiciona uma linha vazia no topo
        tabuleiro.insert(0, [0] * COLUNAS)

    # Pontuação: mais linhas de uma vez = mais pontos
    if len(linhas_completas) == 1:
        pontuacao += 100
    elif len(linhas_completas) == 2:
        pontuacao += 300
    elif len(linhas_completas) == 3:
        pontuacao += 500
    elif len(linhas_completas) == 4:
        pontuacao += 800

    #Atualiza o nível a cada 500 pontos
    nivel = pontuacao // 500 + 1
def verificar_game_over(peca):
    # Se a nova peça já começa numa célula ocupada, acabou o jogo
    for bloco in peca["forma"]:
        linha  = peca["linha"]  + bloco[0]
        coluna = peca["coluna"] + bloco[1]
        if tabuleiro[linha][coluna]:
            return True
    return False

def desenhar_pontuacao(tela, fonte, offset_x=0, offset_y=0):
    texto = fonte.render(f"Score: {pontuacao}", True, VERDE)
    tela.blit(texto, (10 +offset_x, 10 + offset_y))

def desenhar_game_over(tela, fonte, offset_x=0, offset_y=0):
    # Desenha o retângulo cinza por trás do texto
    superficie = pygame.Surface((LARGURA - 80, 100))
    superficie.set_alpha(200)
    superficie.fill(CINZA)
    tela.blit(superficie, (40 + offset_x, ALTURA // 2 - 60 + offset_y))  # mesma posição x=40))

    texto1 = fonte.render("GAME OVER", True, VERMELHO)
    texto2 = fonte.render("Press R to restart", True, BRANCO)
    tela.blit(texto1, (LARGURA // 2 - texto1.get_width() // 2 + offset_x, ALTURA // 2 - 50 + offset_y))
    tela.blit(texto2, (LARGURA // 2 - texto2.get_width() // 2 + offset_x, ALTURA // 2 + offset_y))

def reiniciar():
    global tabuleiro, pontuacao, game_over
    tabuleiro = [[0] * COLUNAS for _ in range(LINHAS)]
    pontuacao = 0
    nivel = 1
    return False
