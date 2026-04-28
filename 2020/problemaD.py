D = int(input())

entradas = []

for _ in range(D):
    H = int(input())
    entradas.append(H)

resultados = []

N = 500 

for H in entradas: 
    delta = H / N 
    volume = 0
    
    for i in range(N):
         T = i * delta
         Q = T * T - 2 * T + 1
         volume += Q * delta 
    
    resultados.append(volume)

for resp in resultados:
    print(f"{resp:.2f}")

# Não consegui 

