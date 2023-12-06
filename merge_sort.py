#1 - split the list
#2 recursively sort the split lists
#3 - merge sublists togethet
#4 - final merge, returning a sorted list

test_list = [-2,0,5,2,-7,4,1,3,-1,-3]
def merge_sort(list):
    #first define the base case
    if len(list)<=1:
        return list
    
    #split the list
    mid = len(list)//2
    left_half = list[:mid]
    right_half = list[mid:]

    #recursively merge sort sublists, then merge together 
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left,right):
    #empty list to add sorted elements to
    merged = []
    #two pointers
    left_index=0
    right_index=0

    while left_index<len(left) and right_index<len(right):
        # if the leftmost element of the left sublist is smaller than the leftmost element of the right sublist, add it to the merged list first
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
        #else add the leftmost element of the right sublist, so that the smallest value is added first
            merged.append(right[right_index])
            right_index += 1
    
    #when one of the sublists has been exausted, add the remaining (largest) element to the merged list
    merged += left[left_index:]
    merged += right[right_index:]
    
    #return the merged list
    return merged

print(merge_sort(test_list))
