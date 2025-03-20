"""
gerador de lero lero

gera frases de efeito sem sentido real
"""
import random

# Cada frase é composta por 3 partes aleatorias,
# aqui , listas de possibilidades para cada uma das partes

parte1 = []
parte2 = []
parte3 = []

lingua = int(input("Digite 1 para português ou 2 para inglês: "))

if lingua == 2:
    parte1 = []
    parte2 = []
    parte3 = []

# combina as partes aleatoriamente
print (random.choice(parte1), random.choice(parte2), random.choice(parte3))