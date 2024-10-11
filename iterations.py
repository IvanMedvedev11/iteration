def search(data, elem):
    for i in range(len(data)):
        if data[i] == elem:
            return i
    else:
        return -1

def binary_search(data, elem):
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = (low + high) // 2
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1
    return -1
import random
import time
min_, max_, long = map(int, input("Введите минимальный элемент, максимальный элемент, длину списка: ").split())
number = int(input("Введите число: "))
my_list = [random.randint(min_, max_) for i in range(long)]
my_list.sort()
print("Готово")
tic1 = time.time()
print(binary_search(my_list, number))
toc1 = time.time()
time1 = toc1 - tic1
print(f"Бинарный поиск: {time1} секунд")
tic2 = time.time()
print(search(my_list, number))
toc2 = time.time()
time2 = toc2 - tic2
print(f"Обычный поиск: {time2} секунд")
tic3 = time.time()
try:
    print(my_list.index(number))
except ValueError:
    print(-1)
toc3 = time.time()
time3 = toc3 - tic3
print(f"Встроенный поиск: {time3} секунд")
