def podar(individuos, tamPoblacionMaxima):
    #breakpoint()

    i = len(individuos) - 1

    while i > 0:
        if len(individuos) > tamPoblacionMaxima:
            individuos.pop(i)
        else:
            break
        i -= 1
    return individuos