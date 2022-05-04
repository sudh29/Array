def getMinMax( a, n):
    min_val=1000000
    max_val=-1000000
    for i in a:
        if i>max_val:
            max_val=i
        if i<min_val:
            min_val=i
    return [min_val,max_val]
    #return [min(a),max(a)]
