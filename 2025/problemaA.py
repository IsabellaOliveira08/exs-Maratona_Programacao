N = int(input())  
eventos = []

for _ in range(N):
    S = int(input())
    F = int(input())
    eventos.append((S, F))

eventos.sort(key=lambda e: e[1])

selecionados = []
ultimo_fim = -1

for s,f in eventos:
    if s >= ultimo_fim:
        selecionados.append((s,f))
        ultimo_fim = f

for s,f in selecionados:
    print(s,f)

