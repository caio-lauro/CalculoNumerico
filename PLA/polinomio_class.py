from __future__ import annotations
from numbers import Number

class Coeficiente:
    def __init__(self, coeficiente: Number, grau: int):
        self.coeficiente = coeficiente
        self.grau = grau
    
    def __str__(self) -> str:
        return str(self.coeficiente)
    
    def __repr__(self) -> str:
        return str(self.coeficiente)

class Polinomio:
    def __init__(self, coeficientes: list[Number] | list[Coeficiente], casasDecimaisPrecisao: int = 3):
        l = len(coeficientes)

        self.coeficientes:list[Coeficiente] = [] if isinstance(coeficientes[0], Number) else coeficientes
        self.grau = l - 1
        self.casasDecimaisPrecisao = casasDecimaisPrecisao
        if not self.coeficientes:
            for i in range(l):
                coeff = Coeficiente(coeficiente=coeficientes[i], grau=(self.grau - i))
                self.coeficientes.append(coeff)
    
    def fitCoeffs(self) -> list[Coeficiente]:
        for i in self.coeficientes:
            i.coeficiente = round(i.coeficiente, self.casasDecimaisPrecisao)
        return self.coeficientes
    
    def subs(self, x: Number) -> Number:
        ans: Number = 0
        for i in range(self.grau + 1):
            ans += (self.coeficientes[i].coeficiente) * (x**(self.grau - i))
        return ans

    def __len__(self) -> int:
        return len(self.coeficientes)

    def __str__(self) -> str:
        s:str = ""
        l:int = len(self.coeficientes)
        for i in range(l):
            if self.coeficientes[i].coeficiente == 0:
                continue

            if i != 0:
                s += "+ " if self.coeficientes[i].coeficiente > 0 else "- "
            elif self.coeficientes[i].coeficiente < 0:
                s += "-"

            if abs(self.coeficientes[i].coeficiente) != 1 or self.coeficientes[i].grau == 0:
                s += str(abs(self.coeficientes[i].coeficiente))
            if self.coeficientes[i].grau > 1:
                s += f"x^{self.coeficientes[i].grau}"
            elif self.coeficientes[i].grau == 1:
                s += "x"

            s += " "

        return s[:-1]
    
    def __add__(self, element: Polinomio | Number) -> Polinomio:
        if isinstance(element, Number):
            coeffs = [i.coeficiente for i in self.coeficientes]
            coeffs[-1] += element
            return Polinomio(coeffs)

        poly = element
        lenSelfCoeficientes:int = len(self.coeficientes)
        lenPoly:int = len(poly)
        maxLen:int = lenSelfCoeficientes if lenSelfCoeficientes > lenPoly else lenPoly

        new_poly = Polinomio([0] * maxLen)
        idxSelf, idxPoly = 0, 0
        for k in range(maxLen):
            if self.coeficientes[idxSelf].grau == new_poly.coeficientes[k].grau:
                new_poly.coeficientes[k].coeficiente += self.coeficientes[idxSelf].coeficiente
                idxSelf+=1
            if poly.coeficientes[idxPoly].grau == new_poly.coeficientes[k].grau:
                new_poly.coeficientes[k].coeficiente += poly.coeficientes[idxPoly].coeficiente
                idxPoly+=1

        while new_poly.coeficientes[0].coeficiente == 0:
            coeffs:list[int] = [i.coeficiente for i in new_poly.coeficientes[1:]]
            new_poly = Polinomio(coeffs)
        
        return new_poly

    def __sub__(self, element: Polinomio | Number) -> Polinomio:
        if isinstance(element, Number):
            return self.__add__(-element)

        poly = element
        for i in poly.coeficientes:
            i.coeficiente = -i.coeficiente
        return self.__add__(poly)
    
    def __mul__(self, element: Polinomio | Number) -> Polinomio:
        if isinstance(element, Number):
            coeffs = [(i.coeficiente * element) for i in self.coeficientes]
            return Polinomio(coeffs)
        
        poly = element
        grau: int = self.grau + poly.grau
        new_poly = Polinomio([0] * (grau+1))
        for i in self.coeficientes:
            for j in poly.coeficientes:
                multCoeff = i.coeficiente * j.coeficiente
                multGrau = i.grau + j.grau

                idx = 0
                while new_poly.coeficientes[idx].grau != multGrau:
                    idx+=1
                
                new_poly.coeficientes[idx].coeficiente += multCoeff
        
        return new_poly

    def __truediv__(self, num: Number) -> Polinomio:
        return self.__mul__(1/num)
    
    def __pow__(self, grau: Number) -> Polinomio | int:
        if grau == 0:
            return 1
        
        coeffs = [i.coeficiente for i in self.coeficientes]
        new_poly = Polinomio(coeffs)

        if grau == 1:
            return new_poly
        
        for i in range(grau - 1):
            new_poly = self.__mul__(new_poly)

        return new_poly