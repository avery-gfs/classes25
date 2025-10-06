import os

tasks = []

while True:
    print(tasks)
    print(f"Tasks remaining: {len(tasks)}")

    name = input("Enter task: ")

    os.system("clear")

    if name in tasks:
        tasks.remove(name)
    else:
        tasks.append(name)
