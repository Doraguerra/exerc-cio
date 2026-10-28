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




