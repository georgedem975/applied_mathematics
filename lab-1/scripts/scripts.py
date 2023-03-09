#прикладная математика
import numpy as np
import matplotlib.pyplot as plt
import statistics


#дифференционарование

#численное вычисление дифференциала
def diff(x0, delta, func):
    return (func(x0 + delta / 2) - func(x0 - delta / 2)) / delta


#правая разностная производная
def right_diff(x0, delta, func):
    return (func(x0 + delta) - func(x0)) / delta

#левая разностная производная
def left_diff(x0, delta, func):
    return (func(x0) - func(x0 - delta)) / delta


#функция(1)
def func(x):
    return x*np.sin(x)


#функция(2)
def func_second(x):
    return np.cos(x)


#дифференциал функции (1)
def diff_func(x):
    return x*np.cos(x) + np.sin(x)


#интегрирование

#метод левых прямоугольников
def left_rect(a, b, n, func):
    h = (b - a) / n
    sum = 0.0
    for i in range(n - 1):
        sum += h * func(a + i * h)
    return sum


#метод правых прямоугольников
def right_rect(a, b, n, func):
    h = (b - a) / n
    sum = 0.0
    for i in range(1, n):
        sum += h * func(a + i * h)
    return sum


#метод средних прямоугольников
def central_rect(a, b, n, func):
    h = (b - a) / n
    sum = 0.0
    for i in range(1, n):
        sum += h * func(a + (i - 0.5) * h)
    return sum


#метод трапеций
def trapeze(a, b, n, func):
    h = (b - a) / n
    sum = func(a) + func(b)
    for i in range(1, n-1):
        sum += 2 * func(a + i * h)
    sum *= h/2
    return sum


#метод симпсона
def sympson(a, b, n, func):
    h = (b - a) / n
    sum = func(a) + func(b)
    k = 0.0
    for i in range(1, n - 1):
        k = 2 + 2 * (i % 2)
        sum += k * func(a + i * h)
    sum *= h/3
    return sum


def func_integral(x):
    return x


if __name__ == '__main__':
    n = np.linspace(0, 1, 100000)

    x = 10

    print(func(x))

    print()

    print(diff_func(x))
    print(diff(x, 0.005, func))
    print(left_diff(x, 0.005, func))
    print(right_diff(x, 0.005, func))

    print()

    print(left_rect(1, 2, 10000, func))
    print(right_rect(1, 2, 10000, func))
    print(central_rect(1, 2, 10000, func))
    print(trapeze(1, 2, 10000, func))
    print(sympson(1, 2, 10000, func))

    print()

    plt.grid()
    plt.plot(n, diff(n, 0.5, func_second), 'r--', n, diff(n, 0.5, func), 'b-')
    plt.legend(['(cos(x))', '(sin(x)*x)'])
    plt.show()

    print(statistics.stdev(diff(n, 0.003125, func)))

    r_1 = [statistics.stdev(right_diff(n, 0.025, func)),
         statistics.stdev(right_diff(n, 0.0125, func)),
         statistics.stdev(right_diff(n, 0.00625, func)),
         statistics.stdev(right_diff(n, 0.003125, func))]

    r_2 = [statistics.stdev(left_diff(n, 0.025, func)),
         statistics.stdev(left_diff(n, 0.0125, func)),
         statistics.stdev(left_diff(n, 0.00625, func)),
         statistics.stdev(left_diff(n, 0.003125, func))]

    r_3 = [statistics.stdev(diff(n, 0.025, func)),
     statistics.stdev(diff(n, 0.0125, func)),
     statistics.stdev(diff(n, 0.00625, func)),
     statistics.stdev(diff(n, 0.003125, func))]

    plt.grid()
    plt.plot(r_1, r_1, 'ro', r_2, r_2, 'bo', r_3, r_3, 'go')
    plt.legend(['right', 'left', 'center'])
    plt.show()

    print()

    print(left_rect(0, 1, 1000, func_integral))
    print(right_rect(0, 1, 1000, func_integral))

    v = [2000, 4000, 8000, 16000]

    answers = np.zeros((5, 4), dtype=float)

    print(answers)

    for i in range(4):
        answers[0][i] += right_rect(0, 1, v[i], func_integral)

    for i in range(4):
        answers[1][i] += left_rect(0, 1, v[i], func_integral)

    for i in range(4):
        answers[2][i] += central_rect(0, 1, v[i], func_integral)

    for i in range(4):
        answers[3][i] += trapeze(0, 1, v[i], func_integral)

    for i in range(4):
        answers[4][i] += sympson(0, 1, v[i], func_integral)

    plt.grid()
    plt.plot(v, answers[0], 'ro',
             v, answers[1], 'bo',
             v, answers[2], 'go',
             v, answers[3], 'y*',
             v, answers[4], 'g^')
    
    plt.legend(['right', 'left', 'center', 'trapeze', 'sympson'])
    plt.show()