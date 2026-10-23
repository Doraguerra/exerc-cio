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
