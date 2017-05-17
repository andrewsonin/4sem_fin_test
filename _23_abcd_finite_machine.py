def finite_machine(seq):  # 'abcd' search
    state = 0
    for i in range(len(seq)):
        char = seq[i]
        if char == 'a':
            state = 1
        elif state == 1 and char == 'b':
            state = 2
        elif state == 2 and char == 'c':
            state = 3
        elif state == 3 and char == 'd':
            return i - 3
        else:
            state = 0
    return -1

my_seq = input()
print(finite_machine(my_seq))
