unsorted_list = [5, 8, 3, -100, 100, 16, 4, 2, 1]
# This function sorts the list by iterating through each element and swapping it with any smaller element found ahead in the nested loop.
# It repeats this process for each element in the outer loop, effectively pushing the smallest elements to the front of the list.
def mysort(unsorted_list):
    length = len(unsorted_list)
    for i in range(length):
        for j in range(i + 1, length):
            if unsorted_list[i] > unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    
    return unsorted_list

print(mysort(unsorted_list))
        
