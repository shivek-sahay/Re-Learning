def rearrange_even_odd(arr):
    # Sort the array
    # arr.sort()
    
    # Split the array into even and odd numbers
    even = [x for x in arr if x > 0]
    odd = [x for x in arr if x < 0]
    print(even, odd)
    # Merge the two arrays alternatively
    result = []
    even_index, odd_index = 0, 0
    
    # Start with even or odd based on the smallest value
    turn_even = True if arr[0] < 0 else False
    
    while even_index < len(even) and odd_index < len(odd):
        if turn_even:
            result.append(even[even_index])
            even_index += 1
        else:
            result.append(odd[odd_index])
            odd_index += 1
        turn_even = not turn_even
    
    # Append the remaining elements from either even or odd
    result.extend(even[even_index:])
    result.extend(odd[odd_index:])
    
    return result

# Example usage
arr = [-5,-2,3,4,-1,9,-7,-10]
print(rearrange_even_odd(arr))
