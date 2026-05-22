import math

# Lê o número total de casos de teste (N) que serão avaliados
N = int(input())

# Guarda a constante matemática 'e' (Número de Euler, que vale aproximadamente 2.71828).
# Ela é a base dos logaritmos naturais e parte fundamental da fórmula de Poisson.
e = math.e

# Lista para armazenar as porcentagens calculadas de cada caso,
# garantindo que a exibição dos resultados aconteça toda junta no final.
respostas = []

# Laço que se repete N vezes, processando uma taxa de tráfego por vez
for _ in range(N):

    # Lê o número de eventos/conexões que ocorrem no intervalo de um minuto (L)
    L = int(input())

    # --- CÁLCULO DA TAXA POR SEGUNDO (λ - Lambda) ---
    # Como o enunciado ou o problema trabalha com a probabilidade por SEGUNDO,
    # dividimos o total do minuto por 60 para descobrir a taxa média por segundo (rot).
    rot = L / 60

    # --- FÓRMULA DE POISSON SIMPLIFICADA ---
    # A fórmula original de Poisson para k eventos é: P(X = k) = (λ^k * e^-λ) / k!
    # Como queremos a probabilidade de NÃO ocorrer nenhum evento (k = 0):
    # P(X = 0) = (λ^0 * e^-rot) / 0!
    # Como λ^0 é 1, e 0! também é 1, a fórmula se simplifica perfeitamente para: e^-rot
    
    # Calculamos e^(-rot) e multiplicamos por