def find_duplicates(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1
            
    most_common = []
    for num in counts:
        if counts[num] > 1:
            most_common.append(num)
    return most_common

print(find_duplicates([1, 2, 3, 2, 4, 1]))
print(find_duplicates([5, 6, 7]))
        
            
    
            