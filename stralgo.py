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
