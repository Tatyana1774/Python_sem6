# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
s=input()
arr=list(map(int,(input()).split()))
n=len(arr)
c=0
for i in range(1,n-1):
    if (arr[i] > arr[i-1]) & (arr[i] > arr[i+1]):
        c+=1
print(c)

#2 вариант

# numbers = [5, 1, 5, 3, 6, 3, 4]
# count= 0
# for i in range(1, len(numbers)-1):
#     if numbers[i - 1] < numbers[i] > numbers[i+1]:
#         count += 1

# print(count)

#3 вариант

# n = int(input('Input quantity of numbers in array: '))
# listn = list(random.randint(0,10) for i in range(n))
# print(listn)
# count = 0
# list_res = []
# for i in range(1,n-1):
#     if listn[i] > listn[i-1] and listn[i] > listn[i+1]:
#         count += 1
#         list_res.append(listn[i])
# print(list_res)
# print(count)