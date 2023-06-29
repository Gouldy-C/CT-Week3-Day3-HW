def toh(n, source, target, auxiliary):
    """
    Input: 2
    1 from source to auxiliary
    2 from source to target
    1 from auxiliary to target

    Input: 3
    1 from source to target
    2 from source to auxiliary
    1 from target to auxiliary
    3 from source to target
    1 from auxiliary to source
    2 from auxiliary to target
    1 from source to target
    
    Input: 4
    1 from source to auxiliary
    2 from source to target
    1 from auxiliary to target
    3 from source to auxiliary
    1 from target to source
    2 from target to auxiliary
    1 from source to auxiliary
    4 from source to target
    1 from auxiliary to source
    2 from auxiliary to target
    1 from source to target
    3 from auxiliary to target
    1 from source to auxiliary
    2 from source to target
    1 from auxiliary to target
    """
    if n == 1: print(f'Disc {n} from {source} to {target}')
    else:
        toh(n-1, source, auxiliary, target)
        print(f'Disc {n} from {source} to {target}')
        toh(n-1,auxiliary, target, source)


toh(1, 'source', 'target', 'auxiliary')
print('')
toh(2, 'source', 'target', 'auxiliary')
print('')
toh(3, 'source', 'target', 'auxiliary')
print('')
toh(4, 'source', 'target', 'auxiliary')
print('')