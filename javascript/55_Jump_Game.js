/*
Thought: Have an index max_reach to keep track of the maximum index we can
reach so far. When looping through the array, if current index exceeds max_reach,
we know current index is not reachable.
*/


/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let max_reach = 0;
    for (let i = 0; i < nums.length; i++){
        if (i > max_reach) {
            return false;
        }
        max_reach = Math.max(max_reach, i + nums[i]);
    };

    return true;

};
