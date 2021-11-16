def fact(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
        yield num


end_num = int(input('Введите последнее число для факториала:'))
fact_num = 1
for el in fact(end_num):
    print(f'{fact_num}! = {el}')
    fact_num +=1