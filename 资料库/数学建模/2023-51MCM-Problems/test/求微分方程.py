import math
from sympy import symbols
from sympy import Derivative,pprint
import sympy
from sympy import pi
from sympy import solve
from sympy.abc import m,t,r,c,s,g,v,rho,omega
r=sympy.Function('r')
v=Derivative(r(t),t)
print(1)
# print(sympy.dsolve(-m*Derivative(r(t),t,2)+m*g-1/2*rho*c*s*v**2+1/2*c,r(t)))
from sympy.vector import CoordSys3D
from sympy.vector import Vector
N = CoordSys3D('N')
x=sympy.Function('x')
y=sympy.Function('y')
z=sympy.Function('z')
print(x(t))
r=x*N.i+y*N.j+z*N.k
pprint(Derivative(r(t),t))

# print(N.origin,N.i+Vector.zero)