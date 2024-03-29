# sorting_algorithms.py
def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])
    
    return merge(left_half, right_half)

def merge(left_half, right_half):
    result = []
    left_index, right_index = 0, 0
    
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            result.append(left_half[left_index])
            left_index += 1
        else:
            result.append(right_half[right_index])
            right_index += 1
    
    result.extend(left_half[left_index:])
    result.extend(right_half[right_index:])
    
    return result