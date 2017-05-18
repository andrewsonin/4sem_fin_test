def prefix_function(seq):
    values = [0] * len(seq)
    for i in range(1, len(seq)):
        k = values[i - 1]
        while k > 0 and seq[i] != seq[k]:
            k = values[k - 1]
        if seq[i] == seq[k]:
            k += 1
        values[i] = k
    return values

# сам алгоритм Кнута-Морриса-Пратта заключается в добавлении в начало строки искомой подстроки и последующем вычислении префикс-функции
