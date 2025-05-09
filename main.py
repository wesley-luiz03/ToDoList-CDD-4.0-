tasks = []

def linha():
    print("-" * 40)
    
def addTasks():
    newTasks = input("\nAdicione uma tasks: ")
    tasks.append(newTasks)
    print("Tasks adicionada com sucesso!")
    
def viewTasks():
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Tarefas:")
        for x, task in enumerate(tasks, start=1):
            print(f"{x} - {task}")
            
def removeTasks():
    if not tasks:
        print("Nenhuma task foi adiconada para ser removida.")
    else:
        print("Tarefas:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i} - {task}")
        try:
            removeTask = int(input("Escolha uma task para ser removida: ")) - 1
            if 1 <= removeTask < len(tasks):
                removed = tasks.pop(removeTask)
                print(f"Task {removed} removida com sucesso!")
            else:
                print("Número inválido! Nenhuma task removida.")
        except ValueError:
            print("Entrada inválida! Por favor digite um número.")

def editTasks():
    if not tasks:
        print("Nenhum task foi adiconada para ser editada.")
    else:
        print("Tasks:")
        for j, task in enumerate(tasks, start=1):
            print(f"{j} - {task}")
        try:
            editedTask = int(input("Escola uma task para ser editada: "))
            if 0 <= editedTask <= len(tasks):
                editedNewTask = input("Digite a nova task: ")
                tasks[editedTask - 1] = editedNewTask
                print("Task editada com sucesso!")
            else:
                print("Número inválido! Nenhuma task editada.")
        except ValueError:
            print("Entrada inválida! Por favor digite um número.")
                
while True:
    linha()
    print("To Do List | CDD 4.0 | By: Wesley Luiz")
    linha()
    
    print("--> MENU <---\n")
    print("1 - Adicionar Task")
    print("2 - Ver Tasks")
    print("3 - Remover Task")
    print("4 - Editar task")
    print("5 - Sair\n")
    
    try:
        opcao = int(input("Digite uma opção: "))
    except ValueError:
        print("Entrada inválida! Por favor digite um número.")
        continue
    
    if opcao == 1:
        addTasks()
    elif opcao == 2:
        viewTasks()
    elif opcao == 3:
        removeTasks()
    elif opcao == 4:
        editTasks()
    elif opcao == 5:
        print("Até logo...")
        break
    else:
        print("Opção inválida! Tente novamente.")