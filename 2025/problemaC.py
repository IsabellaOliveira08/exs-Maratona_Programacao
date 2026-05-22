# Lê a quantidade de palavras que o usuário deseja codificar
N = int(input())

# Tabela de conversão (Matriz/Lista de listas).
# Cada sublista associa uma letra a um número correspondente.
# Exemplo: 'A' vira 1, 'N' vira 8, etc. (Forma a palavra 'ANIT')
matriz = [['A', 1], ['N', 8], ['I', 6], ['T', 3]]

# Lista que vai guardar o resultado final de cada palavra já codificada
todas_respostas = [] 

# Laço que vai rodar N vezes, uma para cada palavra informada
for _ in range(N):
    # Lê a palavra e usa o método .upper() para transformá-la toda em MAIÚSCULAS.
    # Isso garante que 'a' ou 'A' funcionem da mesma forma na comparação.
    palavra = input().upper()
    
    # Lista temporária para guardar os caracteres codificados da palavra atual
    codificada = []
    
    # Passa por cada letra da palavra digitada, uma por uma
    for letra in palavra:
        achou = False  # Variável de controle (Flag) para saber se a letra existe na matriz
        
        # Percorre a matriz de conversão para procurar a letra atual
        for item in matriz:
            # item[0] é a letra da matriz (ex: 'A') e item[1] é o número (ex: 1)
            if letra == item[0]:
                # Se achou a letra, converte o número correspondente para texto (str)
                # e adiciona na lista da palavra atual
                codificada.append(str(item[1]))
                achou = True  # Sinaliza que a letra foi encontrada na tabela
                break         # Interrompe o laço da matriz, pois já achou o que queria
                
        # --- REGRA PARA LETRAS NÃO ENCONTRADAS ---
        # Se após passar por toda a matriz a flag 'achou' continuar Falsa,
        # significa que a letra não está na tabela de conversão (ex: letras 'B', 'C', 'X').
        if not achou:   
            codificada.append("#") # Substitui a letra desconhecida por um '#'

    # --- FINALIZAÇÃO DA PALAVRA ---
    # ''.join(codificada) junta todas as strings da lista em um texto só.
    # Exemplo: ['1', '#', '6', '3'] vira o texto "1#63"
    # Depois, adicionamos esse texto na nossa lista de respostas globais.
    todas_respostas.append(''.join(codificada))


# --- IMPRESSÃO DOS RESULTADOS ---
# Passa pela lista de respostas acumuladas e imprime cada palavra codificada, uma por linha
for resposta in todas_respostas:
    print(resposta)