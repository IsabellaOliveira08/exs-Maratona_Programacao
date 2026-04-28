N = int(input())

# N - 1 representa que cada vertice pode se conectar a todos os outros exceto ele mesmo, ou seja, N - 1 conexões possíveis para cada vértice.

P = N * (N - 1)

# Dividimos por 2 porque cada conexão é contada duas vezes (A se conecta a B e B se conecta a A são a mesma conexão).

K = P / 2

print(f"{K:.0f}")