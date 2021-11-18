def func(list, n):
    for i in list:
        if int(i) > n:
            print(i)

func(list = (input("Список(Через пробел): ").split()), n = int(input("Число: ")))