# Lê o número total de cidades (N) que existem no mapa
N = int(input())

# --- CÁLCULO DO NÚMERO TOTAL DE VÍNCULOS (DIRECIONADOS) ---
# N - 1 representa que cada cidade pode mandar uma estrada para todas as outras, 
# exceto para ela mesma. Se temos 4 cidades, cada uma tenta se conectar a 3 cidades.
#
# Multiplicamos isso pelo total de cidades (N). 
# P representará o número de conexões "de ida e volta" computadas individualmente.
# Exemplo: Se N = 4, temos 4 * 3 = 12 pontas de estradas saindo das cidades.
P = N * (N - 1)

# --- CORREÇÃO DE DUPLICIDADE (Combinação Não-Direcionada) ---
# Dividimos por 2 porque uma estrada entre a Cidade A e a Cidade B é exatamente 
# a mesma estrada que liga a Cidade B à Cidade A. 
# Sem essa divisão, estaríamos contando a mesma estrada duas vezes (ida e volta separadas).
#
# Na matemática, essa é a famosa fórmula da Combinação: C(n, 2) = n * (n - 1) / 2
K = P / 2

# --- EXIBIÇÃO DO RESULTADO ---
# f"{K:.0f}" formata o número para exibir zero casas decimais.
# Em Python, a divisão comum (/) sempre transforma o resultado em um número real (float).
# Essa formatação garante que o número seja impresso como um inteiro limpo (ex: "6" em vez de "6.0").
print(f"{K:.0f}")