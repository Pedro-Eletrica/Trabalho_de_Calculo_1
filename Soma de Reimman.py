#Soma de Reiman
# Bibliotecas importadas para o código
from sympy import integrate, symbols
from sympy import tan, sec, sech, sin, cos, sinh, cosh, tanh, csc, csch, sqrt, sqrt_mod, euler, pi, limit, Limit, limit_seq, ln, log
#Soma de Reiman
x = symbols('x')
função = cos(x)
valorxinicial = 0
valorxfinal = pi
Soma_de_Reiman = integrate(função, (x, valorxinicial, valorxfinal))
print("Integral Definida=")
print(Soma_de_Reiman)