class Task:
    def __init__(self, name):
        # Keep track of task name and status (done or not done)
        # Task should start out not done
        pass

    def __repr__(self):
        # Display the name and status of task
        return f"{self.name}"


class TodoList:
    def __init__(self):
        # Keep track of a tasks list, which starts out empty
        self.tasks = []

    def add(self, name):
        # Add a new task with a given name
        pass

    def finish(self, name):
        # Update the status of the task that matches name to be done
        pass

    def remove(self, name):
        # Remove the task that matches name
        # Hint: make a new tasks list
        pass

    def __repr__(self):
        # Return a representation of the to do list that
        # shows each task (name and status), the total number
        # of tasks, and the number of undone tasks.

        return str(self.tasks)


print("Test Task:\n")

hw = Task("do homework")

print(hw.name)  # "do homework"
print(hw.isDone)  # False

hw.isDone = True
print(hw)  # [x] do homework

print("\nTest TodoList:\n")

todo = TodoList()

todo.add("do homework")
todo.add("feed dog")
todo.add("water plants")
todo.finish("feed dog")
todo.remove("do homework")

print(todo)

# Should print:
#
# [x] feed dog
# [ ] water plants
# --------------------
# 2 tasks, 1 undone
