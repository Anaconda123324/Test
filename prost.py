def a(numb, numb2):
    a=list(range(numb, numb2 + 1))
    for i in a:
        if i %7 == 0:
            return i


user_input=int(input('Введите начало диапазона: '))
user_input_2=int(input('Введите конец диапазона: '))

print(a(user_input, user_input_2))