# Онлайн-университет URBAN
# Домашняя работа по уроку "Функции в Python.Функция с параметром"
# Задача "Матрица воплоти"

def get_matrix(n, m, value):
    matrix = []
    #n = n - 1
    #m = m - 1
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append([j])
            matrix[i][j] = value
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(1, 3, 'УРА!!!')
result5 = get_matrix(1, 1, 'ПЛБЕДА!!!')
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
