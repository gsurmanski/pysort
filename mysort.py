unsorted_list = [1,2,3]

def mysort(unsorted_list):
    length = len(unsorted_list)
    for i in range(length):
        for j in range(i + 1, length):
            print(i,j)
            if unsorted_list[i] > unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    
    #return unsorted_list

print(mysort(unsorted_list))
        