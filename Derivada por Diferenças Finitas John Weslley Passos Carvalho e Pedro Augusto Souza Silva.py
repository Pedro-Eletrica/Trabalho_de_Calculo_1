#Derivada por Diferenças Finitas
from sympy import Derivative, differentiate_finite, symbols, Symbol, difference_delta, diff
from sympy import tan, sec, sech, sin, cos, sinh, cosh, tanh, csc, csch, cot, coth, sqrt, sqrt_mod, euler, pi, limit, Limit, limit_seq, ln, log
from numpy import arange, linspace, random

# Dados da função
x = symbols('x') # Variável independente
função = x**2 + x - 2 # Função a ser derivada
x_deri = 5.2576 # Ponto da função o qual deseja saber a derivada

# Gerando lista de números
def gerar_lista(a1, r, n):
    return [a1 + i * r for i in range(n)]
a1 = 0 # Termo inicial da lista
r = 0.56 # Razão de espaçamento entre os valores de x da lista
n = 10 # Nº de termos da lista de X
lista_de_x = gerar_lista(a1, r, n) # Lista de termos do conjunto do domínio da função
print("Termos de x:", lista_de_x)

def aplicar_função_na_lista(lista_de_x, funcao_simbolica, variavel_simbolica):
    return [funcao_simbolica.subs(variavel_simbolica, x_val) for x_val in lista_de_x]
lista_de_y = aplicar_função_na_lista(lista_de_x, função, x) # Lista de termos do conjunto imagem da função
print("Termos de y:", lista_de_y)

print("Função=", função)
# Aproximação da Derivada usando Diferenças Finitas
fd1 = diff(função, x) # Derivada de primeira ordem da função
print("1ª Derivada=", fd1)
Diferenças_Finitas = differentiate_finite(função, x, points = lista_de_x, x0=x_deri) # Derivada de primeira ordem aproximada da função no ponto determinado
print("Diferenças Finitas 1ª Ordem=", Diferenças_Finitas)

fd2 = diff(fd1, x) # Derivada de segunda ordem da função
print("2ª Derivada=", fd2)
Diferenças_Finitas = differentiate_finite(fd1, x, points = lista_de_x, x0=x_deri) # Derivada de segunda ordem aproximada da função no ponto determinado
print("Diferenças Finitas 2ª Ordem=", Diferenças_Finitas)

fd3 = diff(fd2, x) # Derivada de terceira ordem da função
print("3ª Derivada=", fd3)
Diferenças_Finitas = differentiate_finite(fd2, x, points = lista_de_x, x0=x_deri) # Derivada de terceira ordem aproximada da função no ponto determinado
print("Diferenças Finitas 3ª Ordem=", Diferenças_Finitas)

fd4 = diff(fd3, x) # Derivada de quarta ordem da função
print("4ª Derivada=", fd4)
Diferenças_Finitas = differentiate_finite(fd3, x, points = lista_de_x, x0=x_deri) # Derivada de quarta ordem aproximada da função no ponto determinado
print("Diferenças Finitas 4ª Ordem=", Diferenças_Finitas)

fd5 = diff(fd4, x) # Derivada de quinta ordem da função
print("5ª Derivada=", fd5)
Diferenças_Finitas = differentiate_finite(fd4, x, points = lista_de_x, x0=x_deri) # Derivada de quinta ordem aproximada da função no ponto determinado
print("Diferenças Finitas 5ª Ordem=", Diferenças_Finitas)