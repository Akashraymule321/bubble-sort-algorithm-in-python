#booble sort
import array as arr
#
def bubble_sort(itemList):
    a=itemList

    for i in range (len(a)):
        flag=0
        for j in range (len(a)-1):
            if (a[j]>a[j+1]):
                b=a[j]
                a[j]=a[j+1]
                a[j+1]=b
                flag=1
        if flag==0:break
    print(a)
a=[10,5,6,7,8,4]
bubble_sort(a)
