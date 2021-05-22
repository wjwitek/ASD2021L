from random import randint, seed


# additional function - merge two sorted arrays
def merge(tab1, tab2):
    new_array = [0] * (len(tab1) + len(tab2))
    i, j, k = 0, 0, 0 # i - new_array, j - tab1, k - tab2
    # add elements to new_array until end of one of the arrays is reached
    while j < len(tab1) and k < len(tab2):
        if tab1[j] <= tab2[k]:
            new_array[i] = tab1[j]
            j += 1
        else:
            new_array[i] = tab2[k]
            k += 1
        i += 1
    # add remaining elements of tab1, tab2
    while j < len(tab1):
        new_array[i] = tab1[j]
        i += 1
        j += 1

    while k < len(tab2):
        new_array[i] = tab2[k]
        i += 1
        k += 1
    return new_array


def mergesort(T):
    # check for boundary condition
    if len(T) == 1:
        return T

    # divide T into two arrays
    T1, T2 = [0] * (len(T) // 2), [0] * (len(T) - len(T) // 2)
    for i in range(len(T) // 2):
        T1[i] = T[i]
    k = 0
    for i in range(len(T) // 2, len(T)):
        T2[k] = T[i]
        k += 1
    T = merge(mergesort(T1), mergesort(T2))
    return T
  
  
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
    if T[i] > T[i+1]:
        print("Błąd sortowania!")
        exit()
print("OK")