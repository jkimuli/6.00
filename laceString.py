def laceStrings(s1,s2):
    i = len(s1)
    j = len(s2)

    print i,j

    s3 = []

    s4 = ''

    if i > j:
        longer = s1
        s3_range = j

    else:
        longer = s2
        s3_range = i

    print longer,s3_range

    for s in range(s3_range):
        print s
        s3.append(s1[s])
        s3.append(s2[s])

        print s3

    s3.append(longer[s3_range:])

    print s4.join(s3)

    
    
