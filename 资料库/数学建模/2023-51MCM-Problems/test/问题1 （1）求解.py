import sympy
from  sympy import ln,exp,sqrt,pprint,cos,tan
from sympy.abc import t,k,m,h,g,theta,H,x
Vfz=sympy.symbols('Vfz')
Vfx=sympy.symbols('Vfx')
v=sympy.symbols('V')
vx=v*cos(theta)
t=ln(exp(k/m*(h-Vfz*t))+sqrt(exp(2*k/m*(h-Vfz*t))-1))/sqrt(k*g/m)
print(t)

# Sz=m/k*ln((exp(2*sqrt(k*g/m))+1)/2)-sqrt(m*g/k)*t+Vfz*t
# print(Sz)

Sx=m/k*ln(k*vx*t+m)-m/k*ln(m)+Vfx*t
print(Sx)
print(sympy.solve(H-h-tan(theta)*(10000-x-Sx),x)[0])