import java.lang.Math;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length, i, j;
        int[] numsA = nums1, numsB = nums2;
        if(m > n) {
            numsA = nums2; numsB = nums1;
            int tmpLength = m; m = n; n = tmpLength;
        }
        
        int imin = 0, imax = m, halfLen = (m + n + 1) / 2; // Integer division
        double maxOfLeft, minOfRight;
        for(; imin <= imax;) {
            i = (imin + imax) / 2;
            j = halfLen - i;
            
            if(i < m && numsB[j - 1] > numsA[i]) {
                imin = i + 1;
            } else if(i > 0 && numsA[i - 1] > numsB[j]) {
                imax = i - 1;
            } else {
                if(0 == i) {
                    maxOfLeft = numsB[j - 1];
                } else if(0 == j) {
                    maxOfLeft = numsA[i - 1];
                } else {
                    maxOfLeft = Math.max(numsA[i - 1], numsB[j - 1]);
                }
                
                if((m + n) % 2 == 1) {
                    return maxOfLeft;
                }
                
                if(i == m) {
                    minOfRight = numsB[j];
                } else if(j == n) {
                    minOfRight = numsA[i];
                } else {
                    minOfRight = Math.min(numsA[i], numsB[j]);
                }
                
                return (maxOfLeft + minOfRight) / 2;
            }
        }
        
        return 0; //
    }
}
