
arr = [1,5,4,2,9,9]
k = 3
def main(arr, k):
    max_ans = 0
    n = len(arr)
    window = set()
    window_sum = 0

    # toSide the window
    left = right = 0
    while right < n:
        # 1. Add elemnt till the windoe size is less than of equal to k
        #  element is not present in the window
        if window.find(arr[right]) == window.end():
            window.insert(arr[right])
            window_sum += arr[right]
            right += 1

            # 2. If window size exceed k
            while window.size() > k :
                window.erase(arr[left])
                window_sum -= arr[left]
                left += 1
            # 3. Whenver window size is k
            if window.size() == k:
                max_ans = max(max_ans, window_sum)

        else :
            window.erase(arr[left])
            window_sum -= arr[left]
            left += 1


    return max_ans

print(main(arr, k));