### Отчет по лабораторной работе №1.

---

1. Реализуйте перечисленные выше методы нахождения производной при фиксированном значении шага.

__Теория__
Пусть задана функция $f(x)$ на отрезке $[a, b]$. Выберем на этом отрезке сетки $h$. В таком случае количество узлов сетки будет. 

<tex>$$n={{b - a}\over{h}},$$</tex>

а сами значения $x$ можно задать как $x_i = a + hi, i = 0, ..., n$

* Методы первого порядка:
    1. Правая разностная производная.
    <tex>$$f'(x) \cong {{f(x + h) - f(x)}\over{h}}$$<tex>

    код:
    ```python
    def right_diff(x0, delta, func):
        return (func(x0 + delta) - func(x0)) / delta
    ```

    2. Левая разностная производная.
    $$f'(x) \cong {{f(x) - f(x - h)}\over{h}}$$

    код:
    ```python
    def left_diff(x0, delta, func):
        return (func(x0) - func(x0 - delta)) / delta
    ```

* Метод второго порядка:
    <tex>$$y_i' = {{y_{i+1} - y_{i-1}}\over{2h}}$$<tex>

    <tex>$$y_1' = {{-3y_{0} + 4y_{1} - y_{2}}\over{2h}}$$<tex>

    <tex>$$y_n' = {{y_{n - 2} - 4y_{n - 1} + 3y_{n}}\over{2h}}$$<tex>

    код:
    ```python
    def second_order_diff(x, h, f):
        f_x = f(x)
        f_x_plus_h = f(x + h)
        f_x_minus_h = f(x - h)
        f_x_plus_2h = f(x + 2*h)
        f_x_minus_2h = f(x - 2*h)
        derivative = (f_x_minus_2h - 8*f_x_minus_h + 8*f_x_plus_h - f_x_plus_2h)/(12*h)
        return derivative
    ```

