def levenshtein(seq1, seq2):
    n1, n2 = len(seq1) + 1, len(seq2) + 1
    A = [[0] * n1 for i in range(n2)]
    for i in range(n1):
        A[0][i] = i
    for i in range(n2):
        A[i][0] = i
    for i in range(1, n1):
        for j in range(1, n2):
            A[j][i] = 1 + min(A[j-1][i], A[j][i-1], A[j-1][i-1] - 1 + int(seq1[i-1] != seq2[j-1]))
    return A[-1][-1]

print(levenshtein('маша', 'дура'))
