# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
# 1 2 3 4 5
# 6
# -> 5

N = int(input("Введите количество элементов массива: "))
X = int(input("Введите число 'X': "))
my_array = [ i for i in range(1, N + 1)]
# print(my_array)
for i in my_array:
    print(i, end = " ")
    if i == X:
        near = X + 1
print(f"\n{near} -> {X}")