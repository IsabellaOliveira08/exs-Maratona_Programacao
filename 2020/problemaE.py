import math

N = int(input())

# Formula de Poisson ->
e = math.e

# λ representa a taxa média de eventos por unidade de tempo, que é dada por L / 60, onde L é o número de eventos em um minuto.

respostas = []

for _ in range(N):
    L = int(input())

    rot = L / 60

    prob = (e ** (-rot)) * 100

    respostas.append(prob)

for r in respostas:
    print(f"{r:.2f}%")
