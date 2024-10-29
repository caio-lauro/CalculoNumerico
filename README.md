# Repositório referente às aulas de Cálculo numérico.

## Funções trigonométricas:
Aproximação das funções trigonométricas (em radianos) a partir do polinômio de MaClaurin.

### Explicação breve:
Em ambas as funções (sen, cos) `x` é um número ponto-flutuante em radianos, e `n` é o número de termos (iterações) do algoritmo do polinômio de MaClaurin.


## Polinômio de Lagrange
Implementação de algoritmo do polinômio de Lagrange em python, usando as bibliotecas
* `Sympy`: para lidar com os produtos e adições de expressões polinomiais;
* `numbers`: para incluir a classe `Number`;
* `functools`: para incluir a função `reduce`, que foi utilizada em diversos cálculos;

### Explicação breve:
Implementação da classe `Polinomio`, cujo objeto é criado a partir de uma lista de tuplas de números (`PONTOS`) e (opcionalmente) uma quantidade de casas decimais de precisão (`precisao`) para o resultado final (durante os cálculos são usadas a maior quantidade possível).\
A classe tem um método chamado `getCoeficientes` que é responsável por obter os coeficientes do polinômio de Lagrange na ordem decrescente de grau, que farão parte da própria classe.\
O outro método relevante da classe é o `interpolarX`, que é responsável por interpolar o valor de X __independentemente__ do valor de `x` fornecido pelo usuário, mesmo que extrapole os limites dos pontos, o que irá apenas fornecer um aviso, para evitar confusão. Escolhi esta implementação por uma futura necessidade de demonstrar como o polinômio se torna impreciso fora de seus pontos limite.