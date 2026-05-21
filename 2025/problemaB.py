N = int(input())
conjunto = []
semana = [["Segunda-feira",1,2], ["Terça-feira",3,4], ["Quarta-feira",5,6], ["Quinta-feira",7,8], ["Sexta-feira",9,0]]
carros = []
retorno = []
for _ in range(N): 
    D = str(input())
    P = str(input())
    carros.append((D, P))

N = len(carros)
for x in range(N):
    ultimo_digito = (carros[x][1])[-1]
    resp = ultimo_digito % 2
    dia = (carros[x][0])
    if dia = 
               