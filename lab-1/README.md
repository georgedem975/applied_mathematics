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
    def diff(x0, delta, func):
        return (func(x0 + delta / 2) - func(x0 - delta / 2)) / delta
    ```

2. Возьмите 2 произвольные функции. Вычислите аналитически производные этих функций. Постройте их графики, а также вычисленные значения численной производной в узлах сетки.
    ![1](https://github.com/georgedem975/applied_mathematics/blob/master/lab-1/assets/Figure_1.png)

3. Найдите среднеквадратичные отклонения численных от истинных значений
производной.

    код:
    ```python
    print(statistics.stdev(diff(n, 0.5, func)))
    ```

    вывод:
    ```python
    0.41041159979851366
    ```

4.  Выполните предыдущий пункт при уменьшении шага (увеличения количества
узлов) в 2, 4, 8 и 16. Как изменяется среднеквадратичное отклонение при измнении шага? Постройте график зависимости среднеквадратичного отклонения
от величины шага.
* в 2 раза:
    код:
    ```python
    print(statistics.stdev(diff(n, 0.025, func)))
    ```
    вывод:
    ```python
    0.4198537455151593
    ```
* в 4 раза:
    код:
    ```python
    print(statistics.stdev(diff(n, 0.0125, func)))
    ```
    вывод:
    ```python
    0.4198715800398994
    ```
* в 8 раз:
    код:
    ```python
    print(statistics.stdev(diff(n, 0.00625, func)))
    ```
    вывод:
    ```python
    0.4198760387216906
    ```
* в 16 раз:
    код:
    ```python
    print(statistics.stdev(diff(n, 0.003125, func)))
    ```
    вывод:
    ```python
    0.4198771533952976
    ```
    ![2](https://github.com/georgedem975/applied_mathematics/blob/master/lab-1/assets/Figure_2.png)

---

__Теория__

Для нахождения приближенного значения определенного интеграла могут использоваться так называемые квадратурные формулы.

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

![3](https://github.com/georgedem975/applied_mathematics/blob/master/lab-1/assets/Figure_3.png)

___Примечания___

* используемы библиотеки:
 ```python
import numpy as np
import matplotlib.pyplot as plt
import statistics
 ```
