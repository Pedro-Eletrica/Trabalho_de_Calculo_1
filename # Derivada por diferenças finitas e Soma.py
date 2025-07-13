# Derivada por diferenças finitas e Soma de Reiman
# Bibliotecas importadas para o código
from sympy import integrate, symbols
# Derivada por diferenças finitas



#Soma de Reiman
x = symbols('x')
função = (x**2)+(3*x)+10 
valorxinicial = 1
valorxfinal = 50
Soma_de_Reiman = integrate(função, (x, valorxinicial, valorxfinal))
print("Integral Definida=")
print(Soma_de_Reiman)