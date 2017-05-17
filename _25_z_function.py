def z_function(seq):
    n = len(seq)
    values = [0] * n
    values[0] = n
    left = right = 0
    for i in range(1, n):
        if i <= right:
            values[i] = min(values[i - left], right - i + 1)
        while i + values[i] < n and seq[values[i]] == seq[i + values[i]]:
            values[i] += 1
        if values[i] + i - 1 > right:
            right = values[i] + i - 1
            left = i
    return values
