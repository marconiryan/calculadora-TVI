from math import sin
import numpy as np
import matplotlib.pyplot as graph


def conta(P1: float, P2: float) -> Float:
    if equacao(P1) * equacao(P2) < 0:
        menor, maior = P1, P2
        if equacao(P1) > 0:
            menor, maior = P2, P1
        while round(equacao(maior), 5) != 0.0:
            media = (maior + menor) / 2
            if equacao(media) < 0:
                menor = media
            else:
                maior = media
        return maior


def grafico(P1: float, P2: float) -> None:
    x = np.linspace(P1, P2, 30)
    y = list(map(equacao, x))
    graph.stem(x, y, linefmt='cyan', markerfmt='D')
    graph.plot(x, y, color="g")
    graph.show()


if __name__ == "__main__":
    equacao = lambda x: x ** 3 + 5 * sin(x) + 2 * x + 4
    Ponto1 = float(input("Ponto 1: "))
    Ponto2 = float(input("Ponto 2: "))
    grafico(Ponto1, Ponto2)
    
