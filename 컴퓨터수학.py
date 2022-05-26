import sympy as sp
x = sp.Symbol('x')
fx = x+1/x-1/x**2
gx = (sp.sqrt(x) + 4)/x
print(sp.integrate(fx,x))
print(sp.integrate(gx,x))

