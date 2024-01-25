def wagner_fischer(a, b):
    m = len(a)
    n = len(b)
    
    # swap so as always to have shorter string in a
    if m > n:
        a, b = b, a
        m, n = n, m

    current = range(m+1)

    print(current)

    for i in range(1, n+1):
        previous, current = current, [i]+[0]*m
        for j in range(1, m + 1):
            add, delete, change = previous[j]+1, current[j-1]+1, previous[j-1]
            if a[j-1] != b[i-1]:
                change += 1
            current[j] = min(add, delete, change)
    return current[m]


def main():
    print(wagner_fischer('kitten', 'sitting'))

main()
