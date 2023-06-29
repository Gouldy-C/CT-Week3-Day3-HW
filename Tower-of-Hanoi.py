def toh(n, source, auxiliary, target):
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
    if n == 1: print(f'{(source,target)}')
    else:
        toh(n-1, source, target, auxiliary)
        print(f'{(source,target)}')
        toh(n-1,auxiliary, source, target)


toh(1, 'A', 'B', 'C')
print('')
toh(2, 'A', 'B', 'C')
print('')
toh(3, 'A', 'B', 'C')
print('')
toh(4, 'A', 'B', 'C')
print('')