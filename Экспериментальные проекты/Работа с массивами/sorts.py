array1 = [9, 7, 4, 6, 3, 8, 1, 2, 5]
array2 = [9, 7, 4, 6, 3, 8, 1, 2, 5]
array3 = [9, 7, 4, 6, 3, 8, 1, 2, 5]
array4 = [9, 7, 4, 6, 3, 8, 1, 2, 5]
print("Исходный массив: ", array1)

# ---Сортировка методом пузырька---
flag = True
while flag:
     flag = False
     for i in range(len(array1)-1):
          if array1[i] > array1[i+1]:
               array1[i],array1[i+1] = array1[i+1],array1[i]
               flag = True
print("Сортировка пузырьком: ", array1)

# ---Сортировка выборкой---
for i in range(len(array2)):
     lowest_value_index = i
     for j in range(i + 1, len(array2)):
          if array2[j] < array2[lowest_value_index]:
               lowest_value_index = j
     array2[i], array2[lowest_value_index] = array2[lowest_value_index], array2[i]
print("Сортировка выборкой: ", array2)

# ---Быстрая сортировка---
def partition(nums, low, high):  
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):  
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)

quick_sort(array3)  
print("Быстрая сортировка: ", array3) 

# ---Стандартная сортировка---
array4 = sorted(array4)
print("Стандартная сортировка: ", array4)


