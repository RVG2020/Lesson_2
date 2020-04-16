print('#LIGHT:')
import random
from functools import reduce
print('#1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка')
# (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);
'''def func(x, y):
     a=3
     b=5
     return(a+x*y*b)
print(func(3,5))
'''

def f_N(Name, N):
    f_N_random = []
    #print(len(Name), N)
    k=int((N/(int(len(Name)))))
    Name = Name*k
    random.shuffle(Name) # mix
    f_N_random=Name
    print(len(f_N_random))
    return (f_N_random)

Name = ['Vasj1','Vasj2','Vasj3','Vasj4','Vasj5','Vasj6','Vasj7','Vasj8','Vasj9','Vasj10','Vasj11','Vasj12','Vasj13','Vasj14','Vasj15','Vasj16','Vasj17','Vasj18','Vasj19','Vasj20']
N = 100
print("Вариант №1 - mix", f_N(Name, N))



def func2(Fame,M):
    mylist_empy_M = list({i: i for i in range(0,M)})
    #print(mylist_empy_M)
    f_M_random2 = mylist_empy_M
    for i in range(0, M-1):
        f_M_random2[i] = Fame[random.randint(0, 19)] # ruletka
    print(len(f_M_random2))
    return (f_M_random2)

M = 100
Fame = ['Vasj1','Vasj2','Vasj3','Vasj4','Vasj5','Vasj6','Vasj7','Vasj8','Vasj9','Vasj10','Vasj11','Vasj12','Vasj13','Vasj14','Vasj15','Vasj16','Vasj17','Vasj18','Vasj19','Vasj20']
print("Вариант №2 - random", func2(Fame,M))


def func3(Secondname, L):
     #mylist_empy_L = list({j: j for j in range(0,L)})
     mylist_empy_L = int((N/(int(len(Secondname)))))*Secondname
     #f_L_random3 = list(map(lambda x: y[random.randint(0, 19)], mylist_empy_L, Secondname))
     f_L_random3 = list(map(lambda x: random.choice(mylist_empy_L), mylist_empy_L))
     print(len(f_L_random3))
     return (f_L_random3)

L = 100
Secondname = ['Vasj1','Vasj2','Vasj3','Vasj4','Vasj5','Vasj6','Vasj7','Vasj8','Vasj9','Vasj10','Vasj11','Vasj12','Vasj13','Vasj14','Vasj15','Vasj16','Vasj17','Vasj18','Vasj19','Vasj20']
print("Вариант №3 lambda",func3(Secondname,L))

''
print('#2. Напишите функцию вывода самого частого имени из списка на выходе функции F;')

def F_maxrepeat(List_Repeat):
    temp = List_Repeat
    print(temp)
    Max = 0
    g=0
    RR=0
    for g in range(g, (len(temp))-1):
        # формируем отфильтрованные списки по каждому значению
        Len_Repeat = list(filter(lambda x: x == temp[g], temp))
        # ищем самый длинный список
        if(len(Len_Repeat)>Max):
           Max = len(Len_Repeat)
           RR = temp[g]
        #print(Len_Repeat, Max, temp[g], RR)
           # запоминаем самое повторяемое имя
    Repeat = RR
    return (Repeat)
#может есть проще поиск ? Минус алгоритма ищет первое частоe имя?

List_Repeat = ['Vasj0', 'Vasj7', 'Vas6', 'Vas2', 'Vas', 'Vasj7', 'Vas', 'Vasj8', 'Vas65', 'Vasj1', 'Vasj0', 'Vasj12', 'Vasj13', 'Vasj14', 'Vasj15', 'Vasj16', 'Vas', 'Vas96', 'Vasj6', 'Vasj0']
print("Вариант  Ответ", F_maxrepeat(List_Repeat))





print('#3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.')


