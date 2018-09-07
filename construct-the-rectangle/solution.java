class Solution {
    public int[] constructRectangle(int area) {
        // start from sqrt(area), find factor of area
        // Worst case is 1
        int res[] = new int[2];
        
        for(int i = (int) Math.sqrt(area); i > 0; i--) {
            if(area % i == 0){
                res[0] = area / i;
                res[1] = i;
                break;
            }
        }
        return res;
    }
}
