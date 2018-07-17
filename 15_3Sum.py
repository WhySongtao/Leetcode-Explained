import unittest


def threeSum(nums):
    # we need at least 3 number to continue
    if len(nums) < 3:
        return []
    sorted_nums = sorted(nums)
    answer = []
    # Looping over each element. This will be the A.
    # The reason for the -2 is because we need at least 3 elements (A, B, C)
    for i in range(0, len(sorted_nums)-2):
        # This examines that if current A is the same as the previous
        # A, if it's the same, then all the answer from this step will
        # be the same as the previous one.
        if (i==0 or (sorted_nums[i] != sorted_nums[i-1])):
            lo = i + 1
            hi = len(sorted_nums) - 1
            target = 0 - sorted_nums[i]
            # Here we are starting two pointers, beginning and the end to
            # find all the pair that match the target.
            while(lo < hi):
                if (sorted_nums[lo]+sorted_nums[hi] == target):
                    answer.append([sorted_nums[i], sorted_nums[lo],
                    sorted_nums[hi]])
                    # we don't want a duplicate
                    while((lo < hi) and (sorted_nums[lo]==sorted_nums[lo+1])):
                            lo += 1
                    while((lo < hi) and (sorted_nums[hi]==sorted_nums[hi-1])):
                            hi -= 1

                    lo += 1
                    hi -= 1
                elif (sorted_nums[lo]+sorted_nums[hi] < target):
                    lo += 1
                else:
                    hi -= 1

    return answer


class TestThreeSum(unittest.TestCase):
    def test_threeSum(self):
        input = [1, 2]
        self.assertEqual(threeSum(input), [])
        input = [-1,0,1,2,-1,-4]
        self.assertEqual(threeSum(input), [[-1,-1,2],[-1,0,1]])
