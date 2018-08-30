/*
First key point: XOR.
Second key point: z &= (z-1) will knock out the lowest one.
*/
/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
    let z = x ^ y;
    let count = 0;
    while (z) {
        count++;
        z &= z - 1;
    }

    return count;
};
