import sympy

from numbers import Number
from functools import reduce

class Polinomio:
    def __init__(self, PONTOS: list[tuple[Number, Number]], precisao = 3):
        self.PONTOS = PONTOS
        self.valoresX:list[Number] = [i[0] for i in PONTOS]
        self.valoresY:list[Number] = [i[1] for i in PONTOS]
        self.precisao:int = precisao
        self.Grau:int = len(self.valoresX) - 1

        self.coeficientes:list[Number] = list(map(lambda x: round(x, self.precisao), self.getCoeficientes()))
    
    def __str__(self) -> str:
        s = f"P{self.Grau}(x) = "
        for i in range(len(self.coeficientes) - 1):
            if i > 0 and self.coeficientes[i] > 0:
                s += ' + '
            elif i > 0 and self.coeficientes[i] < 0:
                s += ' - '

            s += f"{abs(self.coeficientes[i])}x" if abs(self.coeficientes[i]) != 1.0 else "x"
            if self.Grau - i > 1:
                s += f"^{self.Grau - i}"

        if self.coeficientes[-1] > 0:
            s += f' + {self.coeficientes[-1]}'
        elif self.coeficientes[-1] < 0:
            s += f' - {-self.coeficientes[-1]}'

        return s
    
    def interpolarX(self, x: Number) -> Number:
        minX:Number = min(self.valoresX)
        maxX:Number = max(self.valoresX)

        if (x > maxX or x < minX):
            print("Não devemos interpolar valores fora dos pontos conhecidos... mas:")
        
        grausX:list[Number] = [x**i for i in range(self.Grau, -1, -1)]
        
        valorNumerico: Number = reduce(lambda a, b: a + b, [grausX[i] * self.coeficientes[i] for i in range(self.Grau + 1)])
        return round(valorNumerico, self.precisao)
    
    def getCoeficientes(self):
        x = sympy.Symbol('x')
        termos = []
        for i in range(self.Grau + 1):
            # Numerador do i-ésimo termo
            elementosNumerador = [(x - n) for n in self.valoresX if n != self.valoresX[i]]
            numerador = reduce(lambda a, b: a * b, elementosNumerador)

            # Multiplicar por yi
            numerador *= self.valoresY[i]

            # Denominador do termo
            elementosDenominador = [(self.valoresX[i] - n) for n in self.valoresX if n != self.valoresX[i]]
            denominador = reduce(lambda a, b: a * b, elementosDenominador)
            
            termo = numerador.expand() / denominador
            termos.append(termo)

        polinomio = reduce(lambda x, y: x + y, termos)
        coeficientes = list(map(lambda x: float(x), polinomio.as_poly().coeffs()))

        return coeficientes

pontosExercicios = [
    [(-1, 14.5), (0, 7.5), (1.5, 4.5)],
    [(0, 5), (2, -3), (4, 13)],
    [(0, 2), (0.3, 2.405), (0.5, 2.8244), (0.9, 4.2136)],
]

for pontos in pontosExercicios:
    pnx = Polinomio(pontos)
    print(pnx)
    x = 2
    interpolacao = pnx.interpolarX(x)
    print(f"Interpolacao para x = {x} é: {interpolacao}\n")
