def flow_chart(a):
    """
    write from flow chart
    """
    l1, l2, l3 = [], [], []

    i = 0
    while i < len(a):
        if a[i] % 2 == 0:
            l1.append(a[i])
        elif a[i] % 3 == 0:
            l2.append(a[i])
        else:
            l3.append(a[i])

    return [l1, l2, l3]
