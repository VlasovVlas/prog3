n1, n2, n3, a1 = map(int, input('').split())
n4, n5, n6, a2 = map(int, input('').split())
n7, n8, n9, a3 = map(int, input('').split())

if n1 == 1 or n2 == 1 or n3 == 1:
    if n1 == 1:
        while n4 != 0:
            n4 = n4 - n1
            n5 = n5 - n2
            n6 = n6 - n3
            a2 = a2 - a1
            print(n4, n5, n6, a2)
            print()

        while n7 != 0:
            n7 = n7 - n1
            n8 = n8 - n2
            n9 = n9 - n3
            a3 = a3 - a1
            print(n7, n8, n9, a3)
            print()

    elif n2 == 1:
        while n5 != 0:
            n4 = n4 - n1
            n5 = n5 - n2
            n6 = n6 - n3
            a2 = a2 - a1
            print(n4, n5, n6, a2)
            print()

        while n8 != 0:
            n7 = n7 - n1
            n8 = n8 - n2
            n9 = n9 - n3
            a3 = a3 - a1
            print(n7, n8, n9, a3)
            print()

    elif n3 == 1:
        while n6 != 0:
            n4 = n4 - n1
            n5 = n5 - n2
            n6 = n6 - n3
            a2 = a2 - a1
            print(n4, n5, n6, a2)
            print()

        while n9 != 0:
            n7 = n7 - n1
            n8 = n8 - n2
            n9 = n9 - n3
            a3 = a3 - a1
            print(n7, n8, n9, a3)
            print()

elif n4 == 1 or n5 == 1 or n6 == 1:
    if n4 == 1:
        while n1 != 0:
            n1 = n1 - n4
            n2 = n2 - n5
            n3 = n3 - n6
            a1 = a1 - a2
            print(n1, n2, n3, a1)
            print()

        while n7 != 0:
            n7 = n7 - n4
            n8 = n8 - n5
            n9 = n9 - n6
            a3 = a3 - a2
            print(n7, n8, n9, a3)
            print()

    elif n5 == 1:
        while n2 != 0:
            n1 = n1 - n4
            n2 = n2 - n5
            n3 = n3 - n6
            a1 = a1 - a2
            print(n1, n2, n3, a1)
            print()

        while n8 != 0:
            n7 = n7 - n4
            n8 = n8 - n5
            n9 = n9 - n6
            a3 = a3 - a2
            print(n7, n8, n9, a3)
            print()

    elif n6 == 1:
        while n3 != 0:
            n1 = n1 - n4
            n2 = n2 - n5
            n3 = n3 - n6
            a1 = a1 - a2
            print(n1, n2, n3, a1)
            print()

        while n9 != 0:
            n7 = n7 - n4
            n8 = n8 - n5
            n9 = n9 - n6
            a3 = a3 - a2
            print(n7, n8, n9, a3)
            print()

elif n7 == 1 or n8 == 1 or n9 == 1:
    if n7 == 1:
        while n1 != 0:
            n1 = n1 - n7
            n2 = n2 - n8
            n3 = n3 - n9
            a1 = a1 - a3
            print(n1, n2, n3, a1)
            print()

        while n4 != 0:
            n4 = n4 - n7
            n5 = n5 - n8
            n6 = n6 - n9
            a2 = a2 - a3
            print(n4, n5, n6, a2)
            print()

    elif n8 == 1:
        while n2 != 0:
            n1 = n1 - n7
            n2 = n2 - n8
            n3 = n3 - n9
            a1 = a1 - a3
            print(n1, n2, n3, a1)
            print()

        while n5 != 0:
            n4 = n4 - n7
            n5 = n5 - n8
            n6 = n6 - n9
            a2 = a2 - a3
            print(n4, n5, n6, a2)
            print()

    elif n9 == 1:
        while n3 != 0:
            n1 = n1 - n7
            n2 = n2 - n8
            n3 = n3 - n9
            a1 = a1 - a3
            print(n1, n2, n3, a1)
            print()

        while n6 != 0:
            n4 = n4 - n7
            n5 = n5 - n8
            n6 = n6 - n9
            a2 = a2 - a3
            print(n4, n5, n6, a2)
            print()