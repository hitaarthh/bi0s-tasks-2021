for i in range(int(input("No of test cases : "))):
    a, b, r = map(int, input().split())
    c = 0
    for j in range(int(input("No of chopsticks in jar : "))):
        if int(input()) < (a + b):
            c += 1

    if c > r:
        print(c)
        print("Natsu")
    else:
        print(c)
        print("Grey")
