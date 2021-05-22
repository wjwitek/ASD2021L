# first sort them by x coordinate than in cases of same x coord sort by y coordinate
# all points have to be in relation with one another - otherwise impossible to do
def counting_sort(array, k, idx):
    counts = [0] * (k + 1)
    sorted_array = [0] * len(array)
    for i in array:
        counts[i[idx]] += 1
    for i in range(1, k + 1):
        counts[i] = counts[i] + counts[i - 1]
    for i in range(k + 1):
        counts[i] -= 1
    for i in range(len(array) - 1, -1, -1):
        sorted_array[counts[array[i][idx]]] = array[i]
        counts[array[i][idx]] -= 1
    return sorted_array


def radix_sort(array, d, r):
    for i in range(d, -1, -1):
        array = counting_sort(array, r, i)
    return array


def find_way(points, n):
    points = radix_sort(points, 1, 1000)
    way = "YES\n"
    for i in range(n - 1):
        if points[i + 1][1] < points[i][1]:
            return "NO"
        else:
            to_the_right = points[i + 1][0] - points[i][0]
            up = points[i + 1][1] - points[i][1]
            way += "R" * to_the_right
            way += "U" * up
    return way


def get_input():
    number_of_cases = int(input())
    cases = [0] * number_of_cases
    for i in range(number_of_cases):
        number_of_points = int(input())
        points = [(0, 0)] * (number_of_points + 1)
        for k in range(1, number_of_points + 1):
            point = input().split(sep=" ")
            point = (int(point[0]), int(point[1]))
            points[k] = point
        cases[i] = points
    return cases


if __name__ == "__main__":
    my_cases = get_input()
    for case in my_cases:
        print(find_way(case, len(case)))
