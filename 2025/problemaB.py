def resolver_rodizio():
    # --- DICIONÁRIOS DE MAPEAMENTO ---
    
    # Este dicionário converte o número recebido na entrada (0 a 4) 
    # para o nome do dia por extenso, exigido no formato de saída.
    dias_extenso = {
        0: "segunda-feira",
        1: "terça-feira",
        2: "quarta-feira",
        3: "quinta-feira",
        4: "sexta-feira"
    }
    
    # Mapeia quais dígitos finais de placa são PROIBIDOS em cada dia.
    # Usamos conjuntos (sets) `{}` porque a busca neles (`in`) é extremamente rápida.
    rodizio_proibido = {
        0: {1, 2},  # Segunda-feira: proibido terminar em 1 ou 2
        1: {3, 4},  # Terça-feira:   proibido terminar em 3 ou 4
        2: {5, 6},  # Quarta-feira:  proibido terminar em 5 ou 6
        3: {7, 8},  # Quinta-feira:  proibido terminar em 7 ou 8
        4: {0, 9}   # Sexta-feira:   proibido terminar em 0 ou 9
    }
    
    # --- ESTRUTURAS DE DADOS (PILHAS) ---
    
    # Criamos listas vazias para representar as garagens.
    # O enunciado diz: "o último a entrar é o primeiro a sair". 
    # Isso é o conceito de PILHA (LIFO - Last In, First Out), como uma pilha de pratos.
    garagem_A = []  # Armazenará os veículos de placas PARES
    garagem_B = []  # Armazenará os veículos de placas ÍMPARES
    
    # --- LEITURA DOS DADOS ---
    
    # input() lê o que o usuário digitou. 
    # .strip() remove espaços extras ou quebras de linha invisíveis (\n).
    # int(...) converte esse texto no número total de iterações (N).
    N = int(input().strip())

    # Este laço vai rodar exatamente N vezes (uma vez para cada veículo).
    for _ in range(N):
        # Como o dia e a placa estão em linhas separadas, chamamos o input() duas vezes:
        dia = int(input().strip())   # Lê a primeira linha (o número do dia)
        placa = input().strip()      # Lê a linha de baixo (o texto da placa, ex: "1234")
        
        # placa[-1] pega o ÚLTIMO caractere da string (o último dígito).
        # int(...) transforma esse caractere em um número inteiro para podermos fazer contas.
        ultimo_digito = int(placa[-1])
        
        # --- REGRA 3: CONSIDERAÇÃO DO RODÍZIO ---
        # Verifica se o último dígito está no conjunto de proibições daquele dia.
        # Exemplo: Se dia for 0 (segunda) e o dígito for 1, '1 in {1, 2}' é Verdadeiro.
        if ultimo_digito in rodizio_proibido[dia]:
            continue  # O comando 'continue' ignora o resto do laço e pula para o próximo veículo (descarta o registro)
        
        # --- REGRAS 1 e 4: DIRECIONAMENTO POR PARIDADE ---
        # Se o resto da divisão por 2 for zero, o número é PAR.
        if ultimo_digito % 2 == 0:
            # .append() adiciona um elemento no FINAL da lista (coloca no topo da pilha).
            # Salvamos uma tupla (placa, dia_por_extenso) para não perder as informações.
            garagem_A.append((placa, dias_extenso[dia]))
        else:
            # Se não for par, é ÍMPAR. Adiciona no final da garagem B.
            garagem_B.append((placa, dias_extenso[dia]))

    # --- PROCESSAMENTO DA SAÍDA ---
    
    # --- GARAGEM A (PARES) ---
    # 'if not garagem_A' verifica se a lista está vazia.
    if not garagem_A:
        print("estacionamento A vago...")
    else:
        # Enquanto a garagem A tiver elementos (não estiver vazia):
        while garagem_A:
            # O método .pop() remove e retorna o ÚLTIMO elemento da lista (o topo da pilha).
            # Isso garante a regra: "o último que entrou é o primeiro que sai".
            # Como salvamos uma tupla, fazemos a desestruturação nas variáveis 'placa' e 'dia_str'.
            placa, dia_str = garagem_A.pop()
            
            # Imprime no formato exigido: "A 1234 segunda-feira"
            print(f"A {placa} {dia_str}")
            
    # --- GARAGEM B (ÍMPARES) ---
    # Fazemos exatamente a mesma lógica para a garagem B.
    if not garagem_B:
        print("estacionamento B vago...")
    else:
        while garagem_B:
            # Retira o último que entrou na garagem B
            placa, dia_str = garagem_B.pop()
            print(f"B {placa} {dia_str}")

# Este bloco padrão garante que a função só execute se o arquivo for rodado diretamente.
if __name__ == "__main__":
    resolver_rodizio()