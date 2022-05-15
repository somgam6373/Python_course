import sympy as sp
x = sp.Symbol('x')
fx = (sp.exp(2*x)-1)/(sp.exp(x)+1)
gx = sp.Abs(sp.sin(x))
kx = x*sp.sqrt(x**2 + 2)
px = sp.exp(x) * sp.sin(x)

print("The answer is:", sp.integrate(fx,(x,0,2)))
print("The answer is:", sp.integrate(gx,(x,-sp.pi,sp.pi)))
print("The answer is:", sp.integrate(kx,(x,1,3)))
print("The answer is:", sp.integrate(px,(x,0,sp.pi/2)))


