import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sici

# Значения C из множества {-1, 0, 1}
C_values = list(range(-4, 5))

# Создаем массив значений x
x = np.linspace(-5, 5, 1000)

# Функция Si(x)
def Si(x):
    si, _ = sici(x)
    return si


# Построим графики для каждого значения C
for C in C_values:
    yr = (C - Si(x[x>0]) - Si(1)) / x[x>0]
    yl = -(C + Si(x[x<0]) + Si(1)) / x[x<0]
    plt.plot(x[x>0], yr, label=f'C = {C}')
    plt.plot(x[x<0], yl, label=f'C = {C}')

# Настройка графика
plt.xlabel('x')
plt.ylabel('y')
plt.title('y(x) = (C - Si(x) - Si(1)) / x, x>0\n'
          'y(x) = -(C + Si(x) + Si(1)) / x, x<0')
plt.legend()

# Устанавливаем местоположение легенды в правый верхний угол
plt.legend(loc='upper right')

# Ограничение осей X и Y
plt.xlim(-5, 5)  # Ограничение по оси X от 0 до 5
plt.ylim(-5, 5)  # Ограничение по оси Y от -2 до 2

# Показать графики
plt.grid(True)
plt.show()
