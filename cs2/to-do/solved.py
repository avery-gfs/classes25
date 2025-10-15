class Task:
    def __init__(self, name):
        # Keep track of task name and status (done or not done)
        # Task should start out not done
        self.name = name
        self.isDone = False

    def __repr__(self):
        # Display the name and status of task
        isDoneStr = "x" if self.isDone else " "
        return f"[{isDoneStr}] {self.name}"


class TodoList:
    def __init__(self):
        # Keep track of a tasks list, which starts out empty
        self.tasks = []

    def addTask(self, name):
        # Add a new task with a given name
        self.tasks.append(Task(name))

    def markDone(self, name):
        # Update the status of the task that matches name to be done
        for task in self.tasks:
            if task.name == name:
                task.isDone = True

    def remove(self, name):
        # Remove the task that matches name
        newTasks = []

        for task in self.tasks:
            if task.name != name:
                newTasks.append(task)

        self.tasks = newTasks

    def __repr__(self):
        # Return a representation of the to do list that
        # shows each task (name and status), the total number
        # of tasks, and the number of undone tasks.

        numTasks = len(self.tasks)
        numUnDone = 0
        result = ""

        for task in self.tasks:
            result += f"{task}\n"

            if task.isDone:
                numUnDone += 1

            # Could also do numUnDone += not task.isDone

        result += "-" * 20
        result += f"\n{numTasks} tasks, {numUnDone} undone"
        return result


print("Test Task:\n")

hw = Task("do homework")

print(hw.name)  # "do homework"
print(hw.isDone)  # False

hw.isDone = True
print(hw)  # [x] do homework

print("\nTest TodoList:\n")

todo = TodoList()

todo.addTask("do homework")
todo.addTask("feed dog")
todo.addTask("water plants")
todo.markDone("feed dog")
todo.remove("do homework")

print(todo)

# Should print:
#
# [x] feed dog
# [ ] water plants
# --------------------
# 2 tasks, 1 undone
