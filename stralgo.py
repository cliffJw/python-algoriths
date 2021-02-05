def sol(S, B, cnt=0):
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
    print(cnt)       
    
sol("BAONXXOLL", "BALLOON")         
sol("BAOOLAONLNNOLOLLBLOGBAX", "BALLOON")
sol("ONLABLABOON", "BALLOON")     