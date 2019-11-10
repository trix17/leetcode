A = [2, 7, 11, 15]
target = 17

def hashtable(A,target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            return(ht[A[i]],i)
        else:
            ht[target - A[i]] = i


print(hashtable(A,target))
