tasks=[]

def add(task):
    tasks.append(task)
    
def remove(task_num):
    if 0<task_num<=len(task):
        remove=tasks.pop(task_num-1)
        print("REMOVED TASK : "+remove)
    else:
        print("Invalid Number")

def view():
    if not tasks:
        print("No Task Listed")
    else:
        for i in range(len(tasks)):
            print(str(i+1)+"."+tasks[i])

while True:
    print("\n1.Create Task\n2.View Task\n3.Remove Taskn\n4.Exit ")

    ch=int(input("Enter your Choice : "))

    if ch==1:
        task=input("Enter task : ")
        add(task)

    elif ch==2:
        view()
    
    elif ch==3:
        task_num = int(input("Enter the task number to remove: "))
        remove(task_num)

    elif ch==4:
        break

    else:
        print("invalid choice !!!")
