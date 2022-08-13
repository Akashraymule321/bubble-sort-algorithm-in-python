

def selectionsort(itemlist):
    n=len(itemlist)
    for i in range (n-1):
        minValueIndex=i
        for j in range(i+1,n):
            print("i = ",i," j = ",j)
            if itemlist[j]< itemlist[minValueIndex]:
                minValueIndex=j
                # print(j)
        if minValueIndex!=i:
            temp=itemlist[i]
            itemlist[i]=itemlist[minValueIndex]
            itemlist[minValueIndex]=temp
    return itemlist

li=[9,5,8,2,6,4,1,2,3]
print(selectionsort(li))
