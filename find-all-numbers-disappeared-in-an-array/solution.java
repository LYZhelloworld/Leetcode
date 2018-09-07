class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> result = new LinkedList<>();
        
        for(int i = 0; i < nums.length; i++) {
            // Since 1 <= a[i] <= n, we mark a[a[i]] as negative, which means |a[i]| has appeared.
            // But array indexes start from 0, so we mark a[a[i] - 1] instead.
            nums[Math.abs(nums[i]) - 1] = -Math.abs(nums[Math.abs(nums[i]) - 1]);
        }
        for(int i = 0; i < nums.length; i++) {
            // Find all non-negative indexes.
            if(nums[i] > 0) {
                result.add(i + 1);
            }
        }
        return result;
    }
}