2. Возьмите 2 произвольные функции. Вычислите аналитически производные этих функций. Постройте их графики, а также вычисленные значения численной производной в узлах сетки.
    
    <tex>$$(\cos(x))' = - \sin(x); \ (x\cdot \sin(x))' = x \cdot \cos(x) + \sin(x)$$<tex>

    ![1](https://github.com/georgedem975/applied_mathematics/blob/master/lab-1/assets/Figure_1.png)

3. Найдите среднеквадратичные отклонения численных от истинных значений
производной.


4.  Выполните предыдущий пункт при уменьшении шага (увеличения количества
узлов) в 2, 4, 8 и 16. Как изменяется среднеквадратичное отклонение при измнении шага? Постройте график зависимости среднеквадратичного отклонения
от величины шага.

    код:
    ```python
    r_1 = [np.sqrt(math.fabs(np.mean(right_diff(n, 0.025, func) - func_(n)))),
           np.sqrt(math.fabs(np.mean(right_diff(n, 0.0125, func) - func_(n)))),
           np.sqrt(math.fabs(np.mean(right_diff(n, 0.00625, func) - func_(n)))),
           np.sqrt(math.fabs(np.mean(right_diff(n, 0.003125, func) - func_(n))))]

    print(r_1)

    r_2 = [np.sqrt(math.fabs(np.mean(left_diff(n, 0.025, func) - func_(n)))),
           np.sqrt(math.fabs(np.mean(left_diff(n, 0.0125, func) - func_(n)))),
           np.sqrt(math.fabs(np.mean(left_diff(n, 0.00625, func) - func_(n)))),
           np.sqrt(math.fabs(np.mean(left_diff(n, 0.003125, func) - func_(n))))]

    print(r_2)

    r_3 = [np.sqrt(math.fabs(np.mean(second_order_diff(n, 0.025, func) - func_(n)))),
           np.sqrt(math.fabs(np.mean(second_order_diff(n, 0.0125, func) - func_(n)))),
           np.sqrt(math.fabs(np.mean(second_order_diff(n, 0.00625, func) - func_(n)))),
           np.sqrt(math.fabs(np.mean(second_order_diff(n, 0.003125, func) - func_(n))))]

    print(r_3)
    ```
    вывод:
    ```python
    [0.13071619467055418, 0.09268204779517762, 0.06562421990935367, 0.04643432765849665]
    ```
    ```python
    [0.13211189494095094, 0.0931754933668976, 0.06579867846975462, 0.046496008003634966]
    ```
    ```python
    [0.0001868039453414342, 4.6702767346332e-05, 1.1675924638483095e-05, 2.917065081658973e-06]
    ```

    ![2](https://github.com/georgedem975/applied_mathematics/blob/master/lab-1/assets/Figure_2.png)
    ![3](https://github.com/georgedem975/applied_mathematics/blob/master/lab-1/assets/Figure_3.png)
    ![4](https://github.com/georgedem975/applied_mathematics/blob/master/lab-1/assets/Figure_4.png)
    ![5](https://github.com/georgedem975/applied_mathematics/blob/master/lab-1/assets/Figure_5.png)


    При уменьшении h среднеквадратичное отклонение начинает стремиться к 0. Чем меньше h тем точнее ответ.

---

__Теория__

Для нахождения приближенного значения определенного интеграла могут использоваться так называемые квадратурные формулы. Заметим, что точность метода второго порядка выше чем у других.

<tex>$$I = \int_a^b f(x) dx \cong \sum_0^n{A_if(\overline{x_i})},$$<tex>

где $ \overline{x_i} $ - некоторые точки из отрезка $[a, b]$.

Введем также сетку узлов на отрезке таким же образом.

<tex>$$a = x_0 < x_1 < ... < x_n = b$$<tex>

Тогда интеграл $I$ разобьется в сумму элементарных интегралов. 

<tex>$$I = \sum_1^n {I_i}$$,<tex>

где каждый $I_i$ вычисляется на отрезке $[x_{i - 1}, x_i]$. Геометрически это будет означать, что вся криволинейная трапеция разбивается на n элементарных криволинейных трапеций.

5. Реализуйте методы численного интегрирования.

* Формула прямоугольников
    * формула левых прямоугольников
    <tex>$$I_i \cong h \cdot f_{i - 1}$$<tex>

    код:
    ```python
    def left_rect(a, b, n, func):
        h = (b - a) / n
        sum = 0.0
        for i in range(n - 1):
            sum += h * func(a + i * h)
        return sum
    ```

    * формула правых прямоугольников
    <tex>$$I_i \cong h \cdot f_i$$<tex>

    код:
    ```python
    def right_rect(a, b, n, func):
        h = (b - a) / n
        sum = 0.0
        for i in range(1, n):
            sum += h * func(a + i * h)
        return sum
    ```

    * формула среддних прямоугольников
    <tex>$$I_i \cong h \cdot f_{i-1/2}$$<tex>

    код:
    ```python
    def central_rect(a, b, n, func):
        h = (b - a) / n
        sum = 0.0
        for i in range(1, n):
            sum += h * func(a + (i - 0.5) * h)
        return sum
    ```

* Формула трапеций
<tex>$$I_i \cong {{h} \over {2}}(f_{i-1} + f_i)$$<tex>

код:
```python
def trapeze(a, b, n, func):
    h = (b - a) / n
    sum = func(a) + func(b)
    for i in range(1, n-1):
        sum += 2 * func(a + i * h)
    sum *= h/2
    return sum
```

* Формула Симпсона
<tex>$$I_i = {{h} \over {6}}(f_{i-1} + 4f_{i - 1/2} + f_i)$$<tex>

код:
```python
def sympson(a, b, n, func):
    h = (b - a) / n
    sum = func(a) + func(b)
    k = 0.0
    for i in range(1, n - 1):
        k = 2 + 2 * (i % 2)
        sum += k * func(a + i * h)
    sum *= h/3
    return sum
```

6. Выберите 2 функции и вычислите для них определенный интеграл на отрезке.
Сравните полученное значение с ответом, полученным аналитически.

- возьмем функции вычисления интергала методами правого и левого прямоугольников соответственно.

- придумаем какой нибудь интеграл и вычисли его значение

<tex>$$\int_0^1 x = 0.5$$<tex>

код:
```python
print(left_rect(0, 1, 1000, func_integral))
print(right_rect(0, 1, 1000, func_integral))
```
вывод:
```python
0.49850100000000014
0.49950000000000017
```

- мы видим что значения полученные численно близки к аналитически вычисленному ответу.

7. Проанализируйте зависимость отклонения численного ответа от аналитического в зависимости от шага при уменьшении его в 2, 4, 8 и 16 раз. Постройте график зависимости отклонения от величины шага.

![6](https://github.com/georgedem975/applied_mathematics/blob/master/lab-1/assets/Figure_6.png)
![7](https://github.com/georgedem975/applied_mathematics/blob/master/lab-1/assets/Figure_7.png)

При уменьшении результат выполнения функций начинает стремиться к истинному значению. Так же заметим, что формула средних прямоугольников работает точнее чем правых или средних в общем количестве случаев, так как значение функции стемится оказаться в середине шага.

___Примечания___

* используемы библиотеки:
 ```python
import numpy as np
import matplotlib.pyplot as plt
import statistics
import math
 ```
