#1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
#N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input())
 
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
 
print(factorial)

 # Через рекурсию
def fac(n):
    if n == 0:
        return 1
   return fac(n-1) * n

print(fac(3))

#2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z
print('x y z')
for x in range(2):
 for y in range(2):
   for z in range(2):
    if (not(x) and y and z) or (not(x) and not(y) and z) or (not(x) and not (y) and not(z))==1:
        print(x, y, z)


#3.Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
#«one» «onetwonine» - o – 2, n – 3, e – 2


import re 
test_str = "onetwonine"
count = len(re.findall("one", test_str))  
print ("Count of t in onetwonine is : "
                            +  str(count)) 


from collections import Counter
s = 'onetwonine'
d = dict()
for k, v in Counter(s).items():
   d.setdefault(v, []).append(k)
print(d)


#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.3 -> [2, 3, -3, -2, -1, 0, 1]

lst = [-3, -2, -1, 0, 1, 2, 3]
length = len(lst)
x = lst[length-1]
for i in range(length-1, -1,-1):
    lst[i] = lst[i-1]
lst[0] = x
print(lst)