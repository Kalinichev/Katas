def find_it(seq):
    for i in set(seq):
        if seq.count(i) % 2:
            return i