def F_maxrepeat_2(List_Repeat_2):
    temp2 = List_Repeat_2
    #temp2 = sorted(List_Repeat2, key = lambda x: x[0])
    #print(temp2)
    Min = len(List_Repeat_2)
    h=0
    Ren = 0
    for h in range(h, (len(temp2))-1):
        # формируем отфильтрованные списки по каждому значению
        onlyH = temp2[h]
        onlyTitle = onlyH[:1]
        #print(onlyH[:1])
        Len_Repeat2 = list(filter(lambda x: x[:1] == onlyTitle,temp2))
        #print(len(Len_Repeat2))
        # ищем самый короткий список
        if(len(Len_Repeat2)<Min):
           Min = len(Len_Repeat2)
           Ren = temp2[h]
        #print(Len_Repeat2, Min, temp2[h], Ren)
    # запоминаем самую не повторяемую букву имени
    Repeat2 = Ren [:1]
    #f_L_random4 = reduce(lambda a, b: a if a>b else b, List_Repeat)
    #f_L_random4 = list(filter(lambda x: x == 'мак'))
    #print(len(List_Repeat), List_Repeat)
    return (Repeat2)

#может есть проще поиск? минус алгоритма он ищет первое редкое. нужно усложнять алгоритм и выводить несколько редких?
List_Repeat_2 = ['Vasj0', 'Vasj0', 'Петя', 'jasj0', 'jasj5', 'asj7', 'Vasj1', 'Vasj8', 'j0', 'Vasj1', 'j0', 'j12', 'Vasj13', 'j14', 'Vasj15', 'Vasj16', 'Vasj5', 'Vasj18', 'Vasj6', 'Vasj0']
print("Вариант  Ответ", F_maxrepeat_2(List_Repeat_2))


#print('Далее Оптимальное решение')

'''
Роман, приветствую,
результаты правильные, с точки зрения более оптимизированных решений, на примере 3го задания можно такое написать
Нам же нужные первые буквы имен, при этом самые редкие
first_letters = [i[0] for i in List_Repeat2] # получаем их список перебором через доступ к текущему имени[первой букве]
temp_dict = {i: first_letters.count(i) for i in first_letters} # далее составляем словарь частотности этих букв в списке
rare_letter = list(temp_dict.items()) #преобразовываем в список кортежей-пар, чтобы можно было отсортировать
rare_letter.sort(key=lambda i: i[1]) # сортируем по кол-ву повторений в порядке возрастания
print(rare_letter[0]) #выдергиваем самый редкий(первый) элемент в отсортированном по частнотности списке букв
'''



def F_maxrepeat2(List_Repeat2):
    temp2 = List_Repeat2
    first_letters = [i[0] for i in List_Repeat2]  # получаем их список перебором через доступ к текущему имени[первой букве]
    #print(first_letters)
    temp_dict = {i: first_letters.count(i) for i in first_letters}  # далее составляем словарь частотности этих букв в списке
    #print(temp_dict)
    rare_letter = list(temp_dict.items())  # преобразовываем в список кортежей-пар, чтобы можно было отсортировать
    #print(rare_letter)
    rare_letter.sort(key=lambda i: i[1])  # сортируем по кол-ву повторений в порядке возрастания
    #print(rare_letter)
    #rare_letter0 = rare_letter1[0]
    #print(rare_letter[0])  # выдергиваем самый редкий(первый) элемент в отсортированном по частнотности списке букв
    first_list= list(rare_letter[0])
    first_paramentr = (first_list[0])
    #print(first_paramentr)
    #print(first_list)
    return(first_paramentr)

List_Repeat2 = ['Vasj0', 'Vasj0', 'Петя', 'jasj0', 'jasj5', 'asj7', 'Vasj1', 'Vasj8', 'j0', 'Vasj1', 'j0', 'j12', 'Vasj13', 'j14', 'Vasj15', 'Vasj16', 'Vasj5', 'Vasj18', 'Vasj6', 'Vasj0']
print("Оптимальный вариант  Ответ", F_maxrepeat2(List_Repeat2))


#PRO:

#LIGHT +

#4.  В файле с логами найти дату самого позднего лога (по метке времени): https://drive.google.com/open?id=1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8

print('пока без #PRO:')