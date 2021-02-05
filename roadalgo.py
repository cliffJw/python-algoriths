def solution(X, W, cnt=0):
    X.sort()
    v = X.copy()
    if len(X) != 0:
        for a in range(X[0], (X[0] + W + 1)):
            while a in v:
                v.remove(a)
            X = v
        cnt += 1
        return solution(X, W, cnt)
    else:
        return cnt 


print(solution([2, 4, 2, 6, 7, 1], 2))
print(solution([4, 8, 2, 2, 1, 4], 3))
print(solution([0, 3, 6, 5], 1))