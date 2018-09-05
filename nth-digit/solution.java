class Solution {
    static final int[] POWERS_OF_10 = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};
    
    public int findNthDigit(int n) {
        int i, d = 1;
        for(i = 1;; ++i) {
            while(d < POWERS_OF_10.length && POWERS_OF_10[d] <= i) ++d;
            if(n - d > 0) {
                n -= d;
                continue;
            } else {
                return i / POWERS_OF_10[d - n] % 10;
            }
        }
    }
}
