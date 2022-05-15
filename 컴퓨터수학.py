#factor는 인수분해를 의미함

import sympy as sp
x = sp.Symbol('x')
a = sp.Symbol('a')
alpha = sp.Symbol('alpha')
beta = sp.Symbol('beta')

fx = a*(x-alpha) * (x-beta)
print(sp.factor(sp.integrate(fx, (x,alpha,beta))))