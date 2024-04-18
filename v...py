def selection_sort(list1):
    n = len(list1)
    for i in range(n-1): 
        min= i 
        for j in range(i+1, n): 
            if list1[j]<list1[min]:
                min = j 
                temp=list1[i]
                list1[1]=list1[min]
                list1[min]=temp 
                return list1 
                list1 = [21,6,9,33,3] 
                print("The sorted array is: ", selection_sort(list1))
