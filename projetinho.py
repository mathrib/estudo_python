def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso.")
    return

def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    


tarefas = []

while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:\n")
    print("1. Adicionar Tarefas")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefas")
    print("4. Completar Tarefas")
    print("5. Deletar Tarefas Completadas")
    print("6. Sair do Programa")
    
    escolha = int(input("Digite o número da opção desejada:"))
    if escolha == 1:
        nome_tarefa = input("Digite o nome da tarefa que você deseja adiconar: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == 2:
        ver_tarefas(tarefas)
    elif escolha == 6:
        print("Saindo do programa...")
        break