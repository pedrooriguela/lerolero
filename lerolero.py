"""
gerador de lero lero

gera frases de efeito sem sentido real
"""
import random

# Cada frase é composta por 3 partes aleatorias,
# aqui , listas de possibilidades para cada uma das partes

parte1 = ["Caros amigos, ", "Por outro lado, ", "Assim mesmo, ", "No entanto, não podemos esquecer que ", "Do mesmo modo, ", "A prática cotidiana prova que ", "Nunca é demais lembrar o peso e o significado destes problemas, uma vez que ", "As experiências acumuladas demonstram que ", "Acima de tudo, é fundamental ressaltar que "]
parte2 = ["a execução dos pontos do programa ", "o novo modelo estrutural aqui preconizado ", "o desenvolvimento contínuo de distintas formas de atuação ", "a constante divulgação das informações ", "a consolidação das estruturas ", "a consulta aos diversos militantes ", "o início da atividade geral de formação de atitudes ", "o desafiador cenário globalizado ", "a mobilidade dos capitais internacionais "]
parte3 = ["nos obriga à análise ", "cumpre um papel essencial na formulação ", "exige a precisão e a definição ", "auxilia a preparação e a composição ", "garante a contribuição de um grupo importante na determinação ", "assume importantes posições na definição ", "facilita a criação ", "obstaculiza a apreciação da importância ", "oferece uma interessante oportunidade para verificação "]

lingua = int(input("Digite 1 para português ou 2 para inglês: "))

if lingua == 2:
    parte1 = ["Dear friends, ", "On the other hand, ", "In the same way, ", "However, we can not forget that ", "The daily practice proves that ", "It is never too much to remember the weight and the meaning of these problems, since ", "The accumulated experiences demonstrate that ", "Above all, it is essential to emphasize that "]
    parte2 = ["Doing the points of the program ", "The new structural model here recommended ", "The continuous development of different forms of action ", "The constant dissemination of information ", "The consolidation of structures ", "Consulting the various militants ", "The beginning of the general activity of attitude formation ", "The challenging globalized scenario ", "The mobility of international capitals "]
    parte3 = ["obliges us to analyze ", "plays an essential role in the formulation ", "requires precision and definition ", "assists in the preparation and composition ", "guarantees the contribution of an important group in the determination ", "assumes important positions in the definition ", "facilitates the creation ", "obstructs the appreciation of the importance ", "offers an interesting opportunity for verification "]

# combina as partes aleatoriamente
print (random.choice(parte1), random.choice(parte2), random.choice(parte3))