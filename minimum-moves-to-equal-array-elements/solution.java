class Solution {
    public int minMoves(int[] nums) {
        // Increasing every number except one can be considered as decreasing that number.
        // We should decrease the maximum number to the minimum one. i.e. (Maximum - minimum) steps.
        // Do this for every number. Total steps = sum(every number - minimum) = sum(every number) - minimum*length
        int sum = 0, minimum = Integer.MAX_VALUE;
        for(int n : nums) {
            sum += n;
            if(minimum > n) minimum = n;
        }
        return sum - minimum * nums.length;
    }
}
