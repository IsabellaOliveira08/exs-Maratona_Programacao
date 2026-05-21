N = int(input())
matriz = [['A', 1], ['N', 8], ['I', 6], ['T', 3]]
todas_respostas = [] 


for _ in range(N):
    palavra = input().upper()
    codificada = []
    
    for letra in palavra:
        achou = False
        for item in matriz:
            if letra == item[0]:
                codificada.append(str(item[1]))
                achou = True
                break 
                
        if not achou:   
            codificada.append("#") 

    todas_respostas.append(''.join(codificada))


for resposta in todas_respostas:
    print(resposta)