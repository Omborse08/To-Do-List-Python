print("====To-Do-List====")

task_list = []
while True:

    print("\n1.Add Task")
    print("2.View Task")
    print("3.Complete Task")
    print("4.Delete Task")
    print("5.Exit")

    option_choose = int(input("Choose Option: "))
    match option_choose:

        case 1:
            add_task = input("> Add Task: ")
            task_list.append([add_task,False])
            print("Task Added.")

        case 2:
            print("> View Tasks")
            for i in range(len(task_list)):
                mark = "[✓]" if task_list[i][1] else "[ ]"
                print(i+1,mark,task_list[i][0])

        case 3:
            for i in range(len(task_list)):
                mark = "[✓]" if task_list [i][1] else "[ ]"
                print(i+1,mark,task_list[i][0])
            option_task = int(input("Choose Completed Task: "))
            
            if 0 < option_task <= len(task_list):
                task_list[option_task - 1][1] = True
                print("Task Completed Successfully.")
            
            else:
                print("Invalid Option")

        case 4:
            print("Delete Task From List")
            number_remove = 0
            for k in range(len(task_list)):
                number_remove += 1
                print(number_remove,task_list[k][0])
            delete_task = int(input("Remove Task: "))
            sum_delete = delete_task - 1
            task_list.pop(sum_delete)
            print("Task Removed Succesfully.")

        case 5:
            print("Thanks For Using My Serives.")
            break        






        