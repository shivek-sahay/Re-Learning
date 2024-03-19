class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        // Let's perform the binary search on smaller array. Ensure that nums1 is smaller. 
        // Time Complexity: O(log(min(m, n)))
        if (m > n) {
            return findMedianSortedArrays(nums2, nums1);
        }

        // nums1 is infact the smaller array. 
        int total_length = m + n;

        // +1 ensures that left partition has one extra element if m+n is odd. 
        int half_length = (total_length + 1)/2;   

        int left = 0, right = m;

        while (left <= right) {
            int p_a = (left + right)/2;
            int p_b = half_length - p_a;

            // If one of the array is entirely occupied in left or right partition, we do not 
            // get 4 elements for the formula (max(a[p_a], b[p_b]) + min(a[p_a + 1], b[p_b + 1]))/2
            // One of them is nothing! So to avoid this, I will check for the extremes. 
            int max_left_a = (p_a == 0 ? -10e7 : nums1[p_a-1]);
            int max_left_b = (p_b == 0 ? -10e7 : nums2[p_b-1]);
            int min_right_a = (p_a == m ? 10e7 : nums1[p_a]);
            int min_right_b = (p_b == n ? 10e7 : nums2[p_b]);

            // Check if the condition is satisfied
            if (max_left_a <= min_right_b && max_left_b <= min_right_a) {
                if (total_length%2 == 0) {
                    return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b))/2.0;
                } else {
                    return max(max_left_a, max_left_b);
                }
            } else if (max_left_a > min_right_b) {
                right = p_a - 1;
            } else {
                left = p_a + 1;
            }
        }
        // Code should never reach here
        return -1;
    }
};