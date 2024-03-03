
task=[]
done=[]
while True:
    print("1 to Add a task in the list")
    print("2 to mark a task as done in the list")
    print("3 to view all the tasks in the list")
    print("4 to exit")
    x=int(input("Enter your choice:\n"))
    if x==1:
        t=input("Enter the task you want to add:\n")
        task.append(t)
        print("The resulting list is:\n",task)
    elif x==2:
        t=input("Enter the tasks that are marked to be done\n")
        task.remove(t)
        done.append(t)
        print("tasks\t\t\t\t\t\t\t\t\t\t\ttasks done\n",task,"\t\t\t\t\t\t",done)
    elif x==3:
        print("The to-do list for today is:\n",task)
    elif x==4:
        break
    else:
        print("INVALID CHOICE!!!!\nENTER A VALID CHOICE")
        
