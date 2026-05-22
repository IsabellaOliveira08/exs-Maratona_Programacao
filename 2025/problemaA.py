# Lê a quantidade total de eventos disponíveis
N = int(input())  

# Cria uma lista vazia para armazenar todos os eventos lidos
eventos = []

# Laço para ler os horários de início e fim de cada um dos N eventos
for _ in range(N):
    S = int(input())  # S (Start): Horário de início do evento
    F = int(input())  # F (Finish): Horário de término do evento
    
    # Adiciona o evento como uma tupla (início, fim) na lista de eventos
    eventos.append((S, F))

# --- O PULO DO GATO (Algoritmo Guloso) ---
# Ordena a lista de eventos com base no horário de TÉRMINO (e[1]) de cada um.
# lambda e: e[1] diz para o Python olhar para o segundo elemento da tupla (o fim) na hora de ordenar.
# Ordenar pelo fim garante que sempre analisaremos primeiro os eventos que acabam mais cedo.
eventos.sort(key=lambda e: e[1])

# Lista que vai guardar os eventos que conseguiremos agendar (sem choques de horário)
selecionados = []

# Guarda o horário em que o último evento escolhido terminou.
# Começa em -1 para garantir que qualquer evento que comece a partir do tempo 0 possa ser escolhido.
ultimo_fim = -1

# Passa por cada evento (já ordenados pelo horário de término)
for s, f in eventos:
    # REGRA DE OURO: Um evento só pode ser selecionado se o seu horário de início (s)
    # for maior ou igual ao horário de término do último evento que agendamos (ultimo_fim).
    if s >= ultimo_fim:
        # Se não houver conflito de horário, coloca o evento na agenda
        selecionados.append((s, f))
        
        # Atualiza o marcador do último fim para o término deste novo evento selecionado
        ultimo_fim = f

# --- IMPRESSÃO DOS RESULTADOS ---
# Exibe na tela os horários de início e fim dos eventos que foram selecionados
for s, f in selecionados:
    print(s, f)
