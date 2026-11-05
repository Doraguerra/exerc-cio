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

def posicao_valida (frota, linha, coluna, orientacao, tamanho):
    posicao = define_posicoes(linha,coluna,orientacao,tamanho)
    tabuleiro_pronto = posiciona_frota(frota)
    for casa in posicao:
        if not(casa[0] < 10 and casa[1] < 10 and casa[0] >= 0 and casa[1] >= 0 and tabuleiro_pronto[casa[0]][casa[1]] == 0):
            return False
    return True


def afundados (dicionario, tabuleiro):
    acertos = 0
    contagem = 0
    for i in dicionario:
        for p in dicionario[i]:
            contagem = 0
            for a in p:
                if tabuleiro[a[0]][a[1]] == 'X':
                    contagem += 1
            if contagem == len(p):
                acertos += 1
    return acertos

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto