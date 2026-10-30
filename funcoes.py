def define_posicoes(linha, coluna, orientação, tamanho):
    r = []
    s = 1
    if orientação == 'vertical':
        r = [[linha, coluna]]
        for i in range(tamanho - 1):
            r.append([linha + s, coluna])
            s += 1
    elif orientação == 'horizontal':
            r = [[linha, coluna]]
            for i in range(tamanho - 1):
                r.append([linha, coluna + s])
                s += 1
    return r


def preenche_frota (frota, nome, linha, coluna, orientacao,tamanho):
     posicao = define_posicoes(linha, coluna, orientacao, tamanho)
     if nome in frota:
        frota[nome].append(posicao)
     else:
        frota[nome] = []
        frota[nome].append(posicao)
     return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro_novo = [[0]*10 for n in range(10)]
    for i in frota:
        for l in frota[i]:
            for x in l:
                tabuleiro_novo[x[0]][x[1]] = 1
    return tabuleiro_novo

def afundados (dicionario, tabuleiro):
    acertos = 0
    contagem = 0
    for i in dicionario:
        for p in dicionario[i]:
            if tabuleiro[p] == 'X':
                contagem = 1
        if contagem == len(dicionario[i]):
            acertos += 1
    return acertos
