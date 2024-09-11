# -*- coding: utf-8 -*-
"""aula9_limites.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AZ2eOUnuPZudoE6-jB2tIn14l7ujcT4i

#Limites
"""

import numpy as np
import pandas as pd
import sympy as sp

"""$\lim_{x \to 1} \frac{x^2 + x -2}{x-2}$"""

#encontrar x
x = sp.Symbol('x')
x

#definir limite
funcao = (x**2 + x - 2) / (x - 1)
funcao

#encontrar limite
sp.limit(funcao, x, 1)

#grafico para a função
sp.plot(funcao)

"""## Exemplo 2

$\lim_{x \to 2} \frac{x+1}{x-2}$
"""

#Definir x

x = sp.Symbol('x')
x

#definir funcao
funcao = (x+1) / (x-2)
funcao

#encontrar limite
sp.limit(funcao, x, 2)

#grafico
sp.plot(funcao, xlim = [-3.5, 5], ylim =[-15, 15])



"""$\lim_{x \to 0} 2+3x$

$\lim_{x \to \infty} 2+3x$
"""

#Definir x

x = sp.Symbol('x')
x

funcao = 2 + 3*x
funcao

#limite tendendo a zero
sp.limit(funcao, x, 0)

sp.limit(funcao, x, sp.oo)

"""#Exemplos 5 e 6

$\lim_{x \to 0} \beta_0 + \beta_1 x$

$\lim_{x \to ∞} \beta_0 + \beta_1 x$
"""

# definir simbolos

x = sp.Symbol('x')
beta0 = sp.Symbol('beta_0')
beta1 = sp.Symbol('beta_1')
beta0

#definir funcao
funcao = beta0 + beta1*x
funcao

#limit x tend 0
sp.limit(funcao, x, 0)

sp.limit(funcao, x, sp.oo)





"""# exemplos 7 e 6"""

#definir x
x = sp.Symbol('x')
x

#definir funcao
funcao = 1 / (1 + sp.exp(-x))
funcao

#limit x tend 0
sp.limit(funcao, x, 0)

#limit x tend 0
sp.limit(funcao, x, sp.oo)

sp.limit(funcao, x, -sp.oo)

#grafico
sp.plot(funcao)