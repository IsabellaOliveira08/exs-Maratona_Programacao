

# Quantidade de alunos (1 até N)
total_alunos = int(input("")) 
# Utilizamos input para fazer a leitura

# Para cada aluno fixo (garantido no grupo)( aluxo_fixo -> Contador de 1 até N)
# O aluno fixo é o primeiro elemento do grupo, garantindo a ordem crescente dos grupos
for aluno_fixo in range(1, total_alunos + 1):

    # Pilha: (próximo_aluno, grupo_atual)
    pilha = [(aluno_fixo + 1, [aluno_fixo])]

    # Enquanto houver combinações ele continua
    while pilha:

        # Acessa o último elemento
        proximo_aluno, grupo_atual = pilha[-1]

        # Remove o último elemento 
        del pilha[-1]

        # Se não há mais alunos para decidir
        # Imprime o grupo atual e continua para a próxima iteração 
        # de forma bonita sem colchetes 
        if proximo_aluno > total_alunos:
            print(" ".join(map(str, grupo_atual)) + " ")
            continue

        # NÃO incluir o próximo aluno
        # Armazena o grupo atual sem o próximo aluno e o próximo aluno para a próxima iteração
        grupo_sem = grupo_atual.copy()
        pilha.append((proximo_aluno + 1, grupo_sem))

        # Incluir o próximo aluno
        grupo_com = grupo_atual.copy()
        grupo_com.append(proximo_aluno)
        pilha.append((proximo_aluno + 1, grupo_com))
        # [1]
        # ├── sem 2 → [1]
        # │   ├── sem 3 → [1]
        # │   └── com 3 → [1, 3]
        # └── com 2 → [1, 2]
        #     ├── sem 3 → [1, 2]
        #     └── com 3 → [1, 2, 3]
