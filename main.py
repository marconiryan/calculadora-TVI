from math import sin
import numpy
import matplotlib.pyplot as plt


def conta(P1: float, P2: float) -> float:
    if equacao(P1) * equacao(P2) < 0:
        menor, maior = P1, P2
        plt.plot(P1, equacao(P1), "o", P2, equacao(P2), "o")
        if equacao(P1) > 0:
            menor, maior = P2, P1
        while equacao(maior) > 0.1:
            media = (maior + menor) / 2
            if equacao(media) < 0:
                menor = media
            else:
                maior = media
        print(maior)
        return maior


equacao = lambda x: x ** 3 + 5 * sin(x) + 2 * x + 4

Ponto1 = float(input("Ponto 1: "))
Ponto2 = float(input("Ponto 2: "))
X = numpy.arange(Ponto1, Ponto2 + 1)
Y = list(map(equacao, X))
plt.plot(X, Y)
plt.plot(conta(Ponto1, Ponto2), 0, 'o')
plt.show()
