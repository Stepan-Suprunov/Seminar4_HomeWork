#  Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#  Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#  Пользователь вводит 2 числа. n - кол-во элементов первого множества.
#  m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

my_collection_1 = []
my_collection_2 = []

n = int(input('Введите колличество элементов первого множества: '))
m = int(input('Введите колличество элементов второго множества: '))

for _ in range(n):
    my_collection_1.append(int(input('Введите число в первое множество: ')))
for _ in range(m):
    my_collection_2.append(int(input('Введите число во второе множество: ')))

my_collection_1 = set(my_collection_1)
my_collection_2 = set(my_collection_2)
my_collection_result = my_collection_1.intersection(my_collection_2)

my_collection_result = list(my_collection_result)
my_collection_result.sort()

print(my_collection_1)
print(my_collection_2)
print(my_collection_result)


#  В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
#  причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
#  Всего на грядке растет N кустов.
#  Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
#  различное число ягод – на i-ом кусте выросло ai ягод.
#  В этом фермерском хозяйстве внедрена система автоматического сбора черники.
#  Эта система состоит из управляющего модуля и нескольких собирающих модулей.
#  Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
#  собирает ягоды с этого куста и с двух соседних с ним.
#  Напишите программу для нахождения максимального числа ягод,
#  которое может собрать за один заход собирающий модуль,
#  находясь перед некоторым кустом заданной во входном файле грядки.

my_list = [1, 2, 3, 4]
max_quantity = 0

for i in range(len(my_list)):
    if i == 0:
        quantity = my_list[len(my_list)-1] + my_list[i] + my_list[i + 1]
    elif i == len(my_list) - 1:
        quantity = my_list[i - 1] + my_list[i] + my_list[0]
    else:
        quantity = my_list[i-1] + my_list[i] + my_list[i+1]
    if quantity > max_quantity:
        max_quantity = quantity
print(max_quantity)
