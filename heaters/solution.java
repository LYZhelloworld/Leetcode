class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        Arrays.sort(heaters);
        int result = 0;
        
        for(int house : houses) {
            int index = Arrays.binarySearch(heaters, house);
            if(index < 0) {
                // Insertion point
                index = -(index + 1);
            }
                        
            int d;
            if(index == 0) {
                // Leftmost. Just compare one side
                d = heaters[index] - house;
            } else if (index > 0 && index < heaters.length) {
                // Compare two sides
                d = Math.min(house - heaters[index - 1], heaters[index] - house);
            } else/* (index >= heaters.length) */{
                // Rightmost. Just compare one side
                d = house - heaters[index - 1];
            }
            
            result = Math.max(result, d);
        }
        
        return result;
    }
}
