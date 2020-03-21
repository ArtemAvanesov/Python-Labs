import numpy as np
from scipy.optimize import linprog	

c = [7,3,6,4,8,2,1,5,9]
A_ub = [[1,1,1,0,0,0,0,0,0],
        [0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,1,1,1]] 
b_ub = [74,40,36] 
A_eq = [[1,0,0,1,0,0,1,0,0],
        [0,1,0,0,1,0,0,1,0],
        [0,0,1,0,0,1,0,0,1]] 
b_eq = [20,45,30] 
solution = linprog(c, A_ub, b_ub, A_eq, b_eq)



# Вывод решения
print("Оптимальное решение, х = ", np.around(solution.get('x'),  decimals=0))

# Min стоимость доставки
print("Min стоимость доставки: ", np.around(solution.get('fun'),  decimals=0))

# Вывод остатков ресурсов
print("&&&&&&Что-то: ", np.around(solution.get('slack'),  decimals=0))

# Вывод числа итераций
print("Число иттераций: ", solution.get('nit'))

# Вывод статуса решения
if (solution.get('status') == 0):
    print("Поиск оптимального решения завершился успешно!")
elif (solution.get('status') == 1):
    print("Достигнут лимит на число итераций!")
elif (solution.get('status') == 2):
    print("Задача не имеет решений!")
else:
    print("Целевая функция не ограничена!")