def task():
    tasks = []
    print("----Welcome to the Task Management App----")
    
    total_task = int(input("Enter how mant task you want to add = "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
        
    print(f"Today's Task are \n{tasks}")
    
    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/ : "))
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added ...")
            
        elif operation == 2:
            update_val = input("Enter the task name you want to update : ")
            if update_val in tasks:
                up = input("Enter new Task : ")
                ind = tasks.index(update_val)
                tasks[ind] = up 
                print(f"Updated task {up}")
                
        elif operation == 3:
            del_val = input("Enter the task name you want to delete : ")
            if del_val in tasks:
                index = tasks.index(del_val)
                del tasks[index]
                print(f"Task {del_val} has been deleted ")
                
        elif operation == 4:
            print(f"Total_tasks = {tasks}")
            
        elif operation == 5:
            print("Closing the program .....")
            break
        
        else: 
            print("Inavlid input")
                
if __name__ == "__main__":
    task()



