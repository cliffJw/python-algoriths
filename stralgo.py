#This is the updated version on feb 7 2021
def sol(S):
    count = 0
    B = "BALLOON"
    while len(S) >= len(B):
        for a in S:
            if a in B:
                S = S.replace(a, "", 1)
                B = B.replace(a, "", 1)
                if B == "":
                    count += 1
                    B = "BALLOON"

    return count
    
sol("BAONXXOLL")         
sol("BAOOLAONLNNOLOLLBLOGBAX")
sol("ONLABLABOON")     
