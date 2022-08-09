# Найти сумму чисел списка стоящих на нечетной позиции

list_num = [1, 2, 3, 5, 1, 5, 3, 10]

sum = 0

list_num = [list_num[i] for i in range(len(list_num)) if not i%2]
for i in range (len(list_num)): sum+= list_num[i]
print(sum)