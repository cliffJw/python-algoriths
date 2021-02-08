def soln(N):
    num = []
    while N > 0:
        if (1<=N<=9):
            num.append(N)
            num.sort()
            N = 0
            number = int(''.join(map(str, num)))
        else:
            num.append(9)
            N -= 9
    return number
    

print(soln(22))
print(soln(100))
