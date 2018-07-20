 def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    start = 0
    max_len = 0
    seen_index = {}

    for i in range(len(s)):
        if s[i] in seen_index and start <= seen_index[s[i]]:
            # We have seen this element and this element is in the current sub-string, we need to
            # move the start to the next of this element to exclude it.
            start = seen_index[s[i]] + 1
        else:
            max_len = max(max_len, i - start + 1)

        seen_index[s[i]] = i

    return max_len
