class Solution {
    public int hammingDistance(int x, int y) {
        int z = x ^ y;
        // Now z contains all different bits
        int count = 0;
        for(int i = 0; i < 32; i++) {
            if((1 << i & z) > 0) count++;
        }
        return count;
    }
}
