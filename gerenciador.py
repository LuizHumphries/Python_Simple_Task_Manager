def add_task(tarefas: list[dict[str,bool]], task_name: str) -> None:
    task = {"task": task_name, "completed": False}
    tarefas.append(task)
    

def see_tasks(tasks: list[dict[str,bool]]) -> None:
    print("\nTask List:")
    for count, task in enumerate(tasks, start = 1):
        task_name = task['task']
        status = "✅" if task["completed"] else " "
        print(f"{count}. [{status}] {task_name}")
    return

def update_task_name(tasks: list[dict[str,bool]], task_index: str, new_task_name: str) -> None:
    task_index_adjusted = int(task_index) - 1
    tasks[task_index_adjusted]["task"] = new_task_name #type: ignore
    print(f"\nTask {task_index} updated! New name = {new_task_name}")
    return


tasks = []
while True:
    print("\n Task Manager Menu:")
    print("1. Add task")
    print("2. See taks")
    print("3. Update Task")
    print("4. Complete Tasks")
    print("5. Delete all completed tasks")
    print("6. Quit")


    user_choice = input("Choose an option: ")

    if user_choice == "1":
        task_name = input("Digite o nome da tarefa que gostaria de adicionar: ")
        add_task(tasks, task_name)

    elif user_choice == "2":
        see_tasks(tasks)

    elif user_choice == "3":
        see_tasks(tasks)
        task_index = input("What is the task number would you want to change? ")
        if int(task_index) - 1 >= 0 and int(task_index) - 1 < len(tasks):
            new_task_name = input("Write the new name for this task: ")
            update_task_name(tasks, task_index, new_task_name)
        else:
            print("Error: invalid task index")

    elif user_choice == "6":
        break