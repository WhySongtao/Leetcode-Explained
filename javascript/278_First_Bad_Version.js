var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        let start = 1;
        let end = n;
        while (start < end) {
            // Prevent overflow
            mid = start + Math.floor((end - start) /2)
            if (!isBadVersion(mid)) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }

        return end;
    };
};
