def get_input():
    number_of_people = int(input())
    events = [(-1, '')] * (number_of_people * 2)
    k = 0
    for i in range(number_of_people):
        temp = input().split(sep=" ")
        events[k] = (int(temp[0]), 'b')  # birth of new person
        k += 1
        events[k] = (int[temp[1]], 'd')  # death of someone
        k += 1
    return events



