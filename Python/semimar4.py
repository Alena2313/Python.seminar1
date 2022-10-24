#Урок 3. Данные, функции и модули в Python
#Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
#6 –> 1 1 2 3 5 8

def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
       a, b = b, a + b

data = list(fibonacci(10))
print(data)

#Задача 2. В файле находятся названия фруктов. 
#Выведите все фрукты, названия которых начинаются на заданную букву.

fruits_list = ['абрикос', 'банан', 'авокадо', 'апельсин']
check = 'а'
print("The original list : " + str(fruits_list))
res = [idx for idx in fruits_list if idx[0].lower() == check.lower()]
print("The list of matching first letter : " + str(res))

# 2 Вариант решения через  startswith() + lower()
fruits_list = ['абрикос', 'банан', 'авокадо', 'апельсин']
check = 'а'
print("The original list : " + str(fruits_list))
res = [idx for idx in fruits_list if idx.lower().startswith(check.lower())]
print("The list of matching first letter : " + str(res))

#Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
#Если фраза ему неизвестна, он выводит соответствующую фразу.
#«как тебя зовут?» –> меня зовут Анатолий

user_name=''

while len(user_name.strip())<1:
    print("Привет! Давай знакомиться! Как тебя зовут?")
    user_name = input()                 
print("Приятно познакомиться, " +  user_name + "!")                                   
    