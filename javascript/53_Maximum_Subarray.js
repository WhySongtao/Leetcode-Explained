/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    if (nums.length === 0) {
        return 0;
    }

    // We need this line! Why? Because we can't set global_maximum to zero Because
    // we may have an all negative array as input.
    let curr_maximum = global_maximum = nums[0];
    nums.shift();
    nums.forEach(num => {
       // Essentially, we are testing if the previous element makes my maximum
       // even smaller. If so, we don't need it. We start from scratch.
       curr_maximum = Math.max(num, num + curr_maximum);
       global_maximum = Math.max(curr_maximum, global_maximum);
    });

    return global_maximum;
};
