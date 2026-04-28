import math

# Número de entradas

N = int(input())

# Formula de Poisson ->

e = math.e

# λ representa a taxa média de eventos por unidade de tempo, que é dada por L / 60, onde L é o número de eventos em um minuto.
# Armazenamos as respostas em uma lista para imprimir depois, evitando a mistura de cálculos e saídas.

respostas = []

for _ in range(N):

    # Número de conexões em um minuto (L)

    L = int(input())

    # Calculamos a taxa média de eventos por unidade de tempo (λ) usando a fórmula λ = L / 60, onde L é o número de eventos em um minuto.

    rot = L / 60

    # A probabilidade de não ocorrer nenhum evento em um minuto é dada por P(X = 0) = (λ^0 * e^(-λ)) / 0!, que simplifica para P(X = 0) = e^(-λ).
    # Traduzindo isso elevamos e sobre rot negativo e multiplicamos por 100 para obter a porcentagem.

    prob = (e ** (-rot)) * 100

    respostas.append(prob)

for r in respostas:
    print(f"{r:.2f}%")
