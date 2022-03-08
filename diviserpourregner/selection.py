def selection(lst):
    UwU = 0
    for i in range(len(lst)):
        k = i
        for j in range(i+1, len(lst)):
            UwU +=1
            if lst[j] < lst[k]:
                k = j
        lst[i], lst[k] = lst[k], lst[i] 
    return lst, UwU

print(selection([1,5,3,8,7,5,5,7,9.36]))
        
    
    
