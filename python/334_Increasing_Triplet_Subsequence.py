import unittest


def increasingTriplet(nums):
    if len(nums) < 3:
        return False

    min1 = min2 = float('inf')

    for num in nums:
        if num <= min1:
            # Find the smallest number.
            min1 = num
        elif num <= min2:
            min2 = num
        else:
            # if num is bigger than min2, there is an implicitly guarantee that
            # there is a number that is smaller than min2.
            return True

    return False


class TestTriplet(unittest.TestCase):
    def test_true_case(self):
        input = [1, 0, 2, 9]
        self.assertTrue(increasingTriplet(input))

    def test_false_case(self):
        input = [5, 3, 4, 2, 1]
        self.assertFalse(increasingTriplet(input))
        input2 = [1, 2]
        self.assertFalse(increasingTriplet(input2))

if __name__ == '__main__':
    unittest.main()
