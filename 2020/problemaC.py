# O numero de Cidades = N 

N = int(input())

# N - 1 representa que cada vertice pode se conectar a todos os outros exceto ele mesmo, ou seja, N - 1 conexões possíveis para cada vértice.
# Multiplicamos por N porque cada vértice tem N - 1 conexões possíveis, e há N vértices no total.
# P = ao número total de conexões possíveis entre as cidades, considerando que cada cidade pode se conectar a todas as outras, exceto a si mesma.

P = N * (N - 1)

# Dividimos por 2 porque cada conexão é contada duas vezes (A se conecta a B e B se conecta a A são a mesma conexão).

K = P / 2

print(f"{K:.0f}")