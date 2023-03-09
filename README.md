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
    ![1]()

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
    ![2]()

5. Реализуйте методы численного интегрирования.

6. Выберите 2 функции и вычислите для них определенный интеграл на отрезке.
Сравните полученное значение с ответом, полученным аналитически.

7. роанализируйте зависимость отклонения численного ответа от аналитического в зависимости от шага при уменьшении его в 2, 4, 8 и 16 раз. Постройтеграфик зависимости отклонения от величины шага.

___Примечания___

* используемы библиотеки:
 ```python
import numpy as np
import matplotlib.pyplot as plt
import statistics
 ```