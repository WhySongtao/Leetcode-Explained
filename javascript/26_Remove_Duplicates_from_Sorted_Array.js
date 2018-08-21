/* Use tail variable to keep track of the index of non-duplicate sub-array.
   Increase tail by one once we found a different value.
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (!nums.length) { return 0; }

    let tail = 0;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[tail]) {
            tail += 1;
            nums[tail] = nums[i];
        }
    }

    return tail + 1;
};
