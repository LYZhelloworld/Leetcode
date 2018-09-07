class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] res = new int[nums1.length];

        for(int i = 0; i < nums1.length; i++) {
            int j = search(nums2, nums1[i]);
            if(j == nums2.length - 1)
                res[i] = -1;
            else {
                boolean found = false;
                for(int k = j + 1; k < nums2.length; k++) {
                    if(nums2[k] > nums1[i]) {
                        found = true;
                        res[i] = nums2[k];
                        break;
                    }
                }
                if(!found) res[i] = -1;
            }
        }
        return res;
    }
    
    private int search(int[] arr, int target) {
        for(int i = 0; i < arr.length; i++)
            if(arr[i] == target) {
                return i;
            }
        return -1;
    }
}
