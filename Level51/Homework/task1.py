def number_of_duplicate_digits(ndigit):
    if ndigit == 1:
        return 0
    
    total = 9 * (10 ** (ndigit - 1))
    no_double = 9 * (9 ** (ndigit - 1))
    
    return total - no_double


# Sum of Triangular Numbers
def sum_triangular_numbers(n):
    if n < 0:
        return 0
    
    total = 0
    for i in range(1, n + 1):
        triangular_number = i * (i + 1) // 2
        total += triangular_number
        
    return total

# Array.diff
def array_diff(a, b):
    last = [ ]
    
    for i in a:
        if i not in b:
             last.append(i)
            
    return last

# Delete occurrences of an element if it occurs more than n times
def delete_nth(order,max_e):
    count = {}
    result = [] 

    for i in order:
        if i not in count or count[i] < max_e:
            result.append(i)
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
    
    return result
# Equal Sides Of An Array
def find_even_index(arr):
    total_sum = sum(arr) 
    left_sum = 0  
    
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]        

        if left_sum == right_sum:
            return i
        
        left_sum += arr[i]
    
    return -1