def lengthOfLongestSubstring(s: str) -> int:
    longest_substring_count = 0
    cur_substring_index = 0
    d = {}
    for i, v in enumerate(s):
        if v in d and d[v] >= cur_substring_index:
            cur_substring_index = d[v] + 1

        longest_substring_count = max(longest_substring_count, i - cur_substring_index + 1)
        d[v] = i


        # if v in d:
        #     # longest_count = max(longest_count, d[v] + 1)
        #     pass
        # else:
        #     d[v] = i
        #     longest_count = max(longest_count, d[v] + 1)

    return longest_substring_count


if __name__ == '__main__':
    print(lengthOfLongestSubstring('dvdf'))
