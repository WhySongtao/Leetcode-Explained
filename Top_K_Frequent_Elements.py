def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        answer = []
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        index_list = [None] * (len(nums)+1)

        for key, count in counts.items():
            if index_list[count] is None:
                index_list[count] = []
            index_list[count].append(key)

        i = len(index_list) - 1
        while len(answer) < k and (i >= 0):
            if index_list[i]:
                for item in index_list[i]:
                    answer.append(item)
                    if len(answer) == k:
                        break
            i -= 1
        return answer

nums = [4,1,-1,2,-1,2,3]
k = 2

print(topKFrequent(nums, k))

import collections
print(collections.Counter(nums).most_common(2))
