# Define RNA sequence

# rna_seq = "AUGGCCAUUGUAAUGGGCCGCUGA"
rna_seq = 'ACGUCGAUUCGAGCGAAUCGUAACGAUACGAGCAUAGCGGCUAGAC'
# rna_seq = 'ACAUGAUGGCCAUGU'
# rna_seq = 'ACCGGUAGU'
#rna_seq = 'AAGACUUCGGAUCUGGCGACACCC'

# Auxiliary function for printing the optimal values array
def print_contents(opt_val):
    n = len(opt_val)
    for i in range(n - 5 - 1, -1, -1):
        print(i, end=': ')
        for j in range(5, n):
            print(str(opt_val[i][j]).rjust(2), end=' ')
        print()
    print('j:', end=' ')
    for j in range(5, n):
        print(str(j).rjust(2), end=' ')
    print()
    print()

# Valid base pairs: {A, U} and {C, G}
valid_pairs = [{'A', 'U'}, {'C', 'G'}]

# Function to check if two bases can be paired
def can_pair(base_1: str, base_2: str) -> bool:
    return {base_1, base_2} in valid_pairs

# Convert base pairings into dot-bracket notation
def get_dot_bracket_notation(n: int, sorted_pairs) -> str:
    structure = ['.'] * n
    for pair in sorted_pairs:
        structure[pair[0]] = '('
        structure[pair[1]] = ')'
    return ''.join(structure)

# Dynamic Programming algorithm to compute RNA secondary structure
def get_opt_val(sequence: str, n: int, opt_val, opt_val_pairs, i: int, j: int) -> int:
    # Check if value is already computed
    if opt_val[i][j] != -1:
        return opt_val[i][j]

    # Consider each possible base pair (t, j)
    listT = []
    for t in range(i, j - 4):
        if can_pair(sequence[t], sequence[j]):
            if t == i:
                listT.append((t, 1 + opt_val[t + 1][j - 1]))
            else:
                listT.append((t, 1 + opt_val[i][t - 1] + opt_val[t + 1][j - 1]))
        else:
            listT.append((t, 0))

    # Find best t
    max_value = max(listT, key=lambda x: x[1], default=(None, 0))[1]
    t = next((t for t, value in listT if value == max_value), None)

    # Update optimal values
    if max_value > opt_val[i][j - 1]:
        opt_val[i][j] = max_value
    else:
        opt_val[i][j] = opt_val[i][j - 1]

    # Store base pairings
    if max_value > opt_val[i][j - 1]:
        if t is not None:
            opt_val_pairs[i][j].append((t, j))
            opt_val_pairs[i][j].extend(opt_val_pairs[t + 1][j - 1])
            if t != i:
                opt_val_pairs[i][j].extend(opt_val_pairs[i][t - 1])
    else:
        opt_val_pairs[i][j].extend(opt_val_pairs[i][j - 1])

    return opt_val[i][j]

# Compute RNA secondary structure
def compute_rna_secondary_structure(sequence) -> str:
    n = len(sequence)
    opt_val = [[-1 for _ in range(n)] for _ in range(n)]
    opt_val_pairs = [[[] for _ in range(n)] for _ in range(n)]

    # Initialize base cases
    for i in range(n):
        for j in range(n):
            if i >= j - 4:
                opt_val[i][j] = 0

    # Compute optimal secondary structure
    for k in range(5, n):
        for i in range(0, n - k):
            j = i + k
            _ = get_opt_val(sequence, n, opt_val, opt_val_pairs, i, j)

    sorted_pairs = sorted(opt_val_pairs[0][n - 1])
    sorted_pair_bases = [(sequence[i], sequence[j]) for i, j in sorted_pairs]
    dot_bracket_notation = get_dot_bracket_notation(n, sorted_pairs)

    return dot_bracket_notation, sorted_pairs, sorted_pair_bases, opt_val, opt_val_pairs

# Run RNA folding algorithm
dot_bracket_notation, sorted_pairs, sorted_pair_bases, opt_val, opt_val_pairs = compute_rna_secondary_structure(rna_seq)

# Print results
print(f'Sorted Pairs: {sorted_pairs}')
print(f'Base Pairings: {sorted_pair_bases}')
print(f'Dot-Bracket Notation: {dot_bracket_notation}')
