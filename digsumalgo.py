def soln(N):
    num = []
    return digit(N, num)
    
def digit(N, num):
    if N in range(1, 10):
        num.append(N)
        num.sort()
        number = int(''.join(map(str, num)))
        return number
    else:
        num.append(9)
        num.sort()
        N -= 9
        return digit(N, num)
    

print(soln(22))
print(soln(100))
