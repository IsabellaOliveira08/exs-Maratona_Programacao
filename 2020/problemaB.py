# Lê a quantidade total de alunos disponíveis (ex: se digitar 3, os alunos serão 1, 2 e 3)
total_alunos = int(input("")) 

# --- LAÇO PRINCIPAL: DEFINE O PRIMEIRO ALUNO DO GRUPO ---
# Este loop garante que cada aluno comece seu próprio conjunto de combinações.
# range(1, total_alunos + 1) gera os números de 1 até N.
for aluno_fixo in range(1, total_alunos + 1):

    # Inicializa a pilha para a Busca em Profundidade (DFS).
    # Cada elemento da pilha é uma tupla: (próximo_aluno_a_decidir, grupo_formado_até_agora)
    # Começamos forçando o 'aluno_fixo' a estar no grupo e o próximo a ser avaliado é o 'aluno_fixo + 1'.
    pilha = [(aluno_fixo + 1, [aluno_fixo])]

    # Enquanto a pilha não estiver vazia, continuamos explorando as combinações
    while pilha:

        # Acessa o elemento que está no topo da pilha (o último índice: -1)
        proximo_aluno, grupo_atual = pilha[-1]

        # Simula o comportamento de um .pop(): remove o elemento do topo da pilha após lê-lo
        del pilha[-1]

        # --- CASO BASE: FIM DA LINHA DE DECISÃO ---
        # Se o próximo aluno a ser avaliado passar do limite total de alunos,
        # significa que já tomamos uma decisão (Sim ou Não) para todos os alunos possíveis.
        if proximo_aluno > total_alunos:
            # map(str, grupo_atual) converte os números do grupo em texto
            # " ".join(...) junta os números com um espaço entre eles (ex: [1, 2] vira "1 2")
            print(" ".join(map(str, grupo_atual)) + " ")
            continue  # Pula para a próxima combinação da pilha

        # --- DECISÃO 1: NÃO INCLUIR O PRÓXIMO ALUNO ---
        # Cria uma cópia idêntica do grupo atual para não modificar o original (.copy())
        grupo_sem = grupo_atual.copy()
        # Adiciona na pilha a instrução de avaliar o próximo número (+ 1) sem alterar o grupo
        pilha.append((proximo_aluno + 1, grupo_sem))

        # --- DECISÃO 2: INCLUIR O PRÓXIMO ALUNO ---
        # Cria outra cópia idêntica do grupo atual
        grupo_com = grupo_atual.copy()
        # Adiciona (inclui) o próximo aluno neste novo grupo
        grupo_com.append(proximo_aluno)
        # Adiciona na pilha a instrução de avaliar o próximo número (+ 1) levando este aluno junto
        pilha.append((proximo_aluno + 1, grupo_com))
        
        # --- EXPLICAÇÃO DO FLUXO (ÁRVORE DE DECISÃO) ---
        # Como a pilha processa quem foi adicionado POR ÚLTIMO (LIFO), o código vai 
        # explorar primeiro todo o caminho de "INCLUIR" (grupo_com) até o final, 
        # para só depois voltar desfazendo as escolhas e testando os caminhos de "NÃO INCLUIR".
        #
        # Exemplo visual que está no seu próprio comentário para N = 3:
        # [1]
        # ├── sem 2 → [1]
        # │   ├── sem 3 → [1]
        # │   └── com 3 → [1, 3]
        # └── com 2 → [1, 2]         <-- Entrou por último na pilha, é o primeiro a ser expandido
        #     ├── sem 3 → [1, 2]
        #     └── com 3 → [1, 2, 3]  <-- Chega ao fim (imprime "1 2 3"), depois volta para "1 2", etc.