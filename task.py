class Task:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

task1 = Task("изучить Python")
print(task1.get_title())  # Вывод: Изучить Python

class my_class:
    def __init__(self, nadpis):
        self.na = nadpis

    def get_nadpis(self):
        return self.na

run = my_class("yflgbcm")
print(run.get_nadpis())
