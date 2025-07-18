#Soma de Riemann
# Bibliotecas importadas para o código
from sympy import integrate, symbols
from sympy import tan, sec, sech, sin, cos, sinh, cosh, tanh, csc, csch, coth, cot, sqrt, sqrt_mod, euler, pi, limit, Limit, limit_seq, ln, log

x = symbols('x') # Variável independente
função = x**4 + 12*x**3 - 6*x**2 - x + 10 # Função a ser integrada
Primitiva = integrate(função, (x)) # Primitiva da função
valorxinferior = 3 # Limite inferior da integral
valorxsuperior = 8 # Limite superior da integral
Soma_de_Riemann = integrate(função, (x, valorxinferior, valorxsuperior)) # Integral Definida, também chamada de Integral de Riemann
print("f(x)=", função)
print("F(x)=", Primitiva, "+ C")
print("Limite Inferio=", valorxinferior)
print("limite Superior=", valorxsuperior)
print("Integral de Riemann/Integral Definida=", Soma_de_Riemann)