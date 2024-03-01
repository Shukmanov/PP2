#first one

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for number in list_of_numbers:
    count +=number

print(count/len(list_of_numbers))


#second one

just_word = "ksoehfshdej"
glas = 0;
for letter in just_word:
    if(letter == "o" or letter == "e" or letter == "i" or letter == "u" or letter == "a"):
        glas += 1

"""""
this more easy way to do it

sogl = "aeiou"
for letter in just_word:
    if(letter in sogl):
        glas +=1
        
"""""

print(glas)


#third one

double_mussive = ([1, 48, 9429, 2983, 9389,],
                  [9238, 858, 82, 12, 2849])

double_massive_sum = 0

for number1 in double_mussive:
    for number2 in double_mussive:
        double_massive_sum += number2
    double_massive_sum += number1

print(double_mussive_sum)

"""""
not finished yet

Сумма элементов матрицы:
Создайте двумерный массив (матрицу) чисел. Напишите программу, которая вычислит сумму всех элементов в этой матрице.

Объединение словарей:
Создайте два словаря с произвольными данными. Напишите программу, которая объединит эти словари в один.

Проверка на палиндром:
Напишите программу, которая проверит, является ли заданная строка палиндромом (читается одинаково слева направо и справа налево).

Поиск уникальных элементов:
Создайте список с повторяющимися элементами. Напишите программу, которая удалит все повторяющиеся элементы и выведет список только с уникальными элементами.

Поиск максимального элемента в списке списков:
Создайте список списков с числами. Напишите программу, которая найдет максимальный элемент в этом списке списков.

"""""