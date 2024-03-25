def rearrange_even_odd(arr):
    # Sort the array
    arr.sort()
    
    # Split the array into even and odd numbers
    even = [x for x in arr if x % 2 == 0]
    odd = [x for x in arr if x % 2 != 0]
    
    # Check if the rearrangement is possible
    if abs(len(even) - len(odd)) > 1:
        return "Rearrangement is not possible"
    
    # Merge the two arrays alternatively
    result = []
    even_index, odd_index = 0, 0
    turn_even = True if arr[0] % 2 == 0 else False
    
    for _ in range(len(arr)):
        if turn_even and even_index < len(even):
            result.append(even[even_index])
            even_index += 1
        elif not turn_even and odd_index < len(odd):
            result.append(odd[odd_index])
            odd_index += 1
        turn_even = not turn_even
    
    return result

# Example usage
arr = [2, 4, 5, 14, 35, 90, 11, 7, 15]
print(rearrange_even_odd(arr))
