import math 

N = int(input())

e = math.e
respostas = []

for _ in range(N):
    L = int(input())
    
    rot = L / 60
    prob = (e ** (-rot)) * 100
    
    respostas.append(prob)

for r in respostas:
    print(f"{r:.2f}%")