
import flask
import requests
import jsons
'''"GBP": {
            "ID": "R01035",
            "NumCode": "826",
            "CharCode": "GBP",
            "Nominal": 1,
            "Name": "Фунт стерлингов Соединенного королевства",
            "Value": 82.9866,
            "Previous": 82.2263'''


url='https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
data = jsons.loads(response.text)
print ('готов задача #0')

#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print()
print('Задача 1')
print()
print('цикл for')
n=5
for i in range (n):
    print('строка № ', i+1,'   0')
    i+=1

print()
print('цикл while')
m=1
while m<=5:
      print('строка № ', m , '   0')
      m += 1
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print()
print('Задача 2 Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.')
count_input = 0
count5 = 0
number_find = 5
while count_input<10:
    print('Номер вводимой цифры №', count_input+1)
    integre_find_5= input('Введите Цифру на проверку =')
    integre_find_5=int(integre_find_5)
    if integre_find_5 % 10 == number_find:
      count5+=1
      integre_find_5 = integre_find_5//10
    count_input+=1
print('количество цифр 5 из 10 = ', count5)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
print()
print('Задача 3 Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.')
sum = 0
for i in range(1,101):
    sum+=i
print(' Класическая задачка  сумма =', sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
print()
print('Задача 4 Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.')
multi = 1
test_number = 10
for i in range(1, test_number+1):
    multi=multi*i
print(' Класическая задачка произведение чисел 1 до 10 = 3628800 сверка', multi)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
print()
print('Задача 5 Вывести цифры числа на каждой строчке.')
integer_number = 565423

# print(integer_number%10,integer_number//10)

while integer_number>0:
 print(integer_number%10)
 integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
print()
print('Задача 6 Найти сумму цифр числа.')
integre_find = 3101010
#count_number = 0
summ_number = 0
while integre_find>0:
    #count_number+=1
    summ_number=summ_number+integre_find%10
    integre_find = integre_find//10
    #print('числа = ', count_number, summ_number,integre_find)
print('сумма цифр числа = ', summ_number)

'''
Задача 7
Найти произведение цифр числа.
'''
print()
print('Задача 7 Найти произведение цифр числа.')
integre_finds = 123
multi_numbers = 1
while integre_finds > 0:
    multi_numbers= multi_numbers*(integre_finds%10)
   # print('числа', integre_finds//10, integre_finds%10, integre_finds, multi_numbers)
    integre_finds = integre_finds//10

print('Произведение цифр числа',  multi_numbers)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
print()
print('Задача 8 Дать ответ на вопрос: есть ли среди цифр числа 5?')
integer_number = 213415
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
print()
print('Задача 9. Найти максимальную цифру в числе')
integre_find = 1234530000000000000000000076
count = 0
count2 = 0
max_number_find = 0
while integre_find>0:
    count2+=1
    #print('Ряд поиска с промежуточными расчетами и проверками', max_number_find, count, count2, integre_find, integre_find % 10, max_number_find)
    buffer = integre_find % 10
    if max_number_find < buffer :
       count+=1
       max_number_find = buffer
    integre_find = integre_find//10

print('Максимальная цифра = ', max_number_find)

'''
Задача 10
Найти количество цифр 5 в числе
'''
print()
print('Задача 10 Найти количество цифр 5 в числе')
integre_find_5 = 56545658452555555
count5 = 0
number_find = 5
while integre_find_5>0:
    if integre_find_5 % 10 == number_find:
     count5+=1
    integre_find_5 = integre_find_5//10
print('количество цифр 5 = ', count5)

