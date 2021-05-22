from random import randint


# generate list of random numbers
def gen_list(n, sm, big, repeat=True):
    if repeat is False and n > big - sm:
        print("Incorrect function input [gen_list]")
        return
    output = [0] * n
    temp = 0
    for i in range(n):
        temp = randint(sm, big)
        if repeat is False:
            while temp not in output:
                temp = randint(sm. big)
        output[i] = temp
    return output


# calculate length of vector (Euclidian)
def vector_length(vector):
    square_sum = 0
    for element in vector:
        square_sum += element ** 2
    return square_sum ** (1 / 2)
