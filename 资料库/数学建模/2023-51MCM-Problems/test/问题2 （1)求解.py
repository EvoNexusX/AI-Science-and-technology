import sympy
from  sympy import ln,exp,sqrt,pprint,cos,tan,simplify,collect,pi
from sympy.abc import t,k,m,h,g,theta,H,x
Vfz=sympy.symbols('Vfz')
Vz=sympy.symbols('Vz')
Vfx=sympy.symbols('Vfx')
v=sympy.symbols('V')
vx=v*cos(theta)


# Sz=m/k*ln((exp(2*sqrt(k*g/m))+1)/2)-sqrt(m*g/k)*t+Vfz*t
# print(Sz)
# x=-H/tan(theta) - Vfx*ln(sqrt(exp(-2*Vfz*k*t/m - 2*Vz*k*t/m + 2*h*k/m) - 1) + exp(-Vfz*k*t/m - Vz*k*t/m + h*k/m))/sqrt(g*k/m) + h/tan(theta) + 10000 + m*ln(m)/k - m*ln(v*k*ln(sqrt(exp(-2*Vfz*k*t/m - 2*Vz*k*t/m + 2*h*k/m) - 1) + exp(-Vfz*k*t/m - Vz*k*t/m + h*k/m))*cos(theta)/sqrt(g*k/m) + m)/k
t =sympy.solve(ln(exp(k / m * (h - (Vfz + Vz) * t)) + sqrt(exp(2 * k / m * (h - (Vfz + Vz) * t)) - 1)) / sqrt(k * g / m)-t,t)
Sx=m/k*ln(k*vx*t+m)-m/k*ln(m)+Vfx*t
# print(Sx)
x=simplify(sympy.solve(H-h-tan(theta)*(10000-x-Sx),x)[0])
print(Sx)
d=sqrt((10000-x)**2+H**2)
print(x)
print(d)
the=0
# x=-H/tan(the) - Vfx*ln(sqrt(exp(-2*Vfz*k*t/m - 2*Vz*k*t/m + 2*h*k/m) - 1) + exp(-Vfz*k*t/m - Vz*k*t/m + h*k/m))/sqrt(g*k/m) + h/tan(the) + 10000 + m*ln(m)/k - m*ln(v*k*ln(sqrt(exp(-2*Vfz*k*t/m - 2*Vz*k*t/m + 2*h*k/m) - 1) + exp(-Vfz*k*t/m - Vz*k*t/m + h*k/m))*cos(the)/sqrt(g*k/m) + m)/k
# print(x)
H=800
v=(300+600)/3.6
# print(v)
# x=-H/
# from math import tan,pi,cos
# print(tan(pi/4))
# for i in range(1,11,1):
#     vx=v*cos(i*0.1*pi/2)
#     ta=tan(i*0.1*pi/2)
#     x = -H / ta - Vfx * ln(sqrt(exp(-2 * Vfz * k * t / m - 2 * Vz * k * t / m + 2 * h * k / m) - 1) + exp(
#         -Vfz * k * t / m - Vz * k * t / m + h * k / m)) / sqrt(g * k / m) + h / tan(the) + 10000 + m * ln(
#         m) / k - m * ln(v * k * ln(sqrt(exp(-2 * Vfz * k * t / m - 2 * Vz * k * t / m + 2 * h * k / m) - 1) + exp(
#         -Vfz * k * t / m - Vz * k * t / m + h * k / m)) * cos(the) / sqrt(g * k / m) + m) / k
#     print(x)
#     break
#     # for j in range(300,900,100):
#     #     x=-H



