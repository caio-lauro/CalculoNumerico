from numbers import Number

from .polinomio_class import Polinomio

def Lagrange(pontos:list[Number], casasDecimaisPrecisao: int = 3) -> Polinomio:
    polinomio = Polinomio([0], casasDecimaisPrecisao)
    
    for i in range(len(pontos)):
        ipoly = Polinomio([1])
        denominador = 1
        for j in range(len(pontos)):
            if i == j:
                continue

            jpoly = Polinomio([1,-(pontos[j][0])])
            ipoly *= jpoly
            denominador *= (pontos[i][0] - pontos[j][0])

        ipoly *= pontos[i][1]
        ipoly /= (denominador)

        polinomio += ipoly

    return Polinomio(polinomio.fitCoeffs())
