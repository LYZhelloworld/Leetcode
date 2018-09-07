class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int result = 0;
        Map<Integer, Integer> counts = new HashMap<>();
        
        for(int i = 0; i < points.length; i++) {
            for(int j = 0; j < points.length; j++) {
                if(i == j) continue; // Ignore same points
                
                int dist = getDistance(points[i], points[j]);
                counts.put(dist, counts.getOrDefault(dist, 0) + 1);
            }
            
            for(int v : counts.values()) {
                result += v * (v - 1); // n points with the same distance can form n(n-1) boomerangs
            }
            counts.clear();
        }
        
        return result;
    }
    
    private int getDistance(int[] a, int[] b) {
        int x = a[0] - b[0];
        int y = a[1] - b[1];
        return x * x + y * y;
    }
}
