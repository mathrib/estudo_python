while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:\n")
    print("1. Adicionar Tarefas")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefas")
    print("4. Completar Tarefas")
    print("5. Deletar Tarefas Completadas")
    print("6. Sair do Programa")
    
    escolha = int(input("Digite o número da opção desejada:"))
    if escolha == 6:
        print("Saindo do programa...")
        break