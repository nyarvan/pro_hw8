from simpleclass import Text
import time

def count_func(f):
    count = 0
    def wrapped(*args):
        nonlocal count
        count += 1
        return f"Функция {f} с результатом {f(*args)} вызвана {count} раз."
    return wrapped

func = []
def list_function(f):
    def wrapped(*args):
        func.append(f(*args))
        return func
    return wrapped

def time_function(n: int, path: str):
    def func(f):
        start = time.time()
        summa = 0
        def wrapped(*args):
            nonlocal summa
            for i in range(n):
                summa += f(*args)
            file = open(path, "w")
            end = time.time()
            result_time = end - start
            file.write(f"Функция {f} с результатом {f(*args)} выполнена {n} раз и хронометраж выполнения {result_time}")
            file.close()
            return f(*args)
        return wrapped
    return func

@list_function
@count_func
def summa(a, b):
    return a + b

@list_function
def mul(a, b):
    return a * b

@time_function(50, "time.txt")
def area_rectangle(a, b):
    return a * b

if __name__ == "__main__":
    print("Exercise 1:")
    print(summa(1, 2))
    print(summa(5, 2))
    print(summa(6, 5))

    print("\nExercise 2:")
    print(mul(2, 3))

    print("\nExercise 3:")
    text = Text(4, 2)
    print(text)
    text1 = Text(6, 2)
    print(text)
    file = open("text.txt")
    res = "".join(file)
    file.close()
    print(res)

    print("\nExercise 4:")
    x = area_rectangle(10, 50)
    file = open("time.txt")
    value_file = "".join(file)
    file.close()
    print(value_file)

