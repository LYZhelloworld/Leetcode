class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        // See: https://leetcode.com/problems/poor-pigs/discuss/94266/Another-explanation-and-solution
        return (int) Math.ceil(
            Math.log(buckets)
            / 
            Math.log(minutesToTest / minutesToDie + 1)
        );
    }
}
