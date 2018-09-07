class Solution {
    public int findContentChildren(int[] g, int[] s) {
        int count = 0;
        Arrays.sort(s);
        Arrays.sort(g);
        for(int size : s) {
            for(int i = 0; i < g.length; i++) {
                if(g[i] <= size) {
                    count++;
                    g[i] = Integer.MAX_VALUE;
                    break;
                }
            }
        }
        return count;
    }
}
