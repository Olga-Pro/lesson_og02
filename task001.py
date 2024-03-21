'''
Вам даны заголовки двух отсортированных связанных списков list1 и list2.

Объедините два списка в один отсортированный список.
Список должен быть составлен путем сращивания узлов первых двух списков.

Возвращает заголовок объединенного связанного списка.

https://leetcode.com/problems/merge-two-sorted-lists/description/
'''

list1 = []
list2 = []
list3 = []

def two_sorted (list_1, list_2):
    list_1.extend(list_2)
    list_1.sort(key=None, reverse=False)
    return list_1

list1 = [1, 2, 4]
list2 = [1, 3, 4]

list3 = two_sorted(list1, list2)
print(list3)

list1 = []
list2 = []
print(two_sorted(list1, list2))