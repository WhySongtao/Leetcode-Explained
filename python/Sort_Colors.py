# def sortColors(nums):
#     """
#     :type nums: List[int]
#     :rtype: void Do not return anything, modify nums in-place instead.
#     """
#     if len(nums) == 0:
#         pass
#
#     bucket = [0] * 3
#     for i in range(len(nums)):
#         bucket[nums[i]] += 1
#
#     index = 0
#     for i in range(len(bucket)):
#         count = bucket[i]
#         while count > 0:
#             nums[index] = i
#             index += 1
#             count -= 1

def sortColors(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            pass

        zero_index = 0
        two_index = len(nums) - 1

        index = 0
        while index <= two_index:
            while nums[index] == 2 and (index < two_index):
                nums[index], nums[two_index] = nums[two_index], nums[index]
                two_index -= 1
            while nums[index] == 0 and (index > zero_index):
                nums[index], nums[zero_index] = nums[zero_index], nums[index]
                zero_index += 1

            index += 1

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)
