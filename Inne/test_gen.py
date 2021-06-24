def matrix_non(n, edges):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for u, v in edges:
        result[u][v] = 1
    return result


def adjacency_non(n, edges):
    result = [[] for _ in range(n)]
    for u, v in edges:
        result[u].append(v)
    return result


def matrix_weight(n, edges):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for u, v, w in edges:
        result[u][v] = w
    return result


def adjacency_weight(n, edges):
    result = [[] for _ in range(n)]
    for u, v, w in edges:
        result[u].append([v, w])
    return result


if __name__ == "__main__":
    rep_type = input("representation: ")
    weight = int(input("weighted: "))
    m = int(input("number of vertexes: "))
    edge = []
    temp = input()
    while temp != "end":
        edge.append([int(x) for x in temp.split()])
        temp = input()
    if weight and rep_type == "matrix":
        end = matrix_weight(m, edge)
    elif weight and rep_type == "adjacency":
        end = adjacency_weight(m, edge)
    elif rep_type == "matrix":
        end = matrix_non(m, edge)
    else:
        end = adjacency_non(m, edge)
    print("[")
    for row in end:
        print(row, ",", sep="")
    print("]")
