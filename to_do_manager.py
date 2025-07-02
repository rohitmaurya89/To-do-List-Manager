import json 
import pandas as pd


class Task:
    def __init__(self,description,due_date,completed_status = False):
        self.description = description
        self.due_date = due_date 
        self.completed_status = completed_status

class ToDoManager : 
    def __init__(self):
        self.tasks = []

    def addTask(self,task):
        self.tasks.append(task)
        self.save_to_file()
        
    
    def viewTask(self):
        if len(self.tasks) == 0 :
            print(f"No Task is found .")
        else:
            print("Tasks List : \n")
            # for index, tsk in enumerate(self.tasks,start=1):
            #     print(f"{index}.  Task : {tsk.description},  Due Date : {tsk.due_date},   is completed : {tsk.completed_status}.")

            df = pd.read_json("Task.json")
            print(df)

    # Function to mark a task completed or incompleted :
    def mark_completed(self,index):
         self.tasks[index].completed_status = True
         self.save_to_file()
    
    # Function to edit a task 
    def edit_task(self,index):
        updated_task = input("enter the updated task name : ")
        self.tasks[index].description = updated_task
        self.save_to_file()

    #Function to remove a task :
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_to_file()
        else : 
            return print("Invalid index or out of range index.")


    # File Handling :
    def save_to_file(self , filename="Task.json"):
        with open (filename,"w") as f :
            json.dump([task.__dict__ for task in self.tasks], f, indent=4)


    def load_from_file(self, filename="Task.json"):
        try :
            with open(filename, "r") as f :
                data = json.load(f)
                self.tasks = [Task(**item) for item in data]
        except FileNotFoundError:
            self.tasks = []




def main():

    todomanager = ToDoManager()
    todomanager.load_from_file()

    while(True):
        print("Task Menu : \n")
        print("1. Add a new task")
        print("2. View all tasks or filtered tasks ")
        print("3. Mark task as completed")
        print("4. Edit Task")
        print("5. Delete a task")
        print("6. Exit")

        choice = int(input("Enter you choice (1-6) : "))

        try : 
            if choice == 1:
                descript = input("Enter name of Task : ")
                duedate = input("Enter the expected date to complete (format - dd/mm/yyyy) : ")
                print()
                task = Task(descript,duedate)
                todomanager.addTask(task)
                print(f"added successfully ! ")

            elif choice == 2:
                todomanager.viewTask()

            elif choice == 3:
                markIndex = int(input("Enter the index to mark the task completed : "))
                todomanager.mark_completed(markIndex-1)  # as indexing start from 0 in the list in python.Then , to manage indexing , here subtracted 1 from user input

            elif choice == 4:
                editIndex = int(input("Enter the index of task you want to edit : "))
                todomanager.edit_task(editIndex-1)

            elif choice == 5:
                removeIndex = int(input("Enter the index to remove a task : "))
                todomanager.remove_task(removeIndex-1)
                print("removed succussfully !")

            elif choice == 6:
                break
        
            
        except (ValueError,IndexError):
            print("Invalid choice . Try again !")

#for code reusability : 
if __name__ == "__main__":
    main()
  