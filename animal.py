class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Я просто животное, и я не говорю."

class Dog(Animal):  # Класс Dog наследует класс Animal
    def speak(self):  # Переопределяем метод speak
        return f"{self.name} говорит: Гав-гав!"

class Cat(Animal):  # Класс Cat наследует класс Animal
    def speak(self):  # Переопределяем метод speak
        return f"{self.name} говорит: Мяу!"

dog = Dog("Бобик")
cat = Cat("Мурка")

print(dog.speak())  # Вывод: Бобик говорит: Гав-гав!
print(cat.speak())  # Вывод: Мурка говорит: Мяу!