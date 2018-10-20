def commons(universal_set, set):
    num_of_commons = 0
    for univ_el in universal_set:
        for el in set:
            if univ_el == el:
                num_of_commons += 1
    return num_of_commons


def set_diff(a, b):
    diff = []
    for a_el in a:
        has_common = False
        for b_el in b:
            if a_el == b_el:
                has_common = True
                break
        if not has_common:
            diff.append(a_el)
    return diff


def set_cover(universal_set, set_of_sets):
    solution_sets = []
    while len(universal_set) != 0:
        best_set = set_of_sets[0]
        best_commons_num = commons(universal_set, set_of_sets[0])
        for i in range(1, len(set_of_sets)):
            set = set_of_sets[i]
            num_of_commons = commons(universal_set, set)
            if num_of_commons > best_commons_num:
                best_set = set
                best_commons_num = num_of_commons
        universal_set = set_diff(universal_set, best_set)
        solution_sets.append(best_set)
    print(solution_sets)


universal_set = [1, 2, 3, 4, 5, 6, 7, 8]
set_of_sets = [[1, 2], [7, 8], [2, 3, 4, 5, 6, 7], [1, 2, 3, 4], [5, 6, 7, 8], [5, 6, 7]]
set_cover(universal_set, set_of_sets)

# time complexity: O(Σ of all S ∈ F: |S|) where F is a family of subsets of X,
# such that every element of X belongs to at least one subset in F, where X is
# a finite set referred to as the universal set
