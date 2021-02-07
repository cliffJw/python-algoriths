#This is the initial code
"""def sol(S, B, cnt=0):
    S = list(S)
    B = list(B)
    for i in B:
        if i in S:
            S.remove(i)
            B.remove(i)
            if len(B)==0:
                cnt += 1
                B = list("BALLOON")
                return sol(S, B, cnt) 
            else:
                return sol(S, B, cnt)
    print(cnt) """
#This is the updated version on feb 7 2021
def sol(S, count=0):
    B = "BALLOON"
    for a in S:
        if a in B:
            S = S.replace(a, "", 1)
            B = B.replace(a, "", 1)
            print(S, B)
            if B == "":
                count += 1
                return sol(S, count)

    return count
    
sol("BAONXXOLL", "BALLOON")         
sol("BAOOLAONLNNOLOLLBLOGBAX", "BALLOON")
sol("ONLABLABOON", "BALLOON")     
