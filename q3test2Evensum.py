def eveNumSq():
    elist=[1,2,3,4,5,6,7,8,9,10]
    sqlist = []
    for i in elist:
        if i % 2==0:
            sqlist.append(i*i)
    listsum=sum(sqlist)
    print ("even integer list is ->", sqlist, "sum of even numbers is in the given list is -> ",listsum)
    
eveNumSq()
