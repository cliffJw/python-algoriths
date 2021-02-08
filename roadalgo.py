def solution(X, Y, W):
    count = 0
    while len(X) > 0:
        X.sort()
        for a in range(X[0], X[0]+W+1):
            while a in X:
                X.remove(a)
        count += 1
    return count


print(solution([2, 4, 2, 6, 7, 1], [], 2))
print(solution([4, 8, 2, 2, 1, 4], [], 3))
print(solution([0, 3, 6, 5], [], 1))
