import yaml
from taskmanage.task import Task

def func(bookpath):
    print(f"Use(bookpath)")





with open("Knigi.yaml") as f:
    config = yaml.safe_load(f)

for book in config["download"]:
    path="books/" + book["filename"]
    func(path)

    task = Task(path)
    task.set_action()
     