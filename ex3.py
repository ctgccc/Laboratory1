while True:
    try:
        n = int(input("Введите количество элементов в списке: "))
        break
    except ValueError:
        print("Вы ввели не число")
print("Введите элементы списка: \n")
a = [int(input()) for i in range(n)]
s = 0

for i in range(n):
   if a[i] > 0:
       s += a[i]
print("1)Сумма элементов списка:", s)

if 0 in a:
    print("2)Сумма элементов после первого нуля:",sum(a[a.index(0):]))
else:
    print("2)Сумму посчитать нельзя, так как нет в списке нет 0")

positive_numbers = []
for i in range(n):
    if a[i] >= 0:
        positive_numbers.append(a[i])
print("Список с положительными числами:", positive_numbers)