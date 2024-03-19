Minimum Window Substring: 

class Solution {
public:
    string minWindow(string s, string t) {
        // Lets create a map for string t
        map<char, int> t_freq;
        for (char c: t) {
            t_freq[c]++;
        }

        // How many unique characters I want in the window
        int required_unique = t_freq.size();

        // Lets create one more map for the window
        map<char, int> window_freq;

        // Variable to capture the size of window
        int window_size = 0;
        int min_len = 10e6;
        int min_window_left = 0;

        int left = 0, right = 0; // window pointers to slide
        
        // Slide the window 
        while (right < s.length()) {
            char c = s[right];
            window_freq[c]++;

            // Check if it present in t_freq, and check if the frequency matches
            if (t_freq.find(c) != t_freq.end() && \
                window_freq[c] == t_freq[c]) {
                    window_size++;
            }

            // Minimize the window as well: by throwing off the characters from the left, if not required
            while (left <= right && window_size == required_unique) {
                // Update the minimum values
                if (right - left + 1 < min_len) {
                    min_len = right - left + 1;
                    min_window_left = left;
                }

                char left_char = s[left];

                // reduce the size of the window from the left
                window_freq[left_char]--;

                // The left character is present, but not enough number of times
                if (t_freq.find(left_char) != t_freq.end() && window_freq[left_char] < t_freq[left_char]) {
                    window_size--;
                }

                left++;
            }
        
            right++;
        }
        
        return min_len == 10e6 ? "" : s.substr(min_window_left, min_len);
    }
};