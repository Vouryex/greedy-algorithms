def select_min(sequence):
    min = sequence[0]
    for i in range(1, len(sequence)):
        n = sequence[i]
        if n < min:
            min = n
    return min


def selection_sort(sequence):
    sorted_sequence = []
    while len(sequence) != 0:
        min = select_min(sequence)
        sorted_sequence.append(min)
        sequence.remove(min)
    print(sorted_sequence)


sequence = [5, 8, 3, 7, 1, 9, 11, 4, 2]
selection_sort(sequence)

# time complexity: O(n^2)
