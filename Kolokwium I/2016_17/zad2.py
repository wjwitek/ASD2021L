"""
Proszę zaimplementować funkcję:
int SumBetween(int T[], int from, int to, int n);
Zadaniem tej funkcji jest obliczyć sumę liczb znelementowej tablicy T, które w posortowanej tablicy znajdywałyby się na pozycjach
o indeksach od from do to (włącznie). Można przyjąć, że liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego
rozkładu danych).Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożonośćczasową (oraz bardzo krótko uzasadnić to oszacowanie).
"""
from select import quick_select
from random import randint


# use quick_select on whole T to find number on index from, then use quick_select on T
# from from to end to find index of two, it will also put all correct elements between them
def sum_between(array, f, t):
    n = len(array)
    from_index = quick_select(array, 0, n-1, f+1)
    to_index = quick_select(array, f+1, n-1, t-f)
    my_sum = 0
    for i in range(f, t+1):
        my_sum += array[i]
    return my_sum


test = [randint(1, 20) for _ in range(15)]
print(test)
print(sum_between(test, 4, 7))
print(test)

