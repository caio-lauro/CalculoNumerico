# Repositório referente às aulas de Cálculo numérico.

## Funções trigonométricas:
Aproximação das funções trigonométricas (em radianos) a partir do polinômio de MaClaurin.

### Explicação breve:
Em ambas as funções (sen, cos) `x` é um número ponto-flutuante em radianos, e `n` é o número de termos (iterações) do algoritmo do polinômio de MaClaurin.


## Polinômio de Lagrange
Implementação de algoritmo do polinômio de Lagrange em python, usando as bibliotecas:
* `Sympy`: para lidar com os produtos e adições de expressões polinomiais;
* `numbers`: para incluir a classe `Number`;
* `functools`: para incluir a função `reduce`, que foi utilizada em diversos cálculos;

### Explicação breve:
Implementação da classe `Polinomio`, cujo objeto é criado a partir de uma lista de tuplas de números (`PONTOS`) e (opcionalmente) uma quantidade de casas decimais de precisão (`precisao`) para o resultado final (durante os cálculos são usadas a maior quantidade possível).\
A classe tem um método chamado `getCoeficientes` que é responsável por obter os coeficientes do polinômio de Lagrange na ordem decrescente de grau, que farão parte da própria classe.\
O outro método relevante da classe é o `interpolarX`, que é responsável por interpolar o valor de X __independentemente__ do valor de `x` fornecido pelo usuário, mesmo que extrapole os limites dos pontos, o que irá apenas fornecer um aviso, para evitar confusão. Escolhi esta implementação por uma futura necessidade de demonstrar como o polinômio se torna impreciso fora de seus pontos limite.

## PLA - Polinômio de Lagrange Autoimplementado
Implementação de algoritmo do polinômio de Lagrange em python, usando as bibliotecas:
* `numbers`: para incluir a classe `Number`;
* `__future__`: para autoreferenciar polinômios dentro da classe `Polinomio`.

### Explicação breve:
Implementação da classe `Polinomio` dentro do script `polinomio_class.py`, cujo objetivo é realizar a multiplicação e soma de polinômios para produzir o polinômio de Lagrange. A classe também é capaz de lidar com a divisão de um polinômio por inteiro e exponenciação a índices não-negativos e, além disso, pode conter uma quantidade de casas decimais de precisão `casasDecimaisPrecisao`, que permite realizar os devidos arredondamentos nos coeficientes do polinômio quando a função `fitCoeffs` é chamada. Ademais, a classe contém um outro método chamado `subs`, que pode realizar a substituição de um valor `x` no polinômio.\
A partir de `polinomio_class.py`, foi criado um outro script `lagrange.py`, que implementa a função `Lagrange`,  que utiliza da classe Polinômio para produzir o polinômio de Lagrange, a partir de um algoritmo similar implementado no outro script `polinomio_lagrange.py`. A função aceita como parâmetros `pontos` e `casasDecimaisPrecisao`, que são os pontos e a quantidade de casas decimais de precisão fornecidos pelo usuário, e retorna um objeto `Polinomio` que é o próprio polinômio de Lagrange.\
Por fim, dado o polinômio, o usuário pode usar de seu método `subs` para realizar uma substituição de um ponto `x` no polinômio, tendo em vista os limites de interpolação em mente, visto que o sistema nesse quesito não impede e nem avisa o usuário se o ponto estiver fora dos limites.