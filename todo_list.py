
# Nome do Projeto  : Sistema de Organização de Tarefas (To-Do List)
# Desenvolvido por : Lucas Schmidt
# Data             : Julho/2025
# Descrição        : Script para cadastrar tarefas, exibir todas e filtrar por prioridade.

# Função para cadastrar tarefas
def cadastrar_tarefas():
    quantidade = int(input("Quantas tarefas gostaria de cadastrar? "))
    tarefas = []

    for numero in range(1, quantidade + 1):
        print(f"\nCadastro da tarefa {numero}")
        titulo = input("Título da tarefa: ")
        descricao = input("Descrição da tarefa: ")
        prioridade = input("Prioridade (Baixa, Média ou Alta): ")

        tarefa = {
            "titulo": titulo,
            "descricao": descricao,
            "prioridade": prioridade
        }

        tarefas.append(tarefa)

    return tarefas

# Função para exibir tarefas
def exibir_tarefas(tarefas):
    print("\nTarefas Cadastradas:")
    for tarefa in tarefas:
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")

# Função para filtrar tarefas por prioridade
def filtro_prioridade(tarefas):
    filtro = input("\nDigite a prioridade para filtrar (Baixa, Média ou Alta): ")
    print(f"\nTarefas com prioridade {filtro}:")
    for tarefa in tarefas:
        if tarefa["prioridade"].lower() == filtro.lower():
            print(f"Título: {tarefa['titulo']} | Descrição: {tarefa['descricao']}")

# Programa principal
tarefas = cadastrar_tarefas()
exibir_tarefas(tarefas)
filtro_prioridade(tarefas)